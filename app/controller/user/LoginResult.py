# coding=utf-8
from controller.base.FrameController import FrameController
import web
import model.user.UserLogin
import system.session

class LoginResult(FrameController):
	def process(self):
		i = web.input()
		
		# redirect
		if 'redirect' in i:
			redirect = i['redirect']
		else:
			redirect = '/'
		
		if 'loginname' in i:
			loginname = i['loginname']
		else:
			self.Error(u'参数无效:缺少loginname参数')
			return
		
		if 'password' in i:
			password = i['password']
		else:
			self.Error(u'参数无效:缺少password参数')
			return
		
		m = model.user.UserLogin.UserLogin()
		r = m.select({'loginname':loginname})
		
		loginResult = False
		uid = -1
		md5_password = m.str_md5(password)
		for it in r:
			if it['password'] == md5_password:
				loginResult = True
				uid = it['uid']
		
		# variable
		self.setVariable('loginResult',loginResult)
		
		# redirect
		if loginResult:
			self.setVariable('redirect',redirect)
		else:
			self.setVariable('redirect','/user/Login?redirect=%s'%web.urlquote(redirect))
		
		# header for client request
		if loginResult:
			web.header('Login-Result','success')
		else:
			web.header('Login-Result','fail')
		
		# session
		if loginResult:
			s = system.session.Session.singleton()
			s['uid'] = uid
			
			aPermissionModel = model.Model.Model('permission')
			permissionIter = aPermissionModel.select({'uid':uid})
			permissionList = []
			for p in permissionIter:
				permissionList.append( p['permission'] )
			permissionList.append('login')
			s['permissionList'] = permissionList
			
			aUserinfoModel = model.Model.Model('userinfo')
			for userinfo in aUserinfoModel.select({'uid':uid}) :
				s['userinfo'] = userinfo
