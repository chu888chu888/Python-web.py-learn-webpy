# -*- coding: utf-8 -*-

from controller.base.FrameController import FrameController
import web
import system.session

class Logout(FrameController):
	def process(self):
		s = system.session.Session.singleton()
		s.kill()
		
		i = web.input()
		# redirect
		if hasattr(i,'redirect'):
			self.setVariable('redirect',i.redirect)
		else:
			self.setVariable('redirect','/')
