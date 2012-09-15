import web

urls = (
    '/(.*)', 'app.route.route'
)

if __name__ == "__main__":
	app = web.application(urls, globals())
	app.run()
