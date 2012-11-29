from controller.base.AjaxController import AjaxController

import web
import model

class UserSetting(AjaxController):
	def process(self):
		i = web.input()
		
		condition = dict()
		if i.has_key('key'):
			condition['key'] = i['key']
			self.setVariable('key',i['key'])
		else:
			self.setVariable('result',False)
			self.setVariable('msg','param error')
			return
			
		s = web.config._session
		if hasattr(s,'uid'):
			condition['uid'] = s['uid']
			self.setVariable('uid',s['uid'])
		else:
			self.setVariable('result',False)
			self.setVariable('msg','unlogin user');
			return
			
		aUserSettingModel = model.Model.Model('user_setting')
		aIter = aUserSettingModel.select(condition)
		
		oldid = -1
		for a in aIter:
			oldid = a['id']
			self.setVariable('oldvalue',a['value'])
		
		if i.has_key('value'):
			if oldid > 0 :
				aUserSettingModel.update(
					'`id` = $id',
					dict(id=oldid),
					value=i['value']
				)
			else:
				aUserSettingModel.insert({
					'`key`': condition['key'],
					'`uid`': condition['uid'],
					'`value`': i['value']
				})
		
		aIter = aUserSettingModel.select(condition)
		for a in aIter:
			self.setVariable('newvalue',a['value'])
