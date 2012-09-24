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
		
		self.view().setVariable('path',self.m_path)
	def run(self,render):
		self.process()
		
		return self.view().render(render)
	
	def process(self):
		pass
	
	def view(self):
		if not hasattr(self,'m_view'):
			self.m_view = view.View.View(self.m_path)
		return self.m_view
	
	def setUrlPath(self,urlPath):
		self.m_urlPath = urlPath
