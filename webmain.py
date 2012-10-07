import web

if __name__ == "__main__":
	web.config.debug = False
	urls = (
		'/(.*)', 'app.route.route'
	)
	application = web.application(urls, globals())
	
	session = web.session.Session(
		application,
		web.session.DiskStore('privatedata/sessions'),
		{'count': 0}
	)
	web.config._session = session
	
	application.run()
