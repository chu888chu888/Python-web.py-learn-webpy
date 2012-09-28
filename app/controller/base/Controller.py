# -*- coding: utf-8 -*-

import PathInvalid


class Controller(object):
	def __init__(self):
		prefix = 'app.controller.'
		modulePath = self.__module__
		if not modulePath.startswith(prefix):
			raise PathInvalid.PathInvalid(self.__module__)
		self.m_path = modulePath[ len(prefix) : ]
		
		self.m_view = None
		
	def run(self,renderObject):
		self.process()
		
		return self.view().render(renderObject)
	
	def process(self):
		pass
	
	def setView(self,aView):
		self.m_view = aView
		
	def view(self):
		return self.m_view
	
	def setUrlPath(self,urlPath):
		self.m_urlPath = urlPath
