# -*- coding: utf-8 -*-

class Resource(object):
	AUTO_PREFIX = 0
	ABS_PATH = 1
	STATIC_PATH = 2
	
	def __init__(self):
		self.__resList = list()
		
	def add(self,name,type='js',option=0):
		path = name
		if( self.AUTO_PREFIX == option ):
			path = '/static/%s/%s.%s'%(type,name,type)
		elif( self.ABS_PATH == option ):
			pass
		elif( self.STATIC_PATH == option ):
			path = '/static/%s.%s'%(name,type)
			
		self.__resList.append(dict(name=name,type=type,path=path))
		
	def __iter__(self):
		return iter(self.__resList)
