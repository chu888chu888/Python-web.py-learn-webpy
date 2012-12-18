# -*- coding: utf-8 -*-

import web
import app.system.application

class Session(web.session.Session):
	__singleton = None
	
	@classmethod
	def singleton(cls):
		if cls.__singleton is None:
			application = app.system.application.Application.singleton()
			cls.__singleton = cls(
				application.webapplication(),
				web.session.DiskStore('privatedata/sessions'),
				{'count': 0}
			)
		return cls.__singleton
