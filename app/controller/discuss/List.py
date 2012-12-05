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
		if i.has_key('pnum') and i['pnum'].isdigit():
			pnum = int(i['pnum'])
		else:
			self.Error(u'参数无效:缺少pnum参数或pnum参数不是整数')
			return
		
		self.setVariable('pnum',pnum)
		
		aDiscussModel = model.LinkedModel('discuss_topic')
		aIter = aDiscussModel \
			.alias('dt') \
			.join('userinfo','ui','dt.uid = ui.uid') \
			.select()
		
		self.setVariable('iter',aIter)
