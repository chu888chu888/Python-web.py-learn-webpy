# -*- coding: utf-8 -*-

import Controller

class JsonController(Controller.Controller):
	def __init__(self):
		super(JsonController,self).__init__()
		self.m_renderType = 'json'
