# -*- coding: utf-8 -*-

from controller.base.Controller import Controller
import web
import model
import time
import system.session

class JudgeResult(Controller):
	s_config = {
		'title':u'上传运行结果',
		'permission':'judge',
	}
	def process(self):
		i = web.input()
		
		s = system.session.Session.singleton()
		judgeResultModel = model.Model.Model('judge_result')
		jrid = judgeResultModel.insert( dict(
			sid = int(i['sid']),
			juid = int(s['uid']),
			result = i['result'],
			addtime = int( time.time() )
		) )
		
		aSubmitModel = model.Model.Model('submit')
		aSubmitModel.update(
			'id = $id',
			dict(id=int(i['sid'])),
			judgeResultId = jrid
		)
		
		self.setVariable('result','success')
		self.setVariable('jrid' , jrid )
		
	def permissionDenied(self):
		self.setVariable('result','permissionDenied')
