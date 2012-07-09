import sys,os

import sae
import web

urls = (
    '/(.*)', 'app.route.route'
)

app_root = os.path.dirname(__file__)
sys.path.append(app_root)

import app.route

app = web.application(urls, globals()).wsgifunc()

application = sae.create_wsgi_app(app)
