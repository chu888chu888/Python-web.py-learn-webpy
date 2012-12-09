# -*- coding: utf-8 -*-

from controller.base.FrameController import FrameController
import web
import model
import os
import hashlib

class EditUserInfo(FrameController):
	s_config = {
		'title':u'修改个人资料',
	}
	def process(self):
		uid = -1
		s = web.config._session
		if 'userinfo' in s:
			uid = s['userinfo']['uid']
		if uid < 0:
			self.permissionDenied('请先登录')
			return
		
		i = web.input(avatar={})
		
		if 'submit' in i:
			data = dict()
			avatarfile = i['avatar']
			if avatarfile.filename:
				data['avatar'] = self.saveAvatar(avatarfile)
			data['nickname'] = i['nickname']
			
			aUserinfoModel = model.Model.Model('userinfo')
			aUserinfoModel.update(
				'uid = $uid',
				dict(uid=uid),
				**data
			)
			self.setVariable('msg',u'修改成功')
		
		aUserinfoModel = model.LinkedModel('userinfo')
		aIter = aUserinfoModel.where(dict(uid=uid)).limit(1).select()
		
		for i in aIter:
			self.setVariable('userinfo',i)
		
	def saveAvatar(self,avatarfile):
		sufix = os.path.splitext(avatarfile.filename)[1][1:]
		
		m = hashlib.md5()
		m.update(avatarfile.file.read())
		saveFileName = m.hexdigest()
		
		dirpath = 'static/userupload/'
		
		if not os.path.isdir(dirpath):
			os.makedirs(dirpath)
		
		filepath = '%s%s.%s'%(dirpath,saveFileName,sufix)
		fout = open( filepath ,'w')
		avatarfile.file.seek(0)
		fout.write( avatarfile.file.read() )
		fout.close()
		
		return '/'+filepath
