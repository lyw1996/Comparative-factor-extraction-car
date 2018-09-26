#!/usr/bin/python
# -*- coding :utf-8 -*-
import Defi_func
import Defi_class
import numpy as np
from stanfordcorenlp import StanfordCoreNLP
nlp = StanfordCoreNLP(r'E:\stanford\stanford-corenlp-full-2018-02-27/', lang='zh')
'''
f1=open('..\data\汽车测试比较句.txt','r')
f2=open('..\data\汽车测试任务2.2改进.txt','r')
f3=open('..\CRF++\\test.txt','w')
'''
#存放原始的待处理的比较句
#类为raw_sentence的列表
def sentence_data(fileresult):  #,filedata,fileoutput
	f1 = open(fileresult, 'r')
	list_sentence = []
	for line1 in f1.readlines():
		if line1 == '\n':
			continue
		else:
			result_0 = line1.split('\t')  # 横向制表符对字符串进行切片
			result_1 = result_0[1].split('<')
			result_2 = result_1[0]  # 存放的是没有任何标签的整个句子
			raw_sentence = Defi_class.raw_sentence(result_0[0], result_2)
			list_sentence.append(raw_sentence)
			#  测试成功
			# print(result_0[0])
			# print(result_2)
	# print(list_sentence.__len__())# 测试成功
	list_sentence=np.array(list_sentence)
	return list_sentence

#读取手工标注的答案
#存入类为sentence的列表中
def result_data(fileanswer):
	f2=open(fileanswer,'r')
	list_stan = []
	for line2 in f2.readlines():
		if line2 == '\n':
			break
		else:
			result_0 = line2.split()
			senten = Defi_class.Standard(result_0[0], result_0[1], result_0[2], result_0[3], result_0[4],result_0[5])
			list_stan.append(senten)
	list_stan=np.array(list_stan)
	return list_stan

raw_sentence=sentence_data('..\data\汽车测试比较句.txt')
list_stan=result_data('..\data\汽车测试任务2.2改进.txt')
#测试人工标注结果存储成功
'''
for num in range(len(list_stan)):
	print(list_stan[num].index,end=" ")
	print(list_stan[num].sub, end=' ')
	print(list_stan[num].obj, end=' ')
	print(list_stan[num].attr,end=' ')
	print(list_stan[num].senti,end=' ')
	print(list_stan[num].kw)
'''
def write_data(filewrite,raw_sentence,list_stan):
	f3=open(filewrite,'w')
	list_result = []
	for i in range(len(raw_sentence)):

		# 测试词性分词成功
		# print(isinstance(nlp.pos_tag(raw_sentence[i].sentence),tuple)) #结果为true stanford词性标注结果为tuple类型的list
		# tuple为不能更改的数组
		# print(nlp.pos_tag(raw_sentence[i].sentence))
		# list_fea = nlp.pos_tag(raw_sentence[i].sentence)
		# print(list_fea)
		# print(list_fea.__len__())

		list_fea = nlp.pos_tag(raw_sentence[i].sentence)  # 存储的是tuple
		print(list_fea)
		for num in range(len(list_fea)):
			'''
			word0=(list_fea[num][0])
			print(word0)
			word1=list_fea[num][1]
			print(word1)
			#print(word1)
	  		'''
			result = Defi_class.Feature(raw_sentence[i].index, list_fea[num][0], list_fea[num][1], '', '', '', '')
			# f3.write(result.index +' '+result.word+' '+result.pos)
			# f3.write('\n')
			list_result.append(result)

	print(list_result.__len__())
	print(list_stan.__len__())
	'''
	for j2 in range(len(list_stan)):
		print(list_stan[j2].attr)
	'''

	for j1 in range(len(list_result)):
		for j2 in range(len(list_stan)):
			'''
			if list_result[j1].index==list_stan[j2].index:
				print('a'in 'ab' and 'b'in 'ab')
			==返回true in也返回true and也是返回true
			f3.write(list_result[j1].index+' '+list_stan[j2].sub)
			f3.write('\n')
			'''
			if list_result[j1].index == list_stan[j2].index and list_result[j1].word in list_stan[j2].sub:
				list_result[j1].result = 'SUB'
				print(list_result[j1].index)
				break
			elif list_result[j1].index == list_stan[j2].index and list_result[j1].word in list_stan[j2].obj:
				list_result[j1].result = 'OBJ'
				print(list_result[j1].index)
				break
			elif list_result[j1].index == list_stan[j2].index and list_result[j1].word in list_stan[j2].attr:
				list_result[j1].result = 'ATTR'
				print(list_result[j1].index)
				break
			elif list_result[j1].index == list_stan[j2].index and list_result[j1].word in list_stan[j2].senti:
				list_result[j1].result = 'SENTI'
				print(list_result[j1].index)
				break
			elif list_result[j1].index == list_stan[j2].index and list_result[j1].word in list_stan[j2].kw:
				list_result[j1].result = 'KW'
				print(list_result[j1].index)
				break
			else:
				list_result[j1].result = 'OTHERS'

	for j1 in range(len(list_result)):
		if list_result[j1].word=='的' and list_result[j1-1].result!=list_result[j1].result:
			list_result[j1].result='OTHERS'
		if list_result[j1].word == '了' and list_result[j1 - 1].result != list_result[j1].result:
			list_result[j1].result = 'OTHERS'
		if list_result[j1].word == '不' and list_result[j1 + 1].result != list_result[j1].result:
			list_result[j1].result = 'OTHERS'
		if list_result[j1].word == '要' and list_result[j1 + 1].result != list_result[j1].result:
			list_result[j1].result = 'OTHERS'
		if list_result[j1].word == ',' or  list_result[j1].word == '。':
			list_result[j1].result = 'OTHERS'
		# print(list_result[j1].result)
		f3.write(list_result[j1].word + ' ' + list_result[j1].pos + ' ' + list_result[j1].result)
		f3.write('\n')
	return result_data

write_data('..\CRF++\\trainT1.txt', raw_sentence, list_stan)


