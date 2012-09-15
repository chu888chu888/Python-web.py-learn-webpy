from controller.base.Controller import Controller

class Index(Controller):
	def __init__(self):
		Controller.__init__(self)
		self.m_templatePath = 'Index'
