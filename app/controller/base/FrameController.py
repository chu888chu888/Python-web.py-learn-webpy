# -*- coding: utf-8 -*-

import Controller
import view.View

class FrameController(Controller.Controller):
	def __init__(self):
		super(FrameController,self).__init__()
		
		self.setVariable('path',self.m_path)
		self.setVariable('title',u'无标题')
		
		aBodyView = view.View.View()
		aBodyView.setTemplatePath(self.m_path.replace('.','/'))
		self.setView(aBodyView)
		
		aPageView = view.View.View()
		aPageView.setTemplatePath('frame/frontpage')
		aPageView.addSubView('body',aBodyView)
		
		aFrameView = view.View.View()
		aFrameView.setTemplatePath('frame/frame')
		aFrameView.addSubView('body',aPageView)
		
		self.setVariable('styles',list())
