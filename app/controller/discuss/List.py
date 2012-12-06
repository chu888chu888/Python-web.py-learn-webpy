# -*- coding: utf-8 -*-

from controller.base.FrameController import FrameController
import model
import web

class List(FrameController):
	s_config = {
		'title':u'讨论区',
	}
	def process(self):
		i = web.input()
		
		pnum = -1
		where = dict()
		if i.has_key('pnum') and i['pnum'].isdigit():
			pnum = int(i['pnum'])
			where['pn.pnum'] = pnum
		
		self.setVariable('pnum',pnum)
		
		aDiscussModel = model.LinkedModel('discuss_topic')
		aIter = aDiscussModel \
			.alias('dt') \
			.join('userinfo','ui','dt.uid = ui.uid') \
			.join('problem_num','pn','dt.pid = pn.pid') \
			.where(where) \
			.select()
		
		self.setVariable('iter',aIter)
