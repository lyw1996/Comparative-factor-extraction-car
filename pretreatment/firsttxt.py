#!/usr/bin/python
# -*- coding :utf-8 -*-


import Defi_class

num=0
list=[]
list_answer=[]
f5=open('..\\data\汽车测试任务2.2改进.txt','w')
f1=open('..\\data\汽车测试任务2.2答案.txt','r',encoding='utf-8')
for line1 in f1.readlines():
	if line1 == '\n':
		break
	else:
		result1=line1.split()
		f2=open('..\data\汽车测试语料.txt','r')
		for line2 in f2.readlines():
			if line1 == '\n':
				break
			else:
				if result1[3] in line2 and result1[4] in line2:
					result2=line2.split()
					result_answer=(result2[0],result1[3],result1[4],result1[5])
					list_answer.append(result_answer)
					list.append(result2[0])
					#print(result2[0])
					num=num+1
					break
				elif result1[3] in line2 and result1[4]=='NULL':
					result2 = line2.split()
					result_answer = (result2[0], result1[3], result1[4], result1[5])
					list_answer.append(result_answer)
					list.append(result2[0])
					# print(result2[0])
					num = num + 1
					break
				elif result1[4] in line2 and result1[3]=='NULL':
					result2 = line2.split()
					result_answer = (result2[0], result1[3], result1[4], result1[5])
					list_answer.append(result_answer)
					list.append(result2[0])
					# print(result2[0])
					num = num + 1
					break
			#print(line1)
list_index=sorted(set(list))
for i in range(len(list_index)):
	for j in range(len(list_answer)):
		if list_index[i]==list_answer[j][0]:
			f5.write(list_answer[j][0]+' '+list_answer[j][1]+' '+list_answer[j][2]+' '+list_answer[j][3])
			f5.write('\n')



list_index.append('prevent cross-border') #不然下一个功能会越界
print(len(list_index))
list_sentence=[]
f2=open('..\\data\汽车测试语料.txt','r')
f3=open('..\\data\汽车测试比较句.txt','w')
num=0
for line2 in f2.readlines():
	if line2 == '\n':
		break
	else:
		result_0 = line2.split()
		if result_0[0]!= list_index[num]:  # eg：DOC2
			continue
		else:
			f3.write(line2)
			f3.write('\n')
			result_0 = line2.split('\t')  # 横向制表符对字符串进行切片
			result_1 = result_0[1].split('<')
			result_2 = result_1[0]  # 存放的是没有任何标签的整个句子
			raw_sentence = Defi_class.raw_sentence(result_0[0], result_2)
			list_sentence.append(raw_sentence)
			print(result_2)
			num = num + 1
print(list_sentence.__len__())
