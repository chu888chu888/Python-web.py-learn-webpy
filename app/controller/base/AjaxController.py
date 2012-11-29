# -*- coding: utf-8 -*-

import Controller
import json

class AjaxController(Controller.Controller):
	def render(self,renderObject):
		return json.dumps(self.m_variableDict)
