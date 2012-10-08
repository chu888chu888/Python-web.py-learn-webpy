import sae
import web
import pylibmc

urls = (
    '/(.*)', 'app.route.route'
)

app = web.application(urls, globals())

class MemStore(web.session.Store):
    def __init__(self, memcache):
        self.mc = memcache

    def __contains__(self, key):
        data = self.mc.get(key)
        return bool(data)

    def __getitem__(self, key):
        now = time.time()
        value = self.mc.get(key)
        if not value:
            raise KeyError
        else:
            value['attime'] = now
            self.mc.set(key,value)
            return value

    def __setitem__(self, key, value):
        now = time.time()
        value['attime'] = now
        s = self.mc.get(key)
        self.mc.set(key, value, web.config.session_parameters['timeout'])

    def __delitem__(self, key):
        self.mc.delete(key)

    def cleanup(self, timeout):
        pass

session = web.session.Session(
		app,
		MemStore(pylibmc.Client()),
		{'count': 0}
	)
web.config._session = session
application = sae.create_wsgi_app(app.wsgifunc())
