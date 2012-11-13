# -*- coding: utf-8 -*-

from controller.base.Controller import Controller
import model

class UnjudgeSubmitList(Controller):
	s_config = {
		'title':u'还没有结果的提交列表',
		'permission':'judge',
	}
	def process(self):
		aSubmitModel = model.Model.Model('submit')
		aIter = aSubmitModel.select(
			dict(judgeResultId=-1)
		)
		
		self.setVariable('aIter',aIter)
		
		self.setVariable('result','success')
		
	def permissionDenied(self):
		self.setVariable('result','permissionDenied')
