from controller.base.Controller import Controller

class NotFound(Controller):
	def process(self):
		self.view().setVariable('urlPath',self.m_urlPath)
