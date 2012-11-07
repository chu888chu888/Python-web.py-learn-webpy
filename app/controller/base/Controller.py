# -*- coding: utf-8 -*-

import PathInvalid
import view.View
import web

class Controller(object):
	s_config = {
	}
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
		
		self.setVariable('c',self)
		
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
		
	@classmethod
	def isPermit(cls):
		if cls.hasConfig('permission'):
			s = web.config._session
			if hasattr(s,'permissionList'):
				permissionList = s['permissionList']
				permission = cls.config('permission')
				if permission in permissionList:
					return True
				else:
					return False
			else:
				return False
		return True
		
	@classmethod
	def hasConfig(cls,key):
		return cls.s_config.has_key(key)
		
	@classmethod
	def config(cls,key,defaultValue=None):
		if cls.hasConfig(key):
			return cls.s_config[key]
		else:
			return defaultValue
		
	@classmethod
	def setConfig(cls,key,value):
		cls.s_config[key] = value
