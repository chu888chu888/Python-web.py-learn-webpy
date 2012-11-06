import web

if __name__ == "__main__":
	urls = (
		'/(.*)', 'app.route.route'
	)
	application = web.application(urls, globals())
	
	if not hasattr(web.config,'_session'):
		session = web.session.Session(
			application,
			web.session.DiskStore('privatedata/sessions'),
			{'count': 0}
		)
		web.config._session = session
	
	application.run()
