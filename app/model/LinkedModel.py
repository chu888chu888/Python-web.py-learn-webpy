import db.DbCreator
import hashlib

class LinkedModel(object):
	def __init__(self,sTableName):
		self.__tableName = sTableName
		self.__db =db.DbCreator.DbCreator.instance()
		
		# linked data
		self.__linkedData = dict()
		
	def alias(self,a):
		self.__setLinkedData('alias',a)
		return self
		
	def where(self,w):
		self.__appendLinkedData('where',w)
		return self
		
	def order(self,w):
		self.__appendLinkedData('order',w)
		return self
		
	def limit(self,length,offset):
		self.__setLinkedData('limit',dict(length=length,offset=offset))
		return self
		
	def join(self,jointable,alias=None,on=None,jointype='left'):
		self.__appendLinkedData(
			'join',
			dict(
				jointable=jointable,
				alias=alias,
				on=on,
				jointype = jointype
			)
		)
		return self
		
	def select(self):
		# table and column
		tableNameList = self.__getTableNameList()
		columnNameListMap = dict()
		for tableName in tableNameList:
			columnNameListMap[ tableName ] = self.__getColumnList(tableName)
			
		print columnNameListMap
		# table alias
		tableAliasMap = self.__getTableAliasMap()
		
		# fieldString
		fieldStringPartedList = list()
		for tableName,columnNameList in columnNameListMap.iteritems():
			for columnName in columnNameList:
				tableAlias = tableAliasMap[ tableName ]
				columnAlias = columnName
				# fieldStringParted = ''
				# print fieldStringParted
				fieldStringParted = '`%s`.`%s` as `%s.%s`'%(
					tableAlias,
					columnName,
					tableAlias,
					columnAlias
				)
				
				fieldStringPartedList.append( fieldStringParted )
				
		fieldString = ",\n".join(fieldStringPartedList)
		
		# tableString
		tableString = self.__getTableString()
		
		# joinString
		joinStringPartedList = list()
		for join in self.__getLinkedData('join'):
			joinStringParted = '%s join `%s`'%(
				join['jointype'],
				join['jointable'],
			)
			if join['alias']:
				joinStringParted = joinStringParted + ' as %s'%join['alias']
			if join['on']:
				joinStringParted = joinStringParted + ' on (%s)'%join['on']
			joinStringPartedList.append( joinStringParted )
		joinString = " \n".join( joinStringPartedList )
		
		# whereString
		whereData = self.__getLinkedData('where')
		if whereData:
			whereString = "(" + " ) AND \n (".join( whereData ) + ")"
		else:
			whereString = '1'
		
		# orderString
		orderData = self.__getLinkedData('order')
		if orderData:
			orderString = "order by "+','.join( orderData )
		else:
			orderString = ''
		
		queryString = "select \n%s \nfrom %s \n%s \nwhere %s \n%s"%(
			fieldString,
			tableString,
			joinString,
			whereString,
			orderString
		)
		
		return self.__db.query(queryString)
		
	def __appendLinkedData(self,name,value):
		if not self.__linkedData.has_key(name):
			self.__linkedData[name] = list()
		
		self.__linkedData[name].append( value )
	
	def __setLinkedData(self,name,value):
		self.__linkedData[name] = value
		
	def __getLinkedData(self,name):
		if self.__linkedData.has_key( name ):
			return self.__linkedData[name]
		else:
			return None
		
	def __getTableNameList(self):
		tableNameList = list()
		tableNameList.append( self.__tableName )
		
		joinData = self.__getLinkedData('join')
		if joinData:
			for join in joinData:
				tableNameList.append( join['jointable'] )
			
		return tableNameList
	
	def __getColumnList(self,tableName):
		aIter = self.__db.query("SHOW COLUMNS FROM `%s`"%tableName)
		columnList = list()
		
		for i in aIter:
			columnList.append(i['Field'])
		
		return columnList
	
	def __getTableAliasMap(self):
		tableAliasMap = dict()
		aliasData = self.__getLinkedData('alias')
		if aliasData:
			tableAliasMap[ self.__tableName ] = aliasData
		else:
			tableAliasMap[ self.__tableName ] = self.__tableName
		
		joinData = self.__getLinkedData('join')
		if joinData:
			for join in joinData:
				if join['alias']:
					tableAliasMap[ join['jointable'] ] = join['alias']
				else:
					tableAliasMap[ join['jointable'] ] = join['jointable']
				
		return tableAliasMap
		
	def __getTableString(self):
		aliasData = self.__getLinkedData('alias')
		if aliasData:
			tableString = '`%s` as %s'%(self.__tableName,aliasData)
		else:
			tableString = '`%s`'%(self.__tableName)
		
		return tableString
