# coding=utf-8
from controller.base.FrameController import FrameController
import web
import model.user.UserLogin

class LoginResult(FrameController):
	def process(self):
		i = web.input()
		
		m = model.user.UserLogin.UserLogin()
		r = m.select({'loginname':i.loginname,'password':m.str_md5(i.password)})
		
		l = r.list()
		
		if len(l) > 0:
			self.setVariable('msg','登录成功')
			self.setVariable('loginresult',True)
			s = web.config._session
			uid = l[0]['uid']
			s['uid'] = uid
			
			aPermissionModel = model.Model.Model('permission')
			permissionIter = aPermissionModel.select({'uid':uid})
			permissionList = []
			for p in permissionIter:
				permissionList.append( p['permission'] )
			s['permissionList'] = permissionList
			
			aUserinfoModel = model.Model.Model('userinfo')
			for userinfo in aUserinfoModel.select({'uid':uid}) :
				s['userinfo'] = userinfo
		else:
			self.setVariable('msg','登录失败')
			self.setVariable('loginresult',False)
		
		# redirect
		if hasattr(i,'redirect'):
			self.setVariable('redirect',i.redirect)
		else:
			self.setVariable('redirect','/')
