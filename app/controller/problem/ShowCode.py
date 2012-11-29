# -*- coding: utf-8 -*-

from controller.base.FrameController import FrameController
import model
import time
import web

class ShowCode(FrameController):
	s_config = {
		'title':u'查看代码',
	}
	def process(self):
		condition = dict()
		i = web.input()
		
		if i.has_key('sid') and i['sid'].isdigit():
			condition['sm.id'] = int(i['sid'])
		else:
			self.setVariable('msg',u'参数无效')
			self.m_path = 'Error'
			return
		
		aSubmitModel = model.LinkedModel('submit')
		aSubmitIter = aSubmitModel \
			.alias('sm') \
			.join('userinfo','ui','ui.uid = sm.uid') \
			.join('problem','pr','sm.pid = pr.pid') \
			.join('problem_num','pn','pr.pid = pn.pid') \
			.join('judge_result','jr','jr.sid=sm.id and jr.id = sm.judgeResultId') \
			.where(condition) \
			.limit(length=1) \
			.select()
		
		self.setVariable('aSubmitInfo',aSubmitIter[0])
