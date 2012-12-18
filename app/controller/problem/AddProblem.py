# -*- coding: utf-8 -*-

from controller.base.FrameController import FrameController
import web
import system.session

class AddProblem(FrameController):
	s_config = {
		'title':u'添加题目',
	}
	def process(self):
		uid = -1
		s = system.session.Session.singleton()
		if hasattr(s,'userinfo'):
			uid = s['userinfo']['uid']
		if uid < 0:
			self.permissionDenied('请先登录',True)
			return
