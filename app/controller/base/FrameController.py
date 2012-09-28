# -*- coding: utf-8 -*-

import Controller
import view.FrameView

class FrameController(Controller.Controller):
	def __init__(self):
		super(FrameController,self).__init__()
		
		aView = view.FrameView.FrameView()
		self.setView(aView)
		
		self.view().setVariable('path',self.m_path)
		self.view().setTemplatePath(self.m_path.replace('.','/'))
		self.view().setFrameTplPath('frame/frame')
		self.view().setTitle( u'无标题' )
