# -*- coding: utf-8 -*-

import Controller
import view.View
import web
import model.Model

class WebPageController(Controller.Controller):
	def __init__(self):
		super(WebPageController,self).__init__()
		
		self.setVariable('styles',list())
		self.setVariable('js',list())
		self.setVariable('title',u'无标题')
	
	def buildView(self):
		aView = view.View.View()
		aView.setTemplatePath(self.m_path.replace('.','/'))
		self.setView(aView)
		
		aFrameView = view.View.View()
		aFrameView.setTemplatePath('frame/frame')
		aFrameView.addSubView('body',aView)
