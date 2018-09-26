#!/usr/bin/python
# -*- coding :utf-8 -*-
import evaluateT1
import evaluateT2
import evaluateT3
import evaluateT4
import evaluateT5
import evaluateT6

def evaluateaAll(target):
	print('T1',end=' ')
	print(evaluateT1.evaluation(target))
	print('T2', end=' ')
	print(evaluateT2.evaluation(target))
	print('T3', end=' ')
	print(evaluateT3.evaluation(target))
	print('T4', end=' ')
	print(evaluateT4.evaluation(target))
	print('T5', end=' ')
	print(evaluateT5.evaluation(target))
	print('T6', end=' ')
	print(evaluateT6.evaluation(target))
	return evaluateaAll

evaluateaAll('SUB')
evaluateaAll('OBJ')
evaluateaAll('ATTR')
evaluateaAll('SENTI')
evaluateaAll('KW')


