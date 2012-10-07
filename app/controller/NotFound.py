from controller.base.FrameController import FrameController

class NotFound(FrameController):
	def process(self):
		self.setVariable('urlPath',self.m_urlPath)
