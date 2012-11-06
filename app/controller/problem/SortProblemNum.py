# -*- coding: utf-8 -*-

from controller.base.FrameController import FrameController
import model
import time

class SortProblemNum(FrameController):
	config = {
		'title':u'重新安排题号',
	}
	def process(self):
		# 清空 problem_num
		aProblemNumModel = model.Model.Model('problem_num')
		aProblemNumModel.truncate()
		
		# 所有problem
		aProblemModel = model.Model.Model('problem')
		aProblemIter = aProblemModel.select(order='`addtime`')
		aProblemList = []
		
		# 安排题号
		nProblemNum = 1000
		for i in aProblemIter:
			print i['pid']
			print i['title']
			print i['addtime']
			aProblemList.append({
				'pid':i['pid'],
				'title':i['title'],
				'addtime':time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(i['addtime']))
			})
			aProblemNumModel.insert({
				'pnum':nProblemNum,
				'pid':i['pid']
			})
			nProblemNum = nProblemNum + 1
		
		self.setVariable('aProblemIter',aProblemList)
		
		# 题号列表
		aProblemNumIter = aProblemNumModel.select(order='`pnum`')
		self.setVariable('aProblemNumIter',aProblemNumIter)
