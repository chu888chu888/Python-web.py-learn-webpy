# -*- coding: utf-8 -*-

import view.Resource

class View(object):
	def __init__(self):
		self.m_templatePath = ''
		self.m_dictSubView = dict()
		self.m_parentView = None
		self.__resource = view.Resource.Resource()
		
		# a cache variable
		self.m_rootView = None
		
	def render(self,render,varDict):
		subViewRenderResult = dict()
		for name in self.m_dictSubView:
			aSubView = self.m_dictSubView[name]
			subViewRenderResult[name] = aSubView.render(render,varDict)
		
		r = render.frender(self.m_templatePath)
		
		varDict['temp'] = dict()
		for name in subViewRenderResult:
			varDict['temp'][name] = subViewRenderResult[name]
		
		varDict['res'] = self.__resource
		varDict['v'] = self
		ret = r( varDict )
		del(varDict['temp'])
		
		return ret
		
	def setTemplatePath(self,strTemplatePath):
		self.m_templatePath = strTemplatePath
		
	def addSubView(self,strName,aView):
		self.m_dictSubView[strName] = aView
		aView.setParentView(self)
		
	def subView(self,strName):
		return self.m_dictSubView[strName]
		
	def setParentView(self,aView):
		self.m_parentView = aView
		
		# clean cache variable when parent view change
		self.m_rootView = None
		
	def parentView(self):
		return self.m_parentView
		
	def rootView(self):
		if self.m_rootView :
			return self.m_rootView
		else:
			if self.m_parentView:
				self.m_rootView = self.m_parentView.rootView()
				return self.m_rootView
			else:
				return self
		
	def resourceIterator(self):
		for i in self.__resource:
			yield i
		for name in self.m_dictSubView:
			aSubView = self.m_dictSubView[name]
			for i in aSubView.resourceIterator():
				yield i
