from controller.base.FrameController import FrameController
import web
import time
import model
import re
import os

class AddProblemResult(FrameController):
	def process(self):
		i = web.input()
		
		pid = self.addProblem( i )
		self.addProblemData(pid,i)
		
	def addProblem(self, data ):
		insertData = dict()
		keyList = [
			'title',
			'time_limit',
			'memory_limit',
			'description',
			'input',
			'output',
			'sample_input',
			'sample_output',
			'hint',
			'source']
		for key in keyList:
			insertData[key] = str(data[key])
		
		insertData['addtime'] = int( time.time() )
		
		s = web.config._session
		if hasattr(s,'uid'):
			insertData['authorid'] = s['uid']
		else:
			insertData['authorid'] = -1
		
		problemModel = model.Model.Model('problem')
		pid = problemModel.insert( insertData )
		
		return pid
		
	def addProblemData(self,pid,data):
		defaultDataMap = dict()
		
		reg = re.compile('rundata_(out|in)data_upload_[0-9]+')
		for key in data:
			if reg.match( key ):
				defaultDataMap[ key ] = dict()
		
		data = web.input( ** defaultDataMap )
		
		dirpath = 'privatedata/rundata/%d/'%pid
		try:
			os.makedirs( dirpath )
		except:
			pass
		for key in data:
			if reg.match( key ):
				filepath = dirpath + key + '.dat'
				fout = open( filepath ,'w')
				fout.write( data[key].file.read() )
				fout.close()
