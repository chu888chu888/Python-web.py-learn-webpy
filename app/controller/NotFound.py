import controller.base.Controller

class NotFound(controller.base.Controller.Controller):
	def __init__(self):
		super(NotFound,self).__init__()
		self.m_templatePath = 'NotFound'
