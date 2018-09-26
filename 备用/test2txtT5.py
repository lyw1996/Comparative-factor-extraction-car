#!/usr/bin/python
# -*- coding :utf-8 -*-
import Defi_class
import Defi_func
import re
import numpy as np
from stanfordcorenlp import StanfordCoreNLP
nlp = StanfordCoreNLP(r'E:\stanford\stanford-corenlp-full-2018-02-27/', lang='zh')

kw_candidate=Defi_func.readkeywords()
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
			senten = Defi_class.Standard(result_0[1], result_0[3], result_0[4], result_0[5], result_0[6],result_0[7])
			list_stan.append(senten)
	list_stan=np.array(list_stan)
	return list_stan


raw_sentence=sentence_data('..\data\电子训练任务2.2答案.txt','..\data\电子训练语料.txt','..\data\电子训练比较句.txt')
list_stan=result_data('..\data\电子训练任务2.2改进.txt')
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
		index=0
		num=0
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
			print(len(list_chunk),len(list_fea))
			'''
		for num in range(len(list_fea)):
			result = Defi_class.Feature(raw_sentence[i].index, list_fea[num][0], list_fea[num][1],'','','','OTHERS')
			result.chunk=list_chunk[num]
			list_result.append(result)

	print(list_result.__len__())
	print(list_stan.__len__())
	for j1 in range(len(list_result)):
		f3.write(list_result[j1].word + ' ' + list_result[j1].pos+ ' ' + list_result[j1].chunk)
		f3.write('\n')

	return write_data


write_data('..\CRF++\\testT5.txt',raw_sentence,list_stan)
