# -*- coding: utf-8 -*-

from controller.base.FrameController import FrameController
import model
import time

class SubmitList(FrameController):
	s_config = {
		'title':u'提交列表',
	}
	def process(self):
		aSubmitModel = model.LinkedModel('submit')
		aSubmitIter = aSubmitModel \
			.alias('sm') \
			.join('userinfo','ui','ui.uid = sm.uid') \
			.join('problem','pr','sm.pid = pr.pid') \
			.join('problem_num','pn','pr.pid = pn.pid') \
			.join('judge_result','jr','jr.sid=sm.id and jr.id = sm.judgeResultId') \
			.order('`sm.addtime` DESC') \
			.select()
		
		self.setVariable('aSubmitIter',aSubmitIter)
		
	def ftime(self,t):
		return time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(t))
