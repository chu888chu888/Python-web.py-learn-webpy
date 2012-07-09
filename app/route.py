import web,os

app_root = os.path.dirname(__file__)
templates_root = os.path.join(app_root, 'template')
render = web.template.render(templates_root)

class route:
    def GET(self,path):
        print "path is %s ;"%path
        c = 'controller.' + path.replace('/','.');
        print "c = %s ;" % c
        mod = __import__(c)
        print mod
        return render.hello()
