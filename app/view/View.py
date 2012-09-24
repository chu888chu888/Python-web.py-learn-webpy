# -*- coding: utf-8 -*-

class View(object):
	def __init__(self,strPath):
		self.m_strPath = strPath
		self.m_templatePath = ''
		self.m_variableDict = dict()
		
		self.setTitle(u"未命名网页")
	
	def render(self,render):
		if self.m_templatePath:
			arrTemplatePath = self.m_templatePath.split('/')
		else:
			arrTemplatePath = self.m_strPath.split('.')
		c=render
		for i in arrTemplatePath:
			c = getattr(c,i)
		
		body = c( self.variableDict() )
		self.setVariable('body',body)
		return render.frame.frame(self.variableDict())
		
	def setVariable(self,key,value):
		self.m_variableDict[key] = value
		
	def variableDict(self):
		return self.m_variableDict
		
	def setTitle(self,strTitle):
		self.setVariable('title',strTitle)
