import sys,os

import sae
import web

urls = (
    '/(.*)', 'Hello'
)

app_root = os.path.dirname(__file__)
templates_root = os.path.join(app_root, 'templates')
render = web.template.render(templates_root)

sys.path.append(app_root)

import controller.route

class Hello:
    def GET(self,path):
        aRoute = controller.route.route()
        return aRoute.GET(render,path)
        return render.hello()

app = web.application(urls, globals()).wsgifunc()

application = sae.create_wsgi_app(app)
