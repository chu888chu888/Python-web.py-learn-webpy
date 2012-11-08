# -*- coding: utf-8 -*-

from controller.base.FrameController import FrameController
import web
import model

class Submit(FrameController):
	s_config = {
		'title':u'提交代码',
		'permission':'login',
	}
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
		
		self.setVariable('problemInfo',problemInfo)
		
		languageList = [
			'g++ 4.6.1 (Ubuntu/Linaro 4.6.1-9ubuntu3)',
			'gcc 4.6.1 (Ubuntu/Linaro 4.6.1-9ubuntu3)',
			'Python 2.7.2',
		]
		self.setVariable('language',languageList)
