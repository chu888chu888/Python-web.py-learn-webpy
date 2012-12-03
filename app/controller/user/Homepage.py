# -*- coding: utf-8 -*-

from controller.base.FrameController import FrameController
import web
import model

class Homepage(FrameController):
	def process(self):
		i = web.input()
		
		uid = -1
		if i.has_key('uid') and i['uid'].isdigit():
			uid = int(i['uid'])
		else:
			self.Error(u'参数无效:缺少uid参数或uid参数不是整数')
			return
			
		aUserinfoModel = model.LinkedModel('userinfo')
		aIter = aUserinfoModel.alias('ui').where(dict(uid=uid)).limit(1).select()
		
		aUserinfo = None
		for i in aIter:
			aUserinfo = i
			self.setVariable('userinfo',i)
		
		if aUserinfo is None:
			self.Error(u'参数无效:没有与uid对应的用户')
			return
