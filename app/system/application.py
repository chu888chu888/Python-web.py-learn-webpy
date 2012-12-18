# -*- coding: utf-8 -*-

class Application(object):
	__singleton = None
	
	@classmethod
	def singleton(cls):
		return cls.__singleton
	
	@classmethod
	def setSingleton(cls,i):
		cls.__singleton = i
	
	def __init__(self,a):
		self.__webpyApplication = a
		
	def webapplication(self):
		return self.__webpyApplication
