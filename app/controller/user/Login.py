from controller.base.FrameController import FrameController

import web

class Login(FrameController):
	def process(self):
		i = web.input()
		
		if 'redirect' in i:
			redirect = i['redirect']
		else:
			redirect = '/'
		
		self.setVariable('redirect',redirect)
		self.setVariable('redirect_quote',web.urlquote( redirect ) )
