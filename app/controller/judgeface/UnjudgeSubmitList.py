# -*- coding: utf-8 -*-

from controller.base.Controller import Controller
import model

class UnjudgeSubmitList(Controller):
	def process(self):
		aSubmitModel = model.Model.Model('submit')
		aIter = aSubmitModel.select(
			dict(judgeResultId=-1)
		)
		
		self.setVariable('aIter',aIter)
