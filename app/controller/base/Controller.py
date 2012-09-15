# coding=utf-8

class Controller:
	def __init__(self):
		self.m_variableDict = {}
		self.m_title = u"未命令网页"
		self.m_templatePath=''
	def run(self,render,path,arrPath):
		self.process()
		self.m_path = path
		self.setVariable('path',path)
		self.m_arrPath = arrPath
		self.setVariable('arrPath',arrPath);
		return self.render(render)
	
	def process(self):
		pass
	
	def render(self,render):
		if self.m_templatePath:
			arrTemplatePath = self.m_templatePath.split('/')
		else:
			arrTemplatePath = self.m_arrPath
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
