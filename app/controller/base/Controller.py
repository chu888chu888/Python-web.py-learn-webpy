# -*- coding: utf-8 -*-

import PathInvalid

class Controller(object):
	def __init__(self):
		self.m_variableDict = {}
		self.m_title = u"未命令网页"
		self.m_templatePath = ''
		
		prefix = 'app.controller.'
		modulePath = self.__module__
		if not modulePath.startswith(prefix):
			raise PathInvalid.PathInvalid(self.__module__)
		self.m_path = modulePath[ len(prefix) : ]
		
		self.setVariable('path',self.m_path)
		
	def run(self,render):
		self.process()
		
		return self.render(render)
	
	def process(self):
		pass
	
	def render(self,render):
		if self.m_templatePath:
			arrTemplatePath = self.m_templatePath.split('/')
		else:
			arrTemplatePath = self.m_path.split('.')
		c=render
		for i in arrTemplatePath:
			c = getattr(c,i)
		
		body = c( self.variableDict() )
		return render.frame.frame(body,self )
		
	def setVariable(self,key,value):
		self.m_variableDict[key] = value
	def variableDict(self):
		return self.m_variableDict
	
	def title(self):
		return self.m_title
