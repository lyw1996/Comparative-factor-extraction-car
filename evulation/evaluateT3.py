#!/usr/bin/python
# -*- coding :utf-8 -*-
#将分词结果合并再测结果
import Defi_class
import sys
sys.path.append("/../")
import pretreatment.test2txtT1 as pre
def extraction():
	f1 = open('F:\Comparative-factor-extraction-car\CRF++\outputT3.txt', 'r')
	f2 = open('F:\Comparative-factor-extraction-car\CRF++\\test_answer.txt', 'r')
	f3 = open('F:\Comparative-factor-extraction-car\CRF++\evaluateT3.txt', 'w')
	'''
	# 测试结果和答案是一样长的文件
	num = 0
	list2 = []
	list4 = []
	for line2 in f2.readlines():
		if line2 == '\n':
			break
		else:
			list2.append(line2)
	for line4 in f1.readlines():
		if line4 == '\n':
			break
		else:
			list4.append(line4)
	for i in range(len(list2)):
		for j in range(len(list4)):
			if list2[i] == list4[j]:
				num = num + 1
				break
	print(list2.__len__())
	print(list4.__len__())
	'''
	list = []  # 存放句子的编号，word,pos,result1训练结果，result
	# 先读取result1
	i = 0
	for line1 in f1.readlines():
		if line1 == '\n':
			break
		else:
			result_1 = line1.split()
			result = Defi_class.Evaluation('', result_1[0],'' , '',result_1[1], result_1[2], result_1[3], '')
			# print(result.word)
			list.append(result)
			i += 1
	# print(len(list))
	# 往list里面放编号和result2
	num = -1
	for line2 in f2.readlines():
		num = num + 1
		if line2 == '\n':
			break
		else:
			result_2 = line2.split()
			list[num].index = result_2[0]
			list[num].result2 = result_2[2]
			f3.write(
				list[num].index + ' ' + list[num].word + ' ' + list[num].pos+ ' ' + list[num].keyword + ' ' + list[num].result1 + ' ' + list[
					num].result2)
			f3.write('\n')
	return list

f4=open('F:\Comparative-factor-extraction-car\CRF++\\result2T3.txt', 'w')
f5=open('F:\Comparative-factor-extraction-car\CRF++\\result1T3.txt', 'w')
list=extraction()

list2=[]
for i2 in range(len(list)):
	list2.append(list[i2].index)
#print(list2)
list_index=sorted(set(list2))#句子去重，存放不重复的编号
#print(list_index)
target='SENTI'
#print(len(list_pre))防止list被改
#for i in range(len(list_pre)):
	#print(list_pre[i].word)
result2_list=[]
#result2中的结果，结果连在一起
#if list[0].result2=='OTHERS':
	#list[0].word='NULL'
list_pre=extraction()
for j5 in range(len(list_pre)):
	if list_pre[j5].word=='.' or  list_pre[j5].word==',' or  list_pre[j5].word=='!':
		list_pre[j5].result2 = 'OTHERS'
	if list_pre[j5].word=='。' or  list_pre[j5].word=='，' or  list_pre[j5].word=='！':
		list_pre[j5].result2 = 'OTHERS'
	if list_pre[j5].word=='的' and list_pre[j5-1].result2!=list_pre[j5].result2:
		list_pre[j5].result2='OTHERS'
	if list_pre[j5].word == '了' and list_pre[j5 - 1].result2 != list_pre[j5].result2:
		list_pre[j5].result2 = 'OTHERS'
	if list_pre[j5].word == '不' and list_pre[j5 + 1].result2!= list_pre[j5].result2:
		list_pre[j5].result2 = 'OTHERS'
	if list_pre[j5].word == '要' and list_pre[j5 + 1].result2 != list_pre[j5].result2:
		list_pre[j5].result2 = 'OTHERS'
	if list_pre[j5].word == ',' or  list_pre[j5].word == '。':
		list_pre[j5].result2 = 'OTHERS'
if list_pre[0].result2=='OTHERS':
	list_pre[0].word='NULL'
for i1 in range(len(list_index)):
	for j1 in range(1,len(list_pre)):
		if list_pre[j1].index == list_index[i1] and list_pre[j1].result2 == list_pre[j1 - 1].result2 and list_pre[j1].result2 != 'OTHERS':
			list_pre[j1].word = list_pre[j1 -1].word+list_pre[j1].word
			list_pre[j1-1].word = 'NULL'
			continue
		elif list_pre[j1].index == list_index[i1] and list_pre[j1].result2 != list_pre[j1 - 1].result2 and list_pre[j1].result2 != 'OTHERS':
			continue
		elif list_pre[j1].index == list_index[i1] and list_pre[j1].result2 == 'OTHERS':
			list_pre[j1].word = 'NULL'
			continue
for j3 in range(len(list_pre)):
	if 'NULL'in list_pre[j3].word:
		continue
	else:
		target=Defi_class.target(list_pre[j3].index,list_pre[j3].word,list_pre[j3].result2)
		result2_list.append(target)
		#print(list_pre[j3].index+' '+list_pre[j3].word+' '+list_pre[j3].result2)
		f4.write(list_pre[j3].index + ' ' + list_pre[j3].word + ' ' + list_pre[j3].result2)
		f4.write('\n')
#print(len(result2_list))

list=extraction()
for j4 in range(len(list)):
	if list[j4].word=='.' or list[j4].word==','or list[j4].word=='!':
		list[j4].result1 = 'OTHERS'
	if list[j4].word == '。' or list[j4].word == '，' or list[j4].word == '！':
		list[j4].result1 = 'OTHERS'
	if list[j4].word=='的' and list[j4-1].result1!=list[j4].result1:
		list[j4].result1='OTHERS'
	if list[j4].word == '了' and list[j4 - 1].result1 != list[j4].result1:
		list[j4].result1 = 'OTHERS'
	if list[j4].word == '不' and list[j4 + 1].result1 != list[j4].result1:
		list[j4].result1 = 'OTHERS'
	if list[j4].word == '要' and list[j4 + 1].result1 != list[j4].result1:
		list[j4].result1 = 'OTHERS'
	if list[j4].word == ',' or  list[j4].word == '。':
		list[j4].result1 = 'OTHERS'
result1_list=[]
#result1中的结果，结果连在一起
if list[0].result1=='OTHERS':
	list[0].word='NULL'
for i1 in range(len(list_index)):
	for j1 in range(1,len(list)):
		if list[j1].index == list_index[i1] and list[j1].result1 == list[j1 - 1].result1 and list[j1].result1 != 'OTHERS':
			list[j1].word = list[j1 -1].word+list[j1].word
			list[j1-1].word = 'NULL'
			continue
		elif list[j1].index == list_index[i1] and list[j1].result1 != list[j1 - 1].result1 and list[j1].result1 != 'OTHERS':
			continue
		elif list[j1].index == list_index[i1] and list[j1].result1 == 'OTHERS':
			list[j1].word = 'NULL'
			continue
for j2 in range(len(list)):
	if list[j2].word in 'NULL' :
		continue
	else:
		target=Defi_class.target(list[j2].index,list[j2].word,list[j2].result1)
		result1_list.append(target)
		f5.write(list[j2].index + ' ' + list[j2].word + ' ' + list[j2].result1)
		f5.write('\n')
		#测试成功
		#print(list[j2].index+' '+list[j2].word+' '+list[j2].result1)
#print(len(result1_list))

def evaluation(target1):
	list_stan = pre.result_data('..\data\汽车训练任务2.2改进.txt')
	sub, obj, attr, senti, kw = pre.num_stan(list_stan)
	#print(pre.num_stan(list_stan))
	if target1=='SUB':
		fn=sub
	if target1=='OBJ':
		fn=obj
	if target1=='ATTR':
		fn=attr
	if target1=='SENTI':
		fn=senti
	if target1=='KW':
		fn=kw
	tp = 0
	fp = 0
	# print(len(list_index))
	for i4 in range(len(list_index)):
		# print(list_index[i4])
		for i5 in range(len(result1_list)):
			# print(result1_list[i5].index)
			if result1_list[i5].index == list_index[i4] and result1_list[i5].target == target1:
				fp += 1
				# print(fp)
				# print(result1_list[i5].word)
				for j5 in range(len(result2_list)):
					if result2_list[j5].index == list_index[i4] and result1_list[i5].word == result2_list[j5].word and \
							result2_list[j5].target == target1:
						tp += 1
						break
				# print(result1_list[i5].index)
				# print(tp)
	print(tp, end=' ')
	print(fp, end=' ')
	print(fn, end=' ')

	precision = float(tp) / (fp)
	recall = float(tp) / (fn)
	f1 = 2 * precision * recall / (precision + recall)
	strAcc=target1+'   Accurate    '+"precision:%f recall:%f f1:%f" % (precision, recall, f1)
	#print(target1 )
	#print('Accurate ',end=' ' )
	#print("precision:%f recall:%f f1:%f" % (precision, recall, f1))

	tp = 0
	fp = 0

	# print(len(list_index))
	for i4 in range(len(list_index)):
		# print(list_index[i4])
		for i5 in range(len(result1_list)):
			# print(result1_list[i5].index)
			if result1_list[i5].index == list_index[i4] and result1_list[i5].target == target1:
				fp += 1
				# print(fp)
				# print(result1_list[i5].word)
				for j5 in range(len(result2_list)):
					if result2_list[j5].index == list_index[i4] and (result1_list[i5].word in result2_list[j5].word) and \
							result2_list[j5].target == target1:
						tp += 1
						# print(result1_list[i5].index)
						break
					if result2_list[j5].index == list_index[i4] and (result2_list[j5].word in result1_list[i5].word) and \
							result2_list[j5].target == target1:
						tp += 1
						# print(result1_list[i5].index)
						break
				# print(tp)

	print(tp, end=' ')
	print(fp, end=' ')
	print(fn, end=' ')

	precision = float(tp) / (fp)
	recall = float(tp) / (fn)
	f1 = 2 * precision * recall / (precision + recall)
	strCov='Coverage  '+"precision:%f recall:%f f1:%f  " % (precision, recall, f1)
	#print('Coverage', end=' ')
	#print("precision:%f recall:%f f1:%f" % (precision, recall, f1))
	return strAcc,strCov








