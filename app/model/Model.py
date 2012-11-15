import db.DbCreator
import hashlib

class Model(object):
	def __init__(self,sTableName):
		self.m_tableName = sTableName
		DbCreator = db.DbCreator.DbCreator()
		self.m_db = DbCreator.create()
	
	def insert(self,dictData):
		return self.m_db.insert(
			self.m_tableName,
			**dictData
		)
		
	def select(self,dictWhere=dict(),**other):
		listWhere = []
		dictVars = dict()
		for key in dictWhere:
			listWhere.append( '`'+key+'` = $'+key )
		if len(dictWhere) > 0:
			whereString = ' AND '.join(listWhere)
		else:
			whereString = None
		return self.m_db.select(
			self.m_tableName,
			dictWhere,
			where = whereString,
			**other
		)
		
	def update(self,where, vars=None, **values):
		return self.m_db.update( self.m_tableName,where,vars,**values )
		
	def str_md5(self,str):
		m = hashlib.md5()
		m.update(str)
		return m.hexdigest()
		
	def truncate(self):
		return self.m_db.query('truncate table %s'%self.m_tableName)
		
	def query(self, sql_query, vars=None):
		return self.m_db.query(sql_query,vars = vars)
