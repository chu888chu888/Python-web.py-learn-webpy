from controller.base.JsonController import JsonController

import web
import model
import time
import util.funs

class PostTopicResult(JsonController):
	def process(self):
		i = web.input()
		
		pnum = -1
		if i.has_key('pnum') and util.funs.isInt(i['pnum']):
			pnum = int(i['pnum'])
		
		title = ''
		if not i.has_key('title') or len(i['title']) == 0:
			self.Error(u'params error:title')
			return
		else:
			title = i['title']
		
		text = ''
		if not i.has_key('text') or len(i['text']) == 0:
			self.Error(u'params error:text')
			return
		else:
			text = i['text']
		
		uid = -1
		s = web.config._session
		if hasattr(s,'userinfo'):
			uid = s['userinfo']['uid']
		if uid < 0:
			self.permissionDenied('not login')
			return
		
		if pnum > 0 :
			aPnumModel = model.Model.Model('problem_num')
			aIter = aPnumModel.select(dict(pnum=pnum))
		
			pid = -1
			for i in aIter:
				pid = i['pid']
			if pid < 0:
				self.Error(u'params error:pnum:no such pnum')
				return
		else:
			pid = -1
		
		aDiscussModel = model.Model.Model('discuss_topic')
		aDiscussModel.insert(dict(
			pid = pid,
			uid = uid,
			ctime = int( time.time() ),
			rtime = int( time.time() ),
			title = title,
			text = text
		))
