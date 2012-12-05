# -*- coding: utf-8 -*-

from controller.base.FrameController import FrameController
import model
import web

class PostTopic(FrameController):
	s_config = {
		'title':u'发表新主题',
	}
	def process(self):
		i = web.input()
		
		pnum = -1
		if i.has_key('pnum') and i['pnum'].isdigit():
			pnum = int(i['pnum'])
		else:
			self.Error(u'参数无效:缺少pnum参数或pnum参数不是整数')
			return
		
		self.setVariable('pnum',pnum)
		
		uid = -1
		s = web.config._session
		if hasattr(s,'userinfo'):
			uid = s['userinfo']['uid']
		if uid < 0:
			self.permissionDenied('请先登录')
			return
