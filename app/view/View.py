# -*- coding: utf-8 -*-

class View(object):
	def __init__(self):
		self.m_templatePath = ''
		self.m_variableDict = dict()
		
	def render(self,render):
		r = render.frender(self.m_templatePath)
		return r(self.variableDict())
		
	def setTemplatePath(self,strTemplatePath):
		self.m_templatePath = strTemplatePath
		
	def setVariable(self,key,value):
		self.m_variableDict[key] = value
		
	def variableDict(self):
		return self.m_variableDict
		
	def setTitle(self,strTitle):
		self.setVariable('title',strTitle)
