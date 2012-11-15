# -*- coding: utf-8 -*-

from controller.base.Controller import Controller
import web
import model
import time

class JudgeResult(Controller):
	s_config = {
		'title':u'上传运行结果',
		'permission':'judge',
	}
	def process(self):
		i = web.input()
		
		s = web.config._session
		judgeResultModel = model.Model.Model('judge_result')
		jrid = judgeResultModel.insert( dict(
			sid = int(i['sid']),
			juid = int(s['uid']),
			result = i['result'],
			addtime = int( time.time() )
		) )
		
		self.setVariable('result','success')
		self.setVariable('jrid' , jrid )
		
	def permissionDenied(self):
		self.setVariable('result','permissionDenied')
