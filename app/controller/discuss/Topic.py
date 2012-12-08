# -*- coding: utf-8 -*-

from controller.base.FrameController import FrameController
import model
import web
import util.funs

class Topic(FrameController):
	s_config = {
		'title':u'查看主题',
	}
	def process(self):
		i = web.input()
		tid = -1
		
		where = dict()
		if 'id' in i and util.funs.isInt(i['id']):
			tid = int(i['id'])
			where['dt.id'] = tid
		else:
			self.Error(u'参数无效:缺少id参数或id参数不是整数')
			return
		
		aDiscussModel = model.LinkedModel('discuss_topic')
		aIter = aDiscussModel \
			.alias('dt') \
			.join('userinfo','ui','dt.uid = ui.uid') \
			.join('problem_num','pn','dt.pid = pn.pid') \
			.where(where) \
			.select() \
		
		aTopicInfo = None
		for i in aIter:
			aTopicInfo = i
		
		if aTopicInfo is None:
			self.Error(u'参数无效:没有与id对应的主题')
			return
		
		self.setVariable('topicInfo',aTopicInfo)
		
		aReplyModel = model.LinkedModel('discuss_reply')
		aReplyIter = aReplyModel \
			.alias('dr') \
			.join('userinfo','ui','dr.uid = ui.uid') \
			.where({'dr.tid':tid}) \
			.select()
		
		self.setVariable('aReplyIter',aReplyIter)
		
		self.setVariable('util',util)
