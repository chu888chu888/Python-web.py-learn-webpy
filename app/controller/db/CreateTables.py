from controller.base.WebPageController import WebPageController
import db.DbCreator

class CreateTables(WebPageController):
	def process(self):
		DbCreator = db.DbCreator.DbCreator()
		self.m_db = DbCreator.create()
		self.m_db.query("CREATE TABLE IF NOT EXISTS `logininfo` ( \
			`uid` int(10) NOT NULL AUTO_INCREMENT, \
			`loginname` varchar(60) NOT NULL, \
			`password` varchar(60) NOT NULL, \
			PRIMARY KEY (`uid`), \
			UNIQUE KEY `loginname` (`loginname`) \
			)");
		self.m_db.query("CREATE TABLE IF NOT EXISTS `userinfo` ( \
			`uid` int(10) NOT NULL, \
			`nickname` varchar(60) NOT NULL, \
			`email` varchar(60) NOT NULL, \
			`avatar` varchar(100) , \
			PRIMARY KEY (`uid`) \
			)");
