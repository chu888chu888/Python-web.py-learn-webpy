# -*- coding: utf-8 -*-

from controller.base.FrameController import FrameController
import web
import model
import time

class ProblemList(FrameController):
	s_config = {
		'title':u'题目列表',
	}
	def process(self):
		i = web.input()
		
		nPerPage = 20
		
		# current page
		nPage = 0
		if i.has_key('page'):
			nPage = int(i['page'])
		self.setVariable('currentPage',nPage)
		
		# problem list
		aProblemModel = model.LinkedModel('problem')
		aProblemIter = aProblemModel \
			.alias('pr') \
			.join('problem_num','pn','pn.pid = pr.pid') \
			.join('userinfo','ui','pr.authorid=ui.uid') \
			.select()
		self.setVariable('aProblemIter',aProblemIter)
		
		# problem count
		count = aProblemModel \
			.alias('pr') \
			.join('problem_num','pn','pn.pid = pr.pid') \
			.join('userinfo','ui','pr.authorid=ui.uid') \
			.count()
		
		# page count
		pageCount = ( count + nPerPage - 1 ) / nPerPage
		self.setVariable('pageCount',pageCount)
		
	def ftime(self,t):
		return time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(t))
