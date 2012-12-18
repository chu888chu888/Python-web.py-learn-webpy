# -*- coding: utf-8 -*-

from controller.base.FrameController import FrameController
import web
import model
import time
import setting.Setting
import system.session

class SubmitResult(FrameController):
	s_config = {
		'title':u'提交结果',
		'permission':'login',
	}
	def process(self):
		success=True
		message=''
		while True:
			i = web.input()
			
			# code length exam
			aSetting = setting.Setting.Setting()
			code_maxlength = int(aSetting.value('problem/submit/code/maxlength',65535))
			if len(i['code']) > code_maxlength:
				success = False
				message = '代码长度不得超过%d'%code_maxlength
				break
			
			s = system.session.Session.singleton()
			
			data=dict(
				pid=int(i['pid']),
				uid=s['uid'],
				judgeResultId=-1,
				addtime=int( time.time() ),
				language=i['language'],
				code=i['code'],
			)
			
			aSubmitModel = model.Model.Model('submit')
			aSubmitModel.insert(data)
			break
		
		self.setVariable('success',success)
		self.setVariable('message',message)
