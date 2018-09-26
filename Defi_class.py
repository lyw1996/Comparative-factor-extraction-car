#!/usr/bin/python
# -*- coding :utf-8 -*-
class Feature:
	def __init__(self,index, word, pos, chunk, keyword, position, result):
		self.index=index
		self.word = word
		self.pos = pos
		self.chunk = chunk
		self.keyword = keyword
		self.position = position
		self.result = result

class Standard:
	def __init__(self,index,sub,obj,attr,senti,kw):
		self.index=index
		self.sub=sub
		self.obj=obj
		self.attr=attr
		self.senti=senti
		self.kw=kw


class raw_sentence:
	def __init__(self,index,sentence):
		self.index=index
		self.sentence=sentence

class Evaluation:
	def __init__(self,index, word, pos, chunk, keyword, position, result1,result2):
		self.index = index
		self.word = word
		self.pos = pos
		self.chunk = chunk
		self.keyword = keyword
		self.position = position
		self.result1 = result1
		self.result2=result2


class pos_result:
	def __init__(self,index,word,pos):
		self.index=index
		self.word=word
		self.pos=pos

class target:
	def __init__(self, index, word,target):
		self.index=index
		self.word=word
		self.target=target
