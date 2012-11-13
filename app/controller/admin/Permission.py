# -*- coding: utf-8 -*-

from controller.base.FrameController import FrameController
import model
import web

class Permission(FrameController):
	s_config = {
		'title':u'权限管理',
		'permission':'admin',
	}
	def process(self):
		inputData = web.input()
		aUserinfoModel = model.Model.Model('userinfo')
		
		if inputData.has_key('submit'):
			uid = int(inputData['uid'])
			permission = inputData['permission']
			
			success = True
			message = ''
			# 验证用户存在
			userinfoIter = aUserinfoModel.select(dict(uid=uid))
			try:
				userinfo=userinfoIter[0]
			except IndexError:
				userinfo=None
				success = False
				message = '用户不存在'
			
			self.setVariable('success',success)
			self.setVariable('message',message)
			
			if userinfo and permission:
				aPermissionModel = model.Model.Model('permission')
				aPermissionModel.insert(
					dict(
						uid = uid,
						permission = permission
					)
				)
			
				self.setVariable(
					'addPermission',
					dict(
						userinfo=userinfo,
						permission=permission
					)
				)
			
		aUserinfoIter = aUserinfoModel.select()
		
		self.setVariable('iter',aUserinfoIter)
