# -*- coding: utf-8 -*-

import PathInvalid
import view.FrameView

class Controller(object):
	def __init__(self):
		prefix = 'app.controller.'
		modulePath = self.__module__
		if not modulePath.startswith(prefix):
			raise PathInvalid.PathInvalid(self.__module__)
		self.m_path = modulePath[ len(prefix) : ]
		
		aView = view.FrameView.FrameView()
		self.setView(aView)
		
		self.view().setVariable('path',self.m_path)
		self.view().setTemplatePath(self.m_path.replace('.','/'))
		self.view().setFrameTplPath('frame/frame')
		self.view().setTitle( u'无标题' )
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
