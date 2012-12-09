# -*- coding: utf-8 -*-

from controller.base.FrameController import FrameController
import web
import model
import time

class Detail(FrameController):
	def process(self):
		i = web.input()
		
		pnum = -1
		if i.has_key('pnum') and i['pnum'].isdigit():
			pnum = int(i['pnum'])
		else:
			self.Error(u'参数无效:缺少pnum参数或pnum参数不是整数')
			return
		
		aProblemModel = model.LinkedModel('problem')
		aProblemIter = aProblemModel \
			.alias('pr') \
			.join('problem_num','pn','pn.pid = pr.pid') \
			.join('userinfo','ui','pr.authorid = ui.uid') \
			.join('discuss_topic','dt','dt.pid = pr.pid') \
			.where({'pn.pnum':pnum}) \
			.group('dt.pid') \
			.field('count(dt.id) as `dt.count`') \
			.reflectField(['pr','pn','ui']) \
			.select()
		
		problemInfo = None
		for i in aProblemIter:
			problemInfo = i
		if problemInfo is None:
			self.Error(u'参数无效:没有与pnum对应的题目')
			return
		
		self.setConfig('title',u'%d -- %s'%(problemInfo['pn.pnum'],problemInfo['title']))
		
		self.setVariable('problemInfo',problemInfo)
