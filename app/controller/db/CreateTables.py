from controller.base.FrameController import FrameController
import db.DbCreator

class CreateTables(FrameController):
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
