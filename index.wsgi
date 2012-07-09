import sae
import web

urls = (
    '/(.*)', 'app.route.route'
)

#import app.route

app = web.application(urls, globals()).wsgifunc()

application = sae.create_wsgi_app(app)
