import web
import app.system.application as DanceApp

if __name__ == "__main__":
	urls = (
		'/(.*)', 'app.route.route'
	)
	application = web.application(urls, locals())
	
	if DanceApp.Application.singleton() is None:
		da = DanceApp.Application(application)
		DanceApp.Application.setSingleton(da)
	
	application.run()
