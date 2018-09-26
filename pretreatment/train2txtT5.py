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
def write_data(filewrite,raw_sentence,list_stan):
	f3=open(filewrite,'w')
	list_result = []
	for i in range(len(raw_sentence)):
		list_fea = nlp.pos_tag(raw_sentence[i].sentence)  # 存储的是tuple
		# print(list_fea)
		list_parse = nlp.parse(raw_sentence[i].sentence)  # 存储的是树
		# print(list_parse)
		list_parse_fea = (list_parse.split('\r\n'))
		# print(list_parse.split('('))
		for i2 in range(1, len(list_parse_fea)):
			list_parse_fea[i2] = list_parse_fea[i2].strip()
		# print(list_parse_fea[i])
		num = 0
		list_chunk = []
		for i3 in range(len(list_parse_fea)):
			for j3 in range(num, len(list_fea)):
				if list_fea[j3][1] + ' ' + list_fea[j3][0] in list_parse_fea[i3]:
					if 'DNP' in list_parse_fea[i3]:
						num = num + 1
						list_chunk.append('DNP')
					# print('DNP')
					elif 'ADVP' in list_parse_fea[i3]:
						num = num + 1
						list_chunk.append('ADVP')
					# print('ADVP')
					elif 'ADJP' in list_parse_fea[i3]:
						num = num + 1
						list_chunk.append('ADJP')
					# print('ADJP')
					elif 'PP' in list_parse_fea[i3]:
						num = num + 1
						list_chunk.append('PP')
					# print('PP')
					elif 'VP' in list_parse_fea[i3]:
						num = num + 1
						list_chunk.append('VP')
					# print('VP')
					elif 'NP' in list_parse_fea[i3]:
						num = num + 1
						list_chunk.append('NP')
					# print('NP')
					elif 'QP' in list_parse_fea[i3]:
						num = num + 1
						list_chunk.append('QP')
					# print('QP')
					elif 'LCP' in list_parse_fea[i3]:
						num = num + 1
						list_chunk.append('LCP')
					elif 'IP' in list_parse_fea[i3]:
						num = num + 1
						list_chunk.append('IP')
					elif 'INC' in list_parse_fea[i3]:
						num = num + 1
						list_chunk.append('INC')
					# print('LCP')
					else:
						count = 0
						for a in range(i3 - 1, 0, -1):
							# print(list_parse_fea[a])
							sl = list_parse_fea[a].count('(')
							# print(sl)
							sr = list_parse_fea[a].count(')')
							count = count + sl - sr
							if count > 0:
								result_0 = list_parse_fea[a].split('(')
								result_1 = result_0[1]

								num = num + 1
								list_chunk.append(result_1)
								# print(result_1)
								break
							else:
								count = count
				else:
					break
		'''
		if len(list_chunk) != len(list_fea):
			print(raw_sentence[i].index)
			print(nlp.parse(raw_sentence[i].sentence))
			print(len(list_chunk), len(list_fea))
	'''
		for n in range(len(list_fea)):
			result = Defi_class.Feature(raw_sentence[i].index, list_fea[n][0], list_fea[n][1], '', '', '', 'OTHERS')
			result.chunk = list_chunk[n]
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


