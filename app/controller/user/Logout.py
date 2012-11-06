# -*- coding: utf-8 -*-

from controller.base.FrameController import FrameController
import web

class Logout(FrameController):
	def process(self):
		s = web.config._session
		if hasattr(s,'uid'):
			del s['uid']
		if hasattr(s,'permissionList'):
			del s['permissionList']
		
		i = web.input()
		# redirect
		if hasattr(i,'redirect'):
			self.setVariable('redirect',i.redirect)
		else:
			self.setVariable('redirect','/')
