# -*- coding: utf-8 -*-

from controller.base.FrameController import FrameController
import web
import model
import time

class Detail(FrameController):
	def process(self):
		i = web.input()
		
		pnum = int(i['pnum'])
		
		aProblemModel = model.Model.Model('problem')
		aProblemIter = aProblemModel.query(
			'select * , u.nickname as author from problem_num as pn \
			left join problem as pr on pn.pid = pr.pid \
			left join userinfo as u on pr.authorid=u.uid \
			where pn.pnum=$pnum',
			dict(pnum=pnum)
		)
		problemInfo = aProblemIter[0]
		
		self.setConfig('title',u'%d -- %s'%(problemInfo['pnum'],problemInfo['title']))
		
		self.setVariable('problemInfo',problemInfo)
