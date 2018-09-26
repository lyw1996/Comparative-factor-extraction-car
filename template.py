#!/usr/bin/python
# -*- coding :utf-8 -*-

import Defi_func
#两个特征的模版
def template2(filename,w,t):
	f1=open(filename,'w')
	f1.write('# Unigram\n')
	num=00
	for i in range(-3,4):
		f1.write('U'+str(num)+':%x['+str(i)+','+str(w)+']')
		f1.write('\n')
		num=num+1
	f1.write('\n')
	for i in range(-3,4):
		f1.write('U'+str(num)+':%x['+str(i)+','+str(t)+']')
		f1.write('\n')
		num=num+1
	f1.write('\n')
	for i in range(0,3):
		f1.write('U' + str(num) + ':%x[' + str(i-1) + ',' + str(w) + ']')
		f1.write('/%x['+str(i) + ',' + str(w) + ']')
		f1.write('\n')
		num = num + 1
	f1.write('\n')
	for i in range(0,3):
		f1.write('U' + str(num) + ':%x[' + str(i-1) + ',' + str(t) + ']')
		f1.write('/%x['+str(i) + ',' + str(t) + ']')
		f1.write('\n')
		num = num + 1
	f1.write('\n')
	for i in range(-2,1):
		f1.write('U' + str(num) + ':%x[' + str(i) + ',' + str(w) + ']')
		f1.write('/%x[' + str(i+1) + ',' + str(w) + ']')
		f1.write('\n')
		num = num + 1
	f1.write('\n')
	for i in range(-2,1):
		f1.write('U' + str(num) + ':%x[' + str(i) + ',' + str(t) + ']')
		f1.write('/%x[' + str(i+1) + ',' + str(t) + ']')
		f1.write('\n')
		num = num + 1
	f1.write('\n')
	for i in range(-1,2):
		f1.write('U' + str(num) + ':%x[' + str(i-1) + ',' + str(t) + ']')
		f1.write('/%x[' + str(i) + ',' + str(t) + ']')
		f1.write('/%x[' + str(i+1) + ',' + str(t) + ']')
		f1.write('\n')
		num = num + 1
	f1.write('\n')
	f1.write('U' + str(num) + ':%x[' + str(0) + ',' + str(w) + ']')
	f1.write('/%x[' + str(0) + ',' + str(t) + ']')
	f1.write('\n')
	f1.write('\n')
	f1.write('# Bigram\n')
	f1.write('B')
	return

#三个特征的模版
def template3(filename,w,t,c):
	f1=open(filename,'w')
	f1.write('# Unigram\n')
	num=00
	for i in range(-3,4):
		f1.write('U'+str(num)+':%x['+str(i)+','+str(w)+']')
		f1.write('\n')
		num=num+1
	f1.write('\n')
	for i in range(-3,4):
		f1.write('U'+str(num)+':%x['+str(i)+','+str(t)+']')
		f1.write('\n')
		num=num+1
	f1.write('\n')
	for i in range(-3,4):
		f1.write('U'+str(num)+':%x['+str(i)+','+str(c)+']')
		f1.write('\n')
		num=num+1
	f1.write('\n')

	for i in range(0,3):
		f1.write('U' + str(num) + ':%x[' + str(i-1) + ',' + str(w) + ']')
		f1.write('/%x['+str(i) + ',' + str(w) + ']')
		f1.write('\n')
		num = num + 1
	f1.write('\n')
	for i in range(0,3):
		f1.write('U' + str(num) + ':%x[' + str(i-1) + ',' + str(t) + ']')
		f1.write('/%x['+str(i) + ',' + str(t) + ']')
		f1.write('\n')
		num = num + 1
	f1.write('\n')
	for i in range(0,3):
		f1.write('U' + str(num) + ':%x[' + str(i-1) + ',' + str(c) + ']')
		f1.write('/%x['+str(i) + ',' + str(c) + ']')
		f1.write('\n')
		num = num + 1
	f1.write('\n')

	for i in range(-2,1):
		f1.write('U' + str(num) + ':%x[' + str(i) + ',' + str(w) + ']')
		f1.write('/%x[' + str(i+1) + ',' + str(w) + ']')
		f1.write('\n')
		num = num + 1
	f1.write('\n')
	for i in range(-2,1):
		f1.write('U' + str(num) + ':%x[' + str(i) + ',' + str(t) + ']')
		f1.write('/%x[' + str(i+1) + ',' + str(t) + ']')
		f1.write('\n')
		num = num + 1
	f1.write('\n')
	for i in range(-2,1):
		f1.write('U' + str(num) + ':%x[' + str(i) + ',' + str(c) + ']')
		f1.write('/%x[' + str(i+1) + ',' + str(c) + ']')
		f1.write('\n')
		num = num + 1
	f1.write('\n')

	for i in range(-1,2):
		f1.write('U' + str(num) + ':%x[' + str(i-1) + ',' + str(t) + ']')
		f1.write('/%x[' + str(i) + ',' + str(t) + ']')
		f1.write('/%x[' + str(i+1) + ',' + str(t) + ']')
		f1.write('\n')
		num = num + 1
	f1.write('\n')
	for i in range(-1,2):
		f1.write('U' + str(num) + ':%x[' + str(i-1) + ',' + str(c) + ']')
		f1.write('/%x[' + str(i) + ',' + str(c) + ']')
		f1.write('/%x[' + str(i+1) + ',' + str(c) + ']')
		f1.write('\n')
		num = num + 1
	f1.write('\n')
	f1.write('U' + str(num) + ':%x[' + str(0) + ',' + str(w) + ']')
	f1.write('/%x[' + str(0) + ',' + str(t) + ']')
	f1.write('\n')
	f1.write('U' + str(num) + ':%x[' + str(0) + ',' + str(t) + ']')
	f1.write('/%x[' + str(0) + ',' + str(c) + ']')
	f1.write('\n')
	f1.write('\n')
	f1.write('# Bigram\n')
	f1.write('B')
	return


#四个特征的模版
def template4(filename,w,t,c,l):
	f1=open(filename,'w')
	f1.write('# Unigram\n')
	num=00
	for i in range(-3,4):
		f1.write('U'+str(num)+':%x['+str(i)+','+str(w)+']')
		f1.write('\n')
		num=num+1
	f1.write('\n')
	for i in range(-3,4):
		f1.write('U'+str(num)+':%x['+str(i)+','+str(t)+']')
		f1.write('\n')
		num=num+1
	f1.write('\n')
	for i in range(-3,4):
		f1.write('U'+str(num)+':%x['+str(i)+','+str(c)+']')
		f1.write('\n')
		num=num+1
	f1.write('\n')
	for i in range(-3,4):
		f1.write('U'+str(num)+':%x['+str(i)+','+str(l)+']')
		f1.write('\n')
		num=num+1
	f1.write('\n')

	for i in range(0,3):
		f1.write('U' + str(num) + ':%x[' + str(i-1) + ',' + str(w) + ']')
		f1.write('/%x['+str(i) + ',' + str(w) + ']')
		f1.write('\n')
		num = num + 1
	f1.write('\n')
	for i in range(0,3):
		f1.write('U' + str(num) + ':%x[' + str(i-1) + ',' + str(t) + ']')
		f1.write('/%x['+str(i) + ',' + str(t) + ']')
		f1.write('\n')
		num = num + 1
	f1.write('\n')
	for i in range(0,3):
		f1.write('U' + str(num) + ':%x[' + str(i-1) + ',' + str(c) + ']')
		f1.write('/%x['+str(i) + ',' + str(c) + ']')
		f1.write('\n')
		num = num + 1
	f1.write('\n')
	for i in range(0,3):
		f1.write('U' + str(num) + ':%x[' + str(i-1) + ',' + str(l) + ']')
		f1.write('/%x['+str(i) + ',' + str(l) + ']')
		f1.write('\n')
		num = num + 1
	f1.write('\n')

	for i in range(-2,1):
		f1.write('U' + str(num) + ':%x[' + str(i) + ',' + str(w) + ']')
		f1.write('/%x[' + str(i+1) + ',' + str(w) + ']')
		f1.write('\n')
		num = num + 1
	f1.write('\n')
	for i in range(-2,1):
		f1.write('U' + str(num) + ':%x[' + str(i) + ',' + str(t) + ']')
		f1.write('/%x[' + str(i+1) + ',' + str(t) + ']')
		f1.write('\n')
		num = num + 1
	f1.write('\n')
	for i in range(-2,1):
		f1.write('U' + str(num) + ':%x[' + str(i) + ',' + str(c) + ']')
		f1.write('/%x[' + str(i+1) + ',' + str(c) + ']')
		f1.write('\n')
		num = num + 1
	f1.write('\n')
	for i in range(-2,1):
		f1.write('U' + str(num) + ':%x[' + str(i) + ',' + str(l) + ']')
		f1.write('/%x[' + str(i+1) + ',' + str(l) + ']')
		f1.write('\n')
		num = num + 1
	f1.write('\n')

	for i in range(-1,2):
		f1.write('U' + str(num) + ':%x[' + str(i-1) + ',' + str(t) + ']')
		f1.write('/%x[' + str(i) + ',' + str(t) + ']')
		f1.write('/%x[' + str(i+1) + ',' + str(t) + ']')
		f1.write('\n')
		num = num + 1
	f1.write('\n')
	for i in range(-1,2):
		f1.write('U' + str(num) + ':%x[' + str(i-1) + ',' + str(c) + ']')
		f1.write('/%x[' + str(i) + ',' + str(c) + ']')
		f1.write('/%x[' + str(i+1) + ',' + str(c) + ']')
		f1.write('\n')
		num = num + 1
	f1.write('\n')
	for i in range(-1,2):
		f1.write('U' + str(num) + ':%x[' + str(i-1) + ',' + str(l) + ']')
		f1.write('/%x[' + str(i) + ',' + str(l) + ']')
		f1.write('/%x[' + str(i+1) + ',' + str(l) + ']')
		f1.write('\n')
		num = num + 1
	f1.write('\n')

	f1.write('U' + str(num) + ':%x[' + str(0) + ',' + str(w) + ']')
	f1.write('/%x[' + str(0) + ',' + str(t) + ']')
	f1.write('\n')
	f1.write('U' + str(num) + ':%x[' + str(0) + ',' + str(t) + ']')
	f1.write('/%x[' + str(0) + ',' + str(c) + ']')
	f1.write('\n')
	f1.write('U' + str(num) + ':%x[' + str(0) + ',' + str(t) + ']')
	f1.write('/%x[' + str(0) + ',' + str(l) + ']')
	f1.write('\n')
	f1.write('U' + str(num) + ':%x[' + str(0) + ',' + str(c) + ']')
	f1.write('/%x[' + str(0) + ',' + str(l) + ']')
	f1.write('\n')
	f1.write('\n')
	f1.write('# Bigram\n')
	f1.write('B')
	return


# 五个特征的模版
def template5(filename, w, t, c, l,s):
	f1 = open(filename, 'w')
	f1.write('# Unigram\n')
	num = 00
	for i in range(-3, 4):
		f1.write('U' + str(num) + ':%x[' + str(i) + ',' + str(w) + ']')
		f1.write('\n')
		num = num + 1
	f1.write('\n')
	for i in range(-3, 4):
		f1.write('U' + str(num) + ':%x[' + str(i) + ',' + str(t) + ']')
		f1.write('\n')
		num = num + 1
	f1.write('\n')
	for i in range(-3, 4):
		f1.write('U' + str(num) + ':%x[' + str(i) + ',' + str(c) + ']')
		f1.write('\n')
		num = num + 1
	f1.write('\n')
	for i in range(-3, 4):
		f1.write('U' + str(num) + ':%x[' + str(i) + ',' + str(l) + ']')
		f1.write('\n')
		num = num + 1
	f1.write('\n')
	for i in range(-3, 4):
		f1.write('U' + str(num) + ':%x[' + str(i) + ',' + str(s) + ']')
		f1.write('\n')
		num = num + 1
	f1.write('\n')

	for i in range(0, 3):
		f1.write('U' + str(num) + ':%x[' + str(i - 1) + ',' + str(w) + ']')
		f1.write('/%x[' + str(i) + ',' + str(w) + ']')
		f1.write('\n')
		num = num + 1
	f1.write('\n')
	for i in range(0, 3):
		f1.write('U' + str(num) + ':%x[' + str(i - 1) + ',' + str(t) + ']')
		f1.write('/%x[' + str(i) + ',' + str(t) + ']')
		f1.write('\n')
		num = num + 1
	f1.write('\n')
	for i in range(0, 3):
		f1.write('U' + str(num) + ':%x[' + str(i - 1) + ',' + str(c) + ']')
		f1.write('/%x[' + str(i) + ',' + str(c) + ']')
		f1.write('\n')
		num = num + 1
	f1.write('\n')
	for i in range(0, 3):
		f1.write('U' + str(num) + ':%x[' + str(i - 1) + ',' + str(l) + ']')
		f1.write('/%x[' + str(i) + ',' + str(l) + ']')
		f1.write('\n')
		num = num + 1
	f1.write('\n')
	for i in range(0, 3):
		f1.write('U' + str(num) + ':%x[' + str(i - 1) + ',' + str(s) + ']')
		f1.write('/%x[' + str(i) + ',' + str(l) + ']')
		f1.write('\n')
		num = num + 1
	f1.write('\n')

	for i in range(-2, 1):
		f1.write('U' + str(num) + ':%x[' + str(i) + ',' + str(w) + ']')
		f1.write('/%x[' + str(i + 1) + ',' + str(w) + ']')
		f1.write('\n')
		num = num + 1
	f1.write('\n')
	for i in range(-2, 1):
		f1.write('U' + str(num) + ':%x[' + str(i) + ',' + str(t) + ']')
		f1.write('/%x[' + str(i + 1) + ',' + str(t) + ']')
		f1.write('\n')
		num = num + 1
	f1.write('\n')
	for i in range(-2, 1):
		f1.write('U' + str(num) + ':%x[' + str(i) + ',' + str(c) + ']')
		f1.write('/%x[' + str(i + 1) + ',' + str(c) + ']')
		f1.write('\n')
		num = num + 1
	f1.write('\n')
	for i in range(-2, 1):
		f1.write('U' + str(num) + ':%x[' + str(i) + ',' + str(l) + ']')
		f1.write('/%x[' + str(i + 1) + ',' + str(l) + ']')
		f1.write('\n')
		num = num + 1
	f1.write('\n')
	for i in range(-2, 1):
		f1.write('U' + str(num) + ':%x[' + str(i) + ',' + str(s) + ']')
		f1.write('/%x[' + str(i + 1) + ',' + str(l) + ']')
		f1.write('\n')
		num = num + 1
	f1.write('\n')

	for i in range(-1, 2):
		f1.write('U' + str(num) + ':%x[' + str(i - 1) + ',' + str(t) + ']')
		f1.write('/%x[' + str(i) + ',' + str(t) + ']')
		f1.write('/%x[' + str(i + 1) + ',' + str(t) + ']')
		f1.write('\n')
		num = num + 1
	f1.write('\n')
	for i in range(-1, 2):
		f1.write('U' + str(num) + ':%x[' + str(i - 1) + ',' + str(c) + ']')
		f1.write('/%x[' + str(i) + ',' + str(c) + ']')
		f1.write('/%x[' + str(i + 1) + ',' + str(c) + ']')
		f1.write('\n')
		num = num + 1
	f1.write('\n')
	for i in range(-1, 2):
		f1.write('U' + str(num) + ':%x[' + str(i - 1) + ',' + str(l) + ']')
		f1.write('/%x[' + str(i) + ',' + str(l) + ']')
		f1.write('/%x[' + str(i + 1) + ',' + str(l) + ']')
		f1.write('\n')
		num = num + 1
	f1.write('\n')
	for i in range(-1, 2):
		f1.write('U' + str(num) + ':%x[' + str(i - 1) + ',' + str(s) + ']')
		f1.write('/%x[' + str(i) + ',' + str(s) + ']')
		f1.write('/%x[' + str(i + 1) + ',' + str(s) + ']')
		f1.write('\n')
		num = num + 1
	f1.write('\n')

	f1.write('U' + str(num) + ':%x[' + str(0) + ',' + str(w) + ']')
	f1.write('/%x[' + str(0) + ',' + str(t) + ']')
	f1.write('\n')
	f1.write('U' + str(num) + ':%x[' + str(0) + ',' + str(t) + ']')
	f1.write('/%x[' + str(0) + ',' + str(c) + ']')
	f1.write('\n')
	f1.write('U' + str(num) + ':%x[' + str(0) + ',' + str(t) + ']')
	f1.write('/%x[' + str(0) + ',' + str(l) + ']')
	f1.write('\n')
	f1.write('U' + str(num) + ':%x[' + str(0) + ',' + str(t) + ']')
	f1.write('/%x[' + str(0) + ',' + str(s) + ']')
	f1.write('\n')
	f1.write('U' + str(num) + ':%x[' + str(0) + ',' + str(c) + ']')
	f1.write('/%x[' + str(0) + ',' + str(l) + ']')
	f1.write('\n')
	f1.write('U' + str(num) + ':%x[' + str(0) + ',' + str(c) + ']')
	f1.write('/%x[' + str(0) + ',' + str(s) + ']')
	f1.write('\n')
	f1.write('U' + str(num) + ':%x[' + str(0) + ',' + str(l) + ']')
	f1.write('/%x[' + str(0) + ',' + str(s) + ']')
	f1.write('\n')
	f1.write('\n')
	f1.write('# Bigram\n')
	f1.write('B')
	return

template2('F:\Comparative-factor-extraction-car\CRF++\\template1.txt',0,1)
template3('F:\Comparative-factor-extraction-car\CRF++\\template2.txt',0,1,2)
template3('F:\Comparative-factor-extraction-car\CRF++\\template3.txt',0,1,2)
template4('F:\Comparative-factor-extraction-car\CRF++\\template4.txt',0,1,2,3)
template3('F:\Comparative-factor-extraction-car\CRF++\\template5.txt',0,1,2)
template5('F:\Comparative-factor-extraction-car\CRF++\\template6.txt',0,1,2,3,4)
