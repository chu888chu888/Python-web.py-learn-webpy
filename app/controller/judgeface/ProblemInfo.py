# -*- coding: utf-8 -*-

from controller.base.Controller import Controller
import model
import web
import os

class ProblemInfo(Controller):
	s_config = {
		'title':u'题目信息',
		'permission':'judge',
	}
	def process(self):
		i = web.input()
		pid = int(i['pid'])
		
		aProblemModel = model.Model.Model('problem')
		aIter = aProblemModel.select(
			dict(pid=pid)
		)
		
		problemInfo = aIter[0]
		
		dirpath = 'privatedata/rundata/%d/'%pid
		
		filenames = []
		for dirname, dirnames, filenames in os.walk(dirpath):
			break
		
		ft = 'rundata_%sdata_upload_%d.dat'
		for i in range(1,100):
			if not ft%('in',i) in filenames or not ft%('out',i) in filenames:
				break
		
		problemInfo['dataCount'] = i-1
		
		self.setVariable('problemInfo',problemInfo)
		self.setVariable('result','success')
		
	def permissionDenied(self):
		self.setVariable('result','permissionDenied')
