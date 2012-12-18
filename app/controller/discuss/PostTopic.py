# -*- coding: utf-8 -*-

from controller.base.FrameController import FrameController
import web
import system.session

class PostTopic(FrameController):
	s_config = {
		'title':u'发表新主题',
	}
	def process(self):
		i = web.input()
		
		pnum = -1
		if i.has_key('pnum') and i['pnum'].isdigit():
			pnum = int(i['pnum'])
		
		self.setVariable('pnum',pnum)
		
		uid = -1
		s = system.session.Session.singleton()
		if hasattr(s,'userinfo'):
			uid = s['userinfo']['uid']
		if uid < 0:
			self.permissionDenied('请先登录',True)
			return
