#!/usr/bin/python
# -*- coding :utf-8 -*-
import Defi_class
def readT2T3(fileT2,fileT3,fileT4):
	f1 = open(fileT2, 'r')
	f2 = open(fileT3, 'r')
	f3 = open(fileT4, 'w')
	list_result = []
	for line1 in f1.readlines():
		if line1 == '\n':
			break
		else:
			result_0 = line1.split()
			result = Defi_class.Feature('',result_0[0],result_0[1],'',result_0[2],'',result_0[3])
			list_result.append(result)

	print(len(list_result))

	list_position=[]
	for line2 in f2.readlines():
		if line2== '\n':
			break
		else:
			result_0 = line2.split()
			list_position.append(result_0[2])

	for i in range(len(list_result)):
		list_result[i].position=list_position[i]
		f3.write(list_result[i].word+' '+list_result[i].pos+' '+list_result[i].keyword+' '+list_result[i].position+' '+list_result[i].result)
		f3.write('\n')
	print(len(list_position))

	return readT2T3

readT2T3('..\CRF++\\trainT2.txt','..\CRF++\\trainT3.txt','..\CRF++\\trainT4.txt')






#!/usr/bin/python
# -*- coding :utf-8 -*-