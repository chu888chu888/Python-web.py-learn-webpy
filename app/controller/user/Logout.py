# -*- coding: utf-8 -*-

from controller.base.FrameController import FrameController
import web

class Logout(FrameController):
	def process(self):
		s = web.config._session
		s.kill()
		
		i = web.input()
		# redirect
		if hasattr(i,'redirect'):
			self.setVariable('redirect',i.redirect)
		else:
			self.setVariable('redirect','/')
