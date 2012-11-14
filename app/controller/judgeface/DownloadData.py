# -*- coding: utf-8 -*-

from controller.base.Controller import Controller
import web
import os

class DownloadData(Controller):
	s_config = {
		'title':u'下载数据',
		'permission':'judge',
	}
	def run(self,renderObject):
		web.header('Content-Type','text/plain')
		if self.isPermit():
			i = web.input()
			if not i.has_key('pid') \
				or not i.has_key('dataid') \
				or not i.has_key('datatype'):
				yield web.notfound()
			
			pid = int(i['pid'])
			dataid = int(i['dataid'])
			datatype = i['datatype']
			
			dirpath = 'privatedata/rundata/%d/'%pid
			ft = 'rundata_%sdata_upload_%d.dat'
			filename = ft%(datatype,dataid)
			
			filepath = os.path.join(dirpath, filename)
			
			if not os.path.isfile(filepath):
				yield web.notfound()
			
			statinfo = os.stat(filepath)
			web.header('Content-Length',statinfo.st_size)
			
			f = open(filepath,'r')
			BUF_SIZE = 262144
			while True:
				c = f.read(BUF_SIZE)
				if c:
					yield c
				else:
					break
			f.close()
			
		else:
			yield web.Forbidden()
