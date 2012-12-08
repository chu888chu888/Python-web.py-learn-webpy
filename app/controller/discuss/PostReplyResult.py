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
		
		reply_to_id = -1
		if 'reply_to_id' in i and util.funs.isInt(i['reply_to_id']):
			reply_to_id = int(i['reply_to_id'])
		else:
			self.Error(u'params error:reply_to_id')
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
		reply_id = aReplyModel.insert(dict(
			tid = tid,
			uid = uid,
			reply_to_id = reply_to_id,
			ctime = int( time.time() ),
			text = text
		))
		
		aTopicModel = model.Model.Model('discuss_topic')
		aTopicModel.update(
			'id = $id',
			dict(id=tid),
			last_rid = reply_id
		)
