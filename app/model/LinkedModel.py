import db.DbCreator
import hashlib

class LinkedModel(object):
	def __init__(self,sTableName):
		self.__tableName = sTableName
		self.__db =db.DbCreator.DbCreator.instance()
		
		# linked data
		self.__clearLinkedData()
		
	def alias(self,a):
		self.__setLinkedData('alias',a)
		return self
		
	def where(self,w):
		if isinstance(w,basestring):
			self.__appendLinkedData('where',w)
		elif isinstance(w,dict):
			for i in w:
				v = w[i]
				if isinstance(v,int):
					self.__appendLinkedData('where','%s = %d'%(i,v))
				else:
					self.__appendLinkedData('where','%s = "%s"'%(i,v))
		return self
		
	def order(self,w):
		self.__appendLinkedData('order',w)
		return self
		
	def limit(self,length,offset=0):
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
		fieldString = self.__buildFieldString()
		tableString = self.__buildTableString()
		joinString = self.__buildJoinString()
		whereString = self.__buildWhereString()
		orderString = self.__buildOrderString()
		limitString = self.__buildLimitString()
			
		queryString = "select \n%s \nfrom %s \n%s \nwhere %s \n%s \n%s"%(
			fieldString,
			tableString,
			joinString,
			whereString,
			orderString,
			limitString
		)
		
		self.__clearLinkedData()
		return self.__db.query(queryString)
		
	def count(self):
		tableString = self.__buildTableString()
		joinString = self.__buildJoinString()
		whereString = self.__buildWhereString()
		
		queryString = "select count(*) from %s \n%s \nwhere %s"%(
			tableString,
			joinString,
			whereString
		)
		
		self.__clearLinkedData()
		aIter = self.__db.query(queryString)
		return aIter[0]['count(*)']
		
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
		
	def __clearLinkedData(self):
		self.__linkedData = dict()
		
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
		
	def __buildFieldString(self):
		# table and column
		tableNameList = self.__getTableNameList()
		columnNameListMap = dict()
		for tableName in tableNameList:
			columnNameListMap[ tableName ] = self.__getColumnList(tableName)
			
		# table alias
		tableAliasMap = self.__getTableAliasMap()
		
		# fieldString
		fieldStringPartedList = list()
		for tableName,columnNameList in columnNameListMap.iteritems():
			for columnName in columnNameList:
				tableAlias = tableAliasMap[ tableName ]
				columnAlias = columnName
				fieldStringParted = '`%s`.`%s` as `%s.%s`'%(
					tableAlias,
					columnName,
					tableAlias,
					columnAlias
				)
				
				fieldStringPartedList.append( fieldStringParted )
				
		fieldString = ",\n".join(fieldStringPartedList)
		return fieldString
		
	def __buildTableString(self):
		aliasData = self.__getLinkedData('alias')
		if aliasData:
			tableString = '`%s` as %s'%(self.__tableName,aliasData)
		else:
			tableString = '`%s`'%(self.__tableName)
		
		return tableString
		
	def __buildJoinString(self):
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
		return joinString
		
	def __buildWhereString(self):
		whereData = self.__getLinkedData('where')
		if whereData:
			whereString = "(" + " ) AND \n (".join( whereData ) + ")"
		else:
			whereString = '1'
		return whereString
		
	def __buildOrderString(self):
		orderData = self.__getLinkedData('order')
		if orderData:
			orderString = "order by "+','.join( orderData )
		else:
			orderString = ''
		return orderString
		
	def __buildLimitString(self):
		limitData = self.__getLinkedData('limit')
		if limitData:
			limitString = 'limit %s,%s'%(limitData['offset'],limitData['length'])
		else:
			limitString = 'limit 30'
		return limitString