#!/usr/bin/python
# -*- coding :utf-8 -*-
#按照分词结果评判
#测试结果不好，已经舍弃
import Defi_class
f1=open('F:\Comparative-factor-extraction\CRF++\output.txt','r')
f2=open('F:\Comparative-factor-extraction\CRF++\\test_answer.txt','r')
f3=open('F:\Comparative-factor-extraction\CRF++\evaluate.txt','w')

'''
#测试结果和答案是一样长的文件
num=0
list2=[]
list4=[]
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
		if list2[i]==list4[j]:
			num=num+1
			break
print(list2.__len__())
print(list4.__len__())
'''

list=[]#存放句子的编号，word,pos,result1训练结果，result
#先读取result1
i=0
for line1 in f1.readlines():
	if line1 == '\n':
		break
	else:
		result_1 = line1.split()
		result=Defi_class.Evaluation('',result_1[0],result_1[1],'','','',result_1[2],'')
		#print(result.word)
		list.append(result)
		i+=1
#print(len(list))
#往list里面放编号和result2
num=-1
for line2 in f2.readlines():
	num=num+1
	if line2 == '\n':
		break
	else:
		result_2=line2.split()
		list[num].index=result_2[0]
		list[num].result2=result_2[3]
		f3.write(list[num].index + ' ' + list[num].word + ' ' + list[num].pos + ' ' + list[num].result1 + ' ' + list[num].result2)
		f3.write('\n')
print(len(list))

#评估词
target='SENTI'
#精确评估

list2=[]
for i2 in range(len(list)):
	list2.append(list[i2].index)
#print(list2)
list_index=sorted(set(list2))#句子去重
#print(list_index)


tp=0
fp=0
fn=0
for i1 in range(len(list_index)):
	num=0
	num1 =0
	num2=0
	for j1 in range(len(list)):
		if list_index[i1]==list[j1].index and list[j1].result1==target:
			num1+=1
		if list_index[i1]==list[j1].index and list[j1].result2==target:
			num2+=1
	if num1==num2 and num1!=0:
		tp+=1
		continue
	elif num2!=0:
		fp += 1
		continue
	elif num1!=0:
		fn += 1

print(tp)
print(fp)
print(fn)

precision = float(tp) / (tp + fp)
recall = float(tp) / (tp + fn)
f1 = 2 * precision * recall / (precision + recall)
print(target+'  Accurate Evaluation')
print("precision:%f recall:%f f1:%f" % (precision, recall, f1))


#覆盖结果，准确度，召回率，F1值
tp=0
fp=0
fn=0
for i in range(len(list)):
	#f3.write(list[i].index+' '+list[i].word+' '+list[i].pos+' '+list[i].result1+' '+list[i].result2)
	#f3.write('\n')
	if list[i].result1==target and list[i].result2==target:
		tp += 1
		continue
	elif list[i].result1!=target and list[i].result2==target:#标注的正确答案-识别出对的
		fp+=1
		continue
	elif list[i].result1==target and list[i].result2!=target:#系统识别出的-识别出对的
		fn+=1

print(tp)
print(fp)
print(fn)

precision = float(tp)/(tp+fp)
recall = float(tp)/(tp+fn)
f1=2 * precision * recall / (precision + recall)
print(target+'  Coverage Evaluation')
print("precision:%f recall:%f f1:%f" % (precision, recall, f1))
'''
num=0
list=[]

for line1 in f1.readlines():
	if line1 == '\n':
		break
	else:
		result_1 = line1.split()
		f3.write(result_1[0]+" "+result_1[1]+" "+result_1[2])
		f3.write('\n')
num=0

num=0
list2=[]
list4=[]for line2 in f2.readlines():

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
		if list2[i]==list4[j]:
			num=num+1
			break
print(list2.__len__())
print(list4.__len__())

'''



