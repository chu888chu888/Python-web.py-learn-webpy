import ConfigParser

class Setting(object):
	__instance=None
	
	@classmethod
	def instance(cls):
		if cls.__instance == None:
			cls.__instance = cls()
		return cls.__instance
		
	def __init__(self):
		self.__cf = ConfigParser.ConfigParser()
		self.__cf.read("privatedata/setting.ini")
		
	def value(self,key,defaultValue=None):
		section,option = self.__parseKey(key)
		if self.__cf.has_option(section,option):
			return self.__cf.get(section,option)
		else:
			return defaultValue
		
	def hasValue(self,key):
		section,option = self.__parseKey(key)
		return self.__cf.has_option(section,option)
		
	def __parseKey(self,key):
		section = key[0:key.rfind('/')]
		option = key[key.rfind('/')+1:]
		return (section,option)
