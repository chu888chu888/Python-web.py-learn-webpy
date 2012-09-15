# coding=utf-8
from controller.base.Controller import Controller
import web

class LoginResult(Controller):
	def process(self):
		i = web.input()
		print "form value:"
		print i
		if i['loginname'] == '111' and i['password'] == '222':
			self.setVariable('msg','登录成功')
		else:
			self.setVariable('msg','登录失败')
