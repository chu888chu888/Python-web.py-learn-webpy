from controller.base.Controller import Controller
import web

class SetupDb(Controller):
	def process(self):
		i = web.input()
		if i:
			self.setVariable('result',self.setupdb(i))
		else:
			print "no input"
	
	def setupdb(self,i):
		db = web.database(dbn="mysql",user='root',pw=i.rootPassword)
		print db
		db.query("create database %s"%i.dbname)
		db.query("grant all privileges on %s.* to %s@localhost identified by '%s'"%(i.dbname,i.dbUserName,i.dbUserPassword))
		return True
