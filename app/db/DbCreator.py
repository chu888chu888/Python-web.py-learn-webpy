import ConfigParser
import web
import os

class DbCreator(object):
	def create(self):
		if os.environ.has_key('SERVER_SOFTWARE'):
			return web.database(
				dbn="mysql",
				user=sae.const.MYSQL_USER,
				pw=sae.const.MYSQL_PASS,
				host=sae.const.MYSQL_HOST,
				port=sae.const.MYSQL_PORT
			)
		else:
			cf = ConfigParser.ConfigParser()
			cf.read("privatedata/setting.ini")
			return web.database(
				dbn="mysql",
				user=cf.get('db','username'),
				pw=cf.get('db','password'),
				db=cf.get('db','dbname')
			)
