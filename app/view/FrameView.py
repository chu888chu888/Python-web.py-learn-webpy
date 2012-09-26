import View

class FrameView(View.View):
	def __init__(self):
		super(FrameView,self).__init__()
		self.m_strFrameTplPath = ''
		
	def setFrameTplPath(self,strFrameTplPath):
		self.m_strFrameTplPath = strFrameTplPath
		
	def render(self,render):
		varDict = self.variableDict()
		
		r = render.frender(self.m_templatePath)
		body = r( varDict )
		
		varDict['body'] = body
		
		rf = render.frender(self.m_strFrameTplPath)
		return rf( varDict )
