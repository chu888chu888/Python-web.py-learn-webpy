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
		
		aDiscussModel = model.LinkedModel('discuss_topic')
		aIter = aDiscussModel \
			.alias('dt') \
			.join('userinfo','ui','dt.uid = ui.uid') \
			.join('problem_num','pn','dt.pid = pn.pid') \
			.join('discuss_reply','count_dr','count_dr.tid = dt.id') \
			.where(where) \
			.group('count_dr.tid') \
			.field('COUNT(count_dr.id)') \
			.reflectField(['discuss_topic','userinfo','problem_num','discuss_reply']) \
			.select()
		
		self.setVariable('iter',aIter)
		
		aRIter = aDiscussModel \
			.alias('dt') \
			.join('problem_num','pn','dt.pid = pn.pid') \
			.join('discuss_reply','last_dr','last_dr.tid = dt.id AND last_dr.id = dt.last_rid') \
			.join('userinfo','ui','last_dr.uid = ui.uid') \
			.where(where) \
			.select()
		
		self.setVariable('riter',aRIter)
		
		self.setVariable('util',util)
		
		self.setVariable('zip',zip)
