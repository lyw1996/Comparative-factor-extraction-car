#!/usr/bin/python
# -*- coding :utf-8 -*-
import Defi_class
def readT4T5(fileT4,fileT5,fileT6):
	f1 = open(fileT4, 'r')
	f2 = open(fileT5, 'r')
	f3 = open(fileT6, 'w')

	list_result = []
	for line1 in f1.readlines():
		if line1 == '\n':
			break
		else:
			result_0 = line1.split()
			result = Defi_class.Feature('', result_0[0], result_0[1], '', result_0[2], result_0[3], result_0[4])
			list_result.append(result)
	print(len(list_result))

	list_chunk = []
	for line2 in f2.readlines():
		if line2 == '\n':
			continue
		else:
			result_0 = line2.split()
			list_chunk.append(result_0[2])
	print(len(list_chunk))
	for i in range(len(list_result)):
		list_result[i].chunk = list_chunk[i]
		f3.write(list_result[i].word + ' ' + list_result[i].pos + ' ' + list_result[i].keyword + ' ' + list_result[
			i].chunk + ' ' + list_result[i].position + ' ' + list_result[i].result)
		f3.write('\n')
		print(list_result[i].word + ' ' + list_result[i].pos + ' ' + list_result[i].keyword + ' ' + list_result[
			i].chunk + ' ' + list_result[i].position + ' ' + list_result[i].result)
		print('\n')
	print(len(list_chunk))
	return readT4T5


readT4T5('..\CRF++\\trainT4.txt','..\CRF++\\trainT5.txt','..\CRF++\\trainT6.txt')






#!/usr/bin/python
# -*- coding :utf-8 -*-