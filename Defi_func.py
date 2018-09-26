#!/usr/bin/python
# -*- coding :utf-8 -*-
import re
import numpy as np
import Defi_class

#读取比较词候选
#存入keywords列表
def readkeywords():
	f1 = open('..\data\比较词候选.txt', 'r')
	list_stan = []
	for line1 in f1.readlines():
		if line1 == '\n':
			break
		else:
			list_stan.append(line1)
	list_stan = np.array(list_stan)
	return list_stan

