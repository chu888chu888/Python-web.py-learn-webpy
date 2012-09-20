from controller.base.Controller import Controller

import web

class SetupDb(Controller):
	def process(self):
		i = web.input()
		if i:
			self.setVariable('result',self.setupdb(i))
		else:
			print "no input"
	
	def setupdb(self,i):
		return True
