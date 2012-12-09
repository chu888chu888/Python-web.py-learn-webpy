# -*- coding: utf-8 -*-

from controller.base.FrameController import FrameController
import model
import web
import util.funs

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
		
		aTopicModel = model.LinkedModel('discuss_topic')
		aTopicIter = aTopicModel \
			.alias('dt') \
			.join('problem_num','pn','dt.pid = pn.pid') \
			.join('userinfo','topic_ui','dt.uid = topic_ui.uid') \
			.join('discuss_reply','last_dr','last_dr.tid = dt.id AND last_dr.id = dt.last_rid') \
			.join('userinfo','last_dr_ui','last_dr.uid = last_dr_ui.uid') \
			.join('discuss_reply','count_dr','count_dr.tid = dt.id') \
			.where(where) \
			.group('dt.id') \
			.field('COUNT(count_dr.id)') \
			.reflectField(['dt','pn','topic_ui','last_dr','last_dr_ui']) \
			.order('CASE WHEN last_dr.id is NULL THEN dt.ctime ELSE last_dr.ctime END DESC') \
			.select()
		
		self.setVariable('iter',aTopicIter)
		
		self.setVariable('util',util)
