# -*- coding: utf-8 -*-

import PathInvalid
import view.View

class Controller(object):
	def __init__(self):
		prefix = 'app.controller.'
		modulePath = self.__module__
		if not modulePath.startswith(prefix):
			raise PathInvalid.PathInvalid(self.__module__)
		self.m_path = modulePath[ len(prefix) : ]
		
		self.m_renderType = 'frameview'
		
		self.m_view = None
		
		self.m_variableDict = dict()
		self.m_pplist = list()
		
	def buildView(self):
		aView = view.View.View()
		aView.setTemplatePath(self.m_path.replace('.','/'))
		self.setView(aView)
		
	def run(self,renderObject):
		self.process()
		
		for strPpName in self.m_pplist:
			func = getattr(self,'pp'+strPpName.capitalize())
			func()
		
		return self.render(renderObject)
		
	def process(self):
		pass
		
	def render(self,renderObject):
		if 'frameview' == self.m_renderType or 'view' == self.m_renderType:
			if not self.view():
				self.buildView()
			if 'frameview' == self.m_renderType:
				return self.view().rootView().render(
					renderObject,
					self.m_variableDict
				)
			else:
				return self.view().render(
					renderObject,
					self.m_variableDict
				)
		else:
			return self.m_renderType
		
	def setView(self,aView):
		self.m_view = aView
		
	def view(self):
		return self.m_view
	
	def setUrlPath(self,urlPath):
		self.m_urlPath = urlPath
		
	def setVariable(self,key,value):
		self.m_variableDict[key] = value
		
	def addPostProcess(self,strPpName):
		self.m_pplist.append(strPpName)
