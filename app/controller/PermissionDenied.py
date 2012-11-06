# -*- coding: utf-8 -*-

from controller.base.FrameController import FrameController

class PermissionDenied(FrameController):
	s_config = {
		'title':u'权限拒绝',
	}
	def process(self):
		self.setVariable('urlPath',self.m_urlPath)
