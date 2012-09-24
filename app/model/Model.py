import db.DbCreator
import hashlib

class Model(object):
	def __init__(self,sTableName):
		self.m_tableName = sTableName
		DbCreator = db.DbCreator.DbCreator()
		self.m_db = DbCreator.create()
	
	def insert(self,dictData):
		self.m_db.insert(
			self.m_tableName,
			**dictData
		);
		
	def select(self,dictWhere):
		listWhere = []
		dictVars = dict()
		for key in dictWhere:
			listWhere.append( '`'+key+'` = $'+key )
		return self.m_db.select(
			self.m_tableName,
			dictWhere,
			where = ' AND '.join(listWhere)
		)
		
	def str_md5(self,str):
		m = hashlib.md5()
		m.update(str)
		return m.hexdigest()
