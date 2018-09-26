
'''
#查看多比较句
f1 = open('..\data\汽车训练任务2.2改进.txt', 'r')
list_stan = []
for line1 in f1.readlines():
	if line1 == '\n':
		break
	else:
		list_stan.append(line1)
		#print(line1)

for i in range(len(list_stan)):
	if '，' in list_stan[i]:
		print(list_stan[i])

#测试结果是否一致
f1=open('F:\Comparative-factor-extraction\CRF++\\test_answer.txt','r')
f2=open('F:\Comparative-factor-extraction\CRF++\\test_answerT2.txt','r')
listf1=[]
listf2=[]
for line in f1.readlines():
	if line == '\n':
		break
	else:
		result=line.split()
		print(result[3])
		listf1.append(result[3])

for line in f2.readlines():
	if line == '\n':
		break
	else:
		result=line.split()
		print(result[4])
		listf2.append(result[4])

for i in range(len(listf1)):
	if listf1[i]!=listf2[i]:
		print('false')
'''
import re
#人工标注是否正确格式
f1=open('..\data\汽车训练任务2.2改进.txt','r')
#f1=open('..\CRF++\\testT5.txt','r')
#f2=open('..\data\汽车测试语料.txt','r')
#f3=open('..\data\汽车测试比较句.txt','w')
list_len=[]
list=[]
i=0
for line1 in f1.readlines():
	i=i+1
	if line1 == '\n':
		break
	else:
		result_0 = line1.split()
		if result_0.__len__()!=8:
			print(line1,i)
		else:
			#print(result_0[0]+" "+result_0[1]+" "+result_0[2]+" "+result_0[3]+" "+result_0[4]+" "+result_0[5])
			list.append(result_0[1])
list_index=sorted(set(list))
#print(len(list))
print(len(list_index))

list_index.append('prevent')
#测试集除了标记出的比较句剩余的句子
'''
num=0
for line2 in f2.readlines():
	#print(line2)
	if line2 == '\n':
		continue
	else:
		#print(line2) #同文章中
		result_0 = line2.split()
		if result_0[0] != list_index[num]:  # eg：DOC2
			print(line2)
			f3.write(line2)
			f3.write('\n')
		else:
			num=num+1

list2=[]
for line2 in f2.readlines():
	#print(line2)
	if line2 == '\n':
		break
	else:
		#print(line2)
		result_2 = line2.split()
		list2.append(result_2[0])
		#print(result_2[0])
		continue
print(len(list2))


num=0
for line2 in f2.readlines():
	#print(line2)
	if line2 == '\n':
		continue
	else:
		#print(line2) #同文章中
		result_0 = line2.split()
		if result_0[0] == list_index[num]:  # eg：DOC2
			print(line2)
			num=num+1
			f3.write(line2)
			f3.write('\n')

# print(result_2[0])

#测试集遗漏的句子
alist=[]
f3=open('..\data\汽车测试比较句other.txt','r')
f4=open('..\data\汽车测试比较句other2.txt','w')
for line3 in f3.readlines():
	if line3 == '\n':
		continue
	else:
		#print(line3)
		result_0 = line3.split()
		if 'a' in result_0[0]:
			alist.append(line3)
			f4.write(line3)
			f4.write('\n')
			print(line3)
			print('\n')
print(len(alist))



#从任务2.1中抽取训练比较句
f1=open('..\data\汽车训练任务2.1答案.txt','r')
f2=open('..\data\汽车训练语料.txt','r')
f3=open('..\data\汽车训练比较句.txt','w')
list_index=[]
for line1 in f1.readlines():
	if line1 == '\n':
		break
	else:
		result_0 = line1.split()
		if result_0[3]=='1':
			list_index.append(result_0[1])
list_index.append('prevent border')
print(len(list_index))
num=0
for line2 in f2.readlines():
		if line2 == '\n':
			break
		else:
			#print(line2) #同文章中
			result_0 = line2.split()
			if list_index[num] in result_0[0]:  # eg：DOC2
				print(line2)
				num=num+1
				f3.write(line2)
				f3.write('\n')
	'''
