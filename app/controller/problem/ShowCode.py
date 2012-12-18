# -*- coding: utf-8 -*-

from controller.base.FrameController import FrameController
import model
import time
import web
import system.session

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
			self.setVariable('msg',u'参数无效:缺少sid参数或sid参数不是整数')
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
		
		aSubmitInfo = None
		for i in aSubmitIter:
			aSubmitInfo = i
			self.setVariable('aSubmitInfo',aSubmitInfo)
			
		if not aSubmitInfo:
			self.setVariable('msg',u'参数无效:没有与sid对应的内容')
			self.m_path = 'Error'
			return
			
		uid = -1
		s = system.session.Session.singleton()
		if hasattr(s,'userinfo'):
			uid = s['userinfo']['uid']
		if not self.checkPermitInSession('showAllCode') \
			and uid != aSubmitInfo['ui.uid']:
			self.permissionDenied('您无权查看此代码')
			return
