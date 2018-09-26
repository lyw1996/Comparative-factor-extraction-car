#!/usr/bin/python
# -*- coding :utf-8 -*-
#!/usr/bin/python
# -*- coding :utf-8 -*-
import Defi_func
import Defi_class
import numpy as np
from stanfordcorenlp import StanfordCoreNLP
nlp = StanfordCoreNLP(r'E:\stanford\stanford-corenlp-full-2018-02-27/', lang='zh')

kw_candidate=Defi_func.readkeywords()
'''
f1=open('..\data\电子测试比较句.txt','r')
f2=open('..\data\电子测试任务2.2改进.txt','r')
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

raw_sentence=sentence_data('..\data\电子测试比较句.txt')
list_stan=result_data('..\data\电子测试任务2.2改进.txt')
def write_data(filewrite,raw_sentence,list_stan):
	f3=open(filewrite,'w')
	list_result = []
	for i in range(len(raw_sentence)):
		list_fea = nlp.pos_tag(raw_sentence[i].sentence)  # 存储的是tuple
		list_parse = nlp.parse(raw_sentence[i].sentence)  # 存储的是树
		str = ''  # 自定义一个根
		#print(list_parse)
		list_parse_fea = list_parse.split('\r\n')
		#print(list_parse_fea)
		#for num in range(len(list_fea)):
			#result = Defi_class.Feature(raw_sentence[i].index, list_fea[num][0], list_fea[num][1],list_fea[num][1],'','','OTHERS')
		num=0
		index=0
		list_chunk=[]
		for j3 in range(len(list_parse_fea)):
			# print(list_result[i] + str)
			# print(sr)
			if 'IP' in list_parse_fea[j3] :
				aindex = index
				for a in range(aindex, len(list_fea)):
					if list_fea[a][1] + ' ' + list_fea[a][0] in list_parse_fea[j3]:
						index = index + 1
						list_chunk.append(list_fea[a][1])
					else:
						break
				continue
			if 'ROOT' in list_parse_fea[j3] or 'IP' in list_parse_fea[j3]:
				continue
			if 'FRAG' in list_parse_fea[j3]:
				continue
			sl = list_parse_fea[j3].count('(')
			# print(sl)
			sr = list_parse_fea[j3].count(')')
			if 'IP' in list_parse_fea[j3 - 1] or 'ROOT' in list_parse_fea[j3 - 1] or 'FRAG' in list_parse_fea[j3 - 1]:
				if sl > sr:
					result_0 = list_parse_fea[j3].split('(')
					result_1 = result_0[1]
					str = result_1
					#print(str)
				elif sl == sr:
					result_0 = list_parse_fea[j3].split('(')
					result_1 = result_0[1].split()
					str = result_1[0]
					#print(str)
			num = num + sl - sr
			if num > 0:
				aindex=index
				for a in range(aindex , len(list_fea)):
					if list_fea[a][1] + ' ' + list_fea[a][0] in list_parse_fea[j3]:
						index = index + 1
						list_chunk.append(str)
						#print(list_parse_fea[j3] + str)
					else:
						break
				# print(str)
				#print(list_parse_fea[i] + str)
			elif num <= 0:
				aindex = index
				for a in range(aindex, len(list_fea)):
					if list_fea[a][1] + ' ' + list_fea[a][0] in list_parse_fea[j3]:
						index = index + 1
						list_chunk.append(str)
						#print(list_parse_fea[j3] + str)
					else:
						break
				#print(list_parse_fea[i] + str)
				# print(str + '  end   ')
				# print(str)
				num = 0
				# print(list_result[i] + str)
				if j3 + 1 < len(list_parse_fea):
					if 'IP' in list_parse_fea[j3 + 1]:
						num = 0
						continue
					result_0 = list_parse_fea[j3 + 1].split('(')
					if ')' in result_0[1]:
						result_1 = result_0[1].split()
						str = result_1[0]
					# print(str, num)
					else:
						result_1 = result_0[1]
						str = result_1
		# print(str, num)
		'''
		if len(list_chunk)!=len(list_fea):
			print(raw_sentence[i].index)
			print(list_fea[len(list_chunk)])
			'''
		for num in range(len(list_fea)):
			result = Defi_class.Feature(raw_sentence[i].index, list_fea[num][0], list_fea[num][1],list_fea[num][1],'','','OTHERS')
			result.chunk=list_chunk[num]
			list_result.append(result)
	print(len(list_result))
	for j1 in range(len(list_result)):
		for j2 in range(len(list_stan)):
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
		if list_result[j1].word == '的' and list_result[j1 - 1].result != list_result[j1].result:
			list_result[j1].result = 'OTHERS'
		if list_result[j1].word == '了' and list_result[j1 - 1].result != list_result[j1].result:
			list_result[j1].result = 'OTHERS'
		if list_result[j1].word == '不' and list_result[j1 + 1].result != list_result[j1].result:
			list_result[j1].result = 'OTHERS'
		if list_result[j1].word == '要' and list_result[j1 + 1].result != list_result[j1].result:
			list_result[j1].result = 'OTHERS'
		if list_result[j1].word == ',' or list_result[j1].word == '。':
			list_result[j1].result = 'OTHERS'
		# print(list_result[j1].result)
		# print(list_result[j1].result)
		f3.write(list_result[j1].word + ' ' + list_result[j1].pos + ' '  + list_result[j1].chunk + ' '+ list_result[j1].result)
		f3.write('\n')
		print(list_result[j1].word + ' ' + list_result[j1].pos + ' ' + list_result[j1].chunk + ' ' + list_result[
			j1].result)
		print('\n')
	return result_data

write_data('..\CRF++\\trainT5.txt', raw_sentence, list_stan)


