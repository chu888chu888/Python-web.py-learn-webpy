from controller.base.JsonController import JsonController

import web
import model
import time
import util.funs

class PostReplyResult(JsonController):
	def process(self):
		i = web.input()
		
		tid = -1
		if 'tid' in i and util.funs.isInt(i['tid']):
			tid = int(i['tid'])
		else:
			self.Error(u'params error:tid')
			return
		
		rid = -1
		if 'rid' in i and util.funs.isInt(i['rid']):
			rid = int(i['rid'])
		else:
			self.Error(u'params error:rid')
			return
		
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
		
		aReplyModel = model.Model.Model('discuss_reply')
		aReplyModel.insert(dict(
			tid = tid,
			uid = uid,
			rid = rid,
			ctime = int( time.time() ),
			text = text
		))
