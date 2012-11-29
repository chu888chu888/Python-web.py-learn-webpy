# -*- coding: utf-8 -*-

import Controller
import view.View
import view.Resource
import web
import model.Model

class WebPageController(Controller.Controller):
	s_config = {
		'title':u'无标题',
	}
	def __init__(self):
		super(WebPageController,self).__init__()
		
		self.setVariable('c',self)
		self.setVariable('res',view.Resource.Resource() )
		
		self.addPostProcess('readconfig')
	
	def buildView(self):
		aView = view.View.View()
		aView.setTemplatePath(self.m_path.replace('.','/'))
		self.setView(aView)
		
		aFrameView = view.View.View()
		aFrameView.setTemplatePath('frame/frame')
		aFrameView.addSubView('body',aView)
		
	def ppReadconfig(self):
		self.setVariable(
			'title',
			'%s - JDMD Online Judget'%self.config('title',u'无标题')
		)
