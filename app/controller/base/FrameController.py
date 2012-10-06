# -*- coding: utf-8 -*-

import Controller
import view.View

class FrameController(Controller.Controller):
	def __init__(self):
		super(FrameController,self).__init__()
		
		aBodyView = view.View.View()
		aBodyView.setVariable('path',self.m_path)
		aBodyView.setTemplatePath(self.m_path.replace('.','/'))
		self.setView(aBodyView)
		
		aFrameView = view.View.View()
		aFrameView.setTemplatePath('frame/frame')
		aFrameView.setVariable('title',u'无标题')
		aFrameView.addSubView('body',aBodyView)
