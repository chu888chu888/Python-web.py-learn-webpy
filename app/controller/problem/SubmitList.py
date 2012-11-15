# -*- coding: utf-8 -*-

from controller.base.FrameController import FrameController
import model
import time

class SubmitList(FrameController):
	s_config = {
		'title':u'提交列表',
	}
	def process(self):
		aSubmitModel = model.Model.Model('submit')
		aSubmitIter = aSubmitModel.query(
			'''select * ,
				sm.addtime as `sm.addtime` ,
				sm.id as `sm.id` ,
				jr.id as `jr.id` ,
				jr.addtime as `jr.addtime`
				from submit sm
				left join userinfo ui on sm.uid = ui.uid
				left join problem pr on sm.pid = pr.pid
				left join problem_num pn on pr.pid = pn.pid
				left join judge_result jr on jr.sid = sm.id and jr.id = sm.judgeResultId
				order by sm.addtime DESC
			'''
		)
		
		self.setVariable('aSubmitIter',aSubmitIter)
		
	def ftime(self,t):
		return time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(t))
