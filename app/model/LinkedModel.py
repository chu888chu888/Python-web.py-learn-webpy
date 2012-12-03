import db.DbCreator
import hashlib

class LinkedModel(object):
	def __init__(self,sTableName):
		self.__tableName = sTableName
		self.__db =db.DbCreator.DbCreator.instance()
		
		# linked data
		self.__clearLinkedData()
		
	def field(self,column,table=None):
		self.__appendLinkedData('field',dict(
			column=column,
			table=table
		))
		return self
		
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
		
	def limit(self,length,offset=None):
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
		
	def group(self,g):
		self.__appendLinkedData('group',g)
		return self
		
	def select(self):
		fieldString = self.__buildFieldString()
		tableString = self.__buildTableString()
		joinString = self.__buildJoinString()
		whereString = self.__buildWhereString()
		orderString = self.__buildOrderString()
		limitString = self.__buildLimitString()
		groupString = self.__buildGroupString()
		
		queryString = "select\n%s\nfrom %s\n%s\nwhere %s\n%s\n%s\n%s"%(
			fieldString,
			tableString,
			joinString,
			whereString,
			groupString,
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
		fieldData = self.__getLinkedData('field')
		if fieldData:
			fieldStringPartedList = list()
			for f in fieldData:
				if f['table']:
					fieldStringParted = '`%s`.`%s` as `%s.%s`'%(
						f['table'],
						f['column'],
						f['table'],
						f['column']
					)
				else:
					fieldStringParted = f['column']
				fieldStringPartedList.append(fieldStringParted)
			fieldString = ',\n'.join(fieldStringPartedList)
		else:
			fieldString = self.__buildFieldStringByColumn()
		return fieldString
	
	def __buildFieldStringByColumn(self):
		# table and column
		tableNameList = self.__getTableNameList()
		columnNameListMap = dict()
		for tableName in tableNameList:
			columnNameListMap[ tableName ] = self.__getColumnList(tableName)
			
		# table alias
		tableAliasMap = self.__getTableAliasMap()
		
		# fieldString
		fieldStringPartedList = list()
		
		# this table
		for columnName in self.__getColumnList( self.__tableName ):
			fieldStringParted = '`%s`.`%s`'%(
				tableAliasMap[ self.__tableName ],
				columnName
			)
			
			fieldStringPartedList.append( fieldStringParted )
		
		# join table
		for tableName,columnNameList in columnNameListMap.iteritems():
			tableAlias = tableAliasMap[ tableName ]
			for columnName in columnNameList:
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
		joinData = self.__getLinkedData('join')
		if joinData:
			for join in joinData:
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
			if limitData['offset'] is None:
				limitString = 'limit %s'%limitData['length']
			else:
				limitString = 'limit %s,%s'%(limitData['offset'],limitData['length'])
		else:
			limitString = ''
		return limitString
		
	def __buildGroupString(self):
		groupData = self.__getLinkedData('group')
		if groupData:
			groupString = 'group by '+','.join( groupData )
		else:
			groupString = ''
		return groupString
