# -*- coding: utf-8 -*-

from controller.base.FrameController import FrameController
import model
import time
import web

class SubmitList(FrameController):
	s_config = {
		'title':u'提交列表',
	}
	def process(self):
		condition = dict()
		i = web.input()
		formvalue = dict()
		
		if i.has_key('uid') and i['uid'].isdigit():
			condition['ui.uid'] = int(i['uid'])
			formvalue['uid'] = i['uid']
		else:
			formvalue['uid'] = None
		
		if i.has_key('pnum') and i['pnum'].isdigit():
			condition['pn.pnum'] = int(i['pnum'])
			formvalue['pnum'] = i['pnum']
		else:
			formvalue['pnum'] = None
		
		if i.has_key('result') and i['result']:
			condition['jr.result'] = i['result']
			formvalue['result'] = i['result']
		else:
			formvalue['result'] = None
			
		self.setVariable('formvalue',formvalue)
		
		if i.has_key('page') and i['page'].isdigit():
			current_page = int(i['page'])
		else:
			current_page = 0
		num_per_page = 4
		page_link_width = 5
		
		aSubmitModel = model.LinkedModel('submit')
		aSubmitIter = aSubmitModel \
			.alias('sm') \
			.join('userinfo','ui','ui.uid = sm.uid') \
			.join('problem','pr','sm.pid = pr.pid') \
			.join('problem_num','pn','pr.pid = pn.pid') \
			.join('judge_result','jr','jr.sid=sm.id and jr.id = sm.judgeResultId') \
			.order('`sm.addtime` DESC') \
			.where(condition) \
			.limit(length=num_per_page,offset=current_page*num_per_page) \
			.select()
		
		self.setVariable('aSubmitIter',aSubmitIter)
		
		total_count = aSubmitModel \
			.alias('sm') \
			.join('userinfo','ui','ui.uid = sm.uid') \
			.join('problem','pr','sm.pid = pr.pid') \
			.join('problem_num','pn','pr.pid = pn.pid') \
			.join('judge_result','jr','jr.sid=sm.id and jr.id = sm.judgeResultId') \
			.where(condition) \
			.count()
			
		page_count = ( total_count + num_per_page -1 )/ num_per_page
		
		page_link_end = current_page + page_link_width /2 +1
		if page_link_end > page_count:
			page_link_end = page_count
		
		page_link_begin = page_link_end - page_link_width
		if page_link_begin < 0:
			page_link_end = page_link_end - page_link_begin
			page_link_begin = 0
		if page_link_end > page_count:
			page_link_end = page_count
		
		baseLink = ''
		for key in formvalue:
			if formvalue[key]:
				baseLink += '%s=%s&'%(key,formvalue[key])
		
		self.setVariable('pager',dict(
			current = current_page,
			count = page_count,
			begin = page_link_begin,
			end = page_link_end,
			link = baseLink
		))
		
	def ftime(self,t):
		return time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(t))
