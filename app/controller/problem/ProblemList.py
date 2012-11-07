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
		aProblemModel = model.Model.Model('problem')
		aProblemIter = aProblemModel.query(
			'select * from problem_num as pn left join problem as pr on pn.pid = pr.pid LIMIT %s , %s'
			%(
				nPage * nPerPage,
				nPerPage
			)
		)
		self.setVariable('aProblemIter',aProblemIter)
		
		# problem count
		aProblemCount = aProblemModel.select(what='count(*)')
		count = 0
		for c in aProblemCount:
			count = c['count(*)']
		
		# page count
		pageCount = ( count + nPerPage - 1 ) / nPerPage
		self.setVariable('pageCount',pageCount)
		
	def ftime(self,t):
		return time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(t))
