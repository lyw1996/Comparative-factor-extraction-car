#!/usr/bin/python
# -*- coding :utf-8 -*-
import Defi_func
import Defi_class
import re
import numpy as np
from stanfordcorenlp import StanfordCoreNLP
nlp = StanfordCoreNLP(r'E:\stanford\stanford-corenlp-full-2018-02-27/', lang='zh')
#从语料库中提取比较句
#list_sentence存放比较句的编号，没有任何标签的纯比较句
def sentence_data(fileresult,filedata,fileoutput):
	f1=open(fileresult,'r')
	list_index=[]
	list_sentence=[]
	list=[]
	for line in f1.readlines():
		if line=='\n':
			break
		else:
			m=re.search('\w+\d+',line)
			m_number=m.group(0)
			list.append(m_number)#带有重复的字符串
	list_index=sorted(set(list), key=list.index)
	list_index.append('prevent cross-border') #不然下一个功能会越界
	#print(list_index.__len__())  测试成功
	f2=open(filedata,'r')
	f3=open(fileoutput,'w')
	num=0
	for line2 in f2.readlines():
		if line2 == '\n':
			break
		else:
			# print(line2) #同文章中
			m2 = re.search('\w+\d+', line2)
			if m2.group(0) != list_index[num]:  # eg：DOC2
				continue
			else:
				f3.write(line2)
				f3.write('\n')
				result_0 = line2.split('\t')  # 横向制表符对字符串进行切片
				result_1 = result_0[1].split('<')
				result_2 = result_1[0]  # 存放的是没有任何标签的整个句子
				raw_sentence=Defi_class.raw_sentence(result_0[0],result_2)
				list_sentence.append(raw_sentence)
				#print(result_2) 测试成功
				num = num + 1
	#print(list_sentence.__len__())  测试成功
	list_sentence=np.array(list_sentence)
	return list_sentence

#读取手工标注的答案
#存入类为sentence的列表中
def result_data(fileanswer):
	f1=open(fileanswer,'r')
	list_stan = []
	for line1 in f1.readlines():
		if line1 == '\n':
			break
		else:
			result_0 = line1.split()
			#print(len(result_0))
			senten = Defi_class.Standard(result_0[1], result_0[3], result_0[4], result_0[5], result_0[6],result_0[7])
			list_stan.append(senten)
	list_stan=np.array(list_stan)
	return list_stan


raw_sentence=sentence_data('..\data\汽车训练任务2.2答案.txt','..\data\汽车训练语料.txt','..\data\汽车训练比较句.txt')
'''
#测试比较句存储成功
for i in range(len(raw_sentence)):
	print(raw_sentence[i].sentence)
'''
list_stan=result_data('..\data\汽车训练任务2.2改进.txt')

def num_stan(list_stan):
	num_sub = 0
	num_obj = 0
	num_attr = 0
	num_senti = 0
	num_kw = 0
	for i in range(len(list_stan)):
		if list_stan[i].sub == 'NULL':
			continue
		elif list_stan[i].sub == list_stan[i - 1].sub and list_stan[i].index == list_stan[i - 1].index:
			continue
		else:
			num_sub = num_sub + len(list_stan[i].sub.split('|'))
	#print(num_sub)

	for i in range(len(list_stan)):
		if list_stan[i].obj == 'NULL':
			continue
		elif list_stan[i].obj == list_stan[i - 1].obj and list_stan[i].index == list_stan[i - 1].index:
			continue
		else:
			num_obj = num_obj + len(list_stan[i].obj.split('|'))
	#print(num_obj)

	for i in range(len(list_stan)):
		if list_stan[i].attr == 'NULL':
			continue
		elif list_stan[i].attr == list_stan[i - 1].attr and list_stan[i].index == list_stan[i - 1].index:
			continue
		else:
			num_attr = num_attr + len(list_stan[i].attr.split('|'))
	#print(num_attr)

	for i in range(len(list_stan)):
		if list_stan[i].senti == 'NULL':
			continue
		elif list_stan[i].senti == list_stan[i - 1].senti and list_stan[i].index == list_stan[i - 1].index:
			continue
		else:
			num_senti = num_senti + len(list_stan[i].senti.split('|'))
	#print(num_senti)
	for i in range(len(list_stan)):
		if list_stan[i].kw == 'NULL':
			continue
		elif list_stan[i].kw == list_stan[i - 1].kw and list_stan[i].index == list_stan[i - 1].index:
			continue
		else:
			num_kw = num_kw + len(list_stan[i].kw.split('...'))
	#print(num_kw)
	return num_sub,num_obj,num_attr,num_senti,num_kw

'''
f4=open('feature.txt','w')
for num1 in range(len(list_stan)):
	f4.write(list_stan[num1].index+' '+list_stan[num1].sub+' '+list_stan[num1].obj+' '+list_stan[num1].attr+' '+list_stan[num1].senti)
	f4.write('\n')

#测试人工标注结果存储成功
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
		#print(list_fea)
		for num in range(len(list_fea)):
			result = Defi_class.Feature(raw_sentence[i].index, list_fea[num][0], list_fea[num][1], '', '', '', '')
			# f3.write(result.index +' '+result.word+' '+result.pos)
			# f3.write('\n')
			list_result.append(result)

	#print(list_result.__len__())
	#print(list_stan.__len__())
	'''
	for j2 in range(len(list_stan)):
		print(list_stan[j2].attr)
	'''
	#print(list_result.__len__())
	for j in range(len(list_result)):
		f3.write(list_result[j].word + ' ' + list_result[j].pos)
		f3.write('\n')
	'''
	for j1 in range(len(list_result)):
		for j2 in range(len(list_stan)):

			if list_result[j1].index == list_stan[j2].index and list_result[j1].word in list_stan[j2].sub:
				list_result[j1].result = 'SUB'
				#print(list_result[j1].index)
				break
			elif list_result[j1].index == list_stan[j2].index and list_result[j1].word in list_stan[j2].obj:
				list_result[j1].result = 'OBJ'
				#print(list_result[j1].index)
				break
			elif list_result[j1].index == list_stan[j2].index and list_result[j1].word in list_stan[j2].attr:
				list_result[j1].result = 'ATTR'
				#print(list_result[j1].index)
				break
			elif list_result[j1].index == list_stan[j2].index and list_result[j1].word in list_stan[j2].senti:
				list_result[j1].result = 'SENTI'
				#print(list_result[j1].index)
				break
			elif list_result[j1].index == list_stan[j2].index and list_result[j1].word in list_stan[j2].kw:
				list_result[j1].result = 'KW'
				#print(list_result[j1].index)
				break
			else:
				list_result[j1].result = 'OTHERS'
		# print(list_result[j1].result)
	'''
	return write_data

def write_evaluate(filewrite,raw_sentence,list_stan):
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
		#print(list_fea)
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

	#print(list_result.__len__())
	#print(list_stan.__len__())
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
				#print(list_result[j1].index)
				break
			elif list_result[j1].index == list_stan[j2].index and list_result[j1].word in list_stan[j2].obj:
				list_result[j1].result = 'OBJ'
				#print(list_result[j1].index)
				break
			elif list_result[j1].index == list_stan[j2].index and list_result[j1].word in list_stan[j2].attr:
				list_result[j1].result = 'ATTR'
				#print(list_result[j1].index)
				break
			elif list_result[j1].index == list_stan[j2].index and list_result[j1].word in list_stan[j2].senti:
				list_result[j1].result = 'SENTI'
				#print(list_result[j1].index)
				break
			elif list_result[j1].index == list_stan[j2].index and list_result[j1].word in list_stan[j2].kw:
				list_result[j1].result = 'KW'
				#print(list_result[j1].index)
				break
			else:
				list_result[j1].result = 'OTHERS'
		# print(list_result[j1].result)
	list_result[-1].result='OTHERS'
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
		f3.write(list_result[j1].index + ' ' +list_result[j1].word  + ' ' + list_result[j1].result)
		f3.write('\n')
	#print(len(list_result))
	return write_evaluate

write_data('..\CRF++\\testT1.txt',raw_sentence,list_stan)
write_evaluate('..\CRF++\\test_answer.txt',raw_sentence,list_stan)






