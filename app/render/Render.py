import web

class Render(object):
	def frender(self,file_path):
		fp = 'app/template/'+file_path+'.html'
		return web.template.frender(fp)
