import web

app_root = os.path.dirname(__file__)
templates_root = os.path.join(app_root, 'template')
render = web.template.render(templates_root)

class route:
    def GET(self,path):
        print "path is %s ;"%path
        return render.hello()
