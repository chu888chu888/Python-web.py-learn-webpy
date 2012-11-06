# -*- coding: utf-8 -*-

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
			)ENGINE=MyISAM DEFAULT CHARSET=utf8");
		self.m_db.query("CREATE TABLE IF NOT EXISTS `problem` ( \
			`pid` int(10) NOT NULL AUTO_INCREMENT COMMENT '内部id,题号由时间排序得到', \
			`title` varchar(60) NOT NULL COMMENT '题目标题', \
			`addtime` int(11) NOT NULL COMMENT '添加时间，时间戳', \
			`time_limit` int(10) NOT NULL COMMENT '单位：ms' , \
			`memory_limit` int(10) NOT NULL COMMENT '单位：kb' ,\
			`description` TEXT NOT NULL ,\
			`input` TEXT NOT NULL,\
			`output` TEXT NOT NULL,\
			`sample_input` TEXT NOT NULL,\
			`sample_output` TEXT NOT NULL,\
			`hint` TEXT NOT NULL,\
			`source` varchar(100) NOT NULL,\
			`authorid` int(10) NOT NULL,\
			PRIMARY KEY (`pid`) \
			)ENGINE=MyISAM DEFAULT CHARSET=utf8");
		self.m_db.query("CREATE TABLE IF NOT EXISTS `problem_num`(\
			`pnum` int(10) NOT NULL COMMENT '题号',\
			`pid` int(10) NOT NULL COMMENT '题目真实id',\
			PRIMARY KEY (`pnum`) \
			)");
		self.m_db.query("CREATE TABLE IF NOT EXISTS `permission`(\
			`id` int(10) NOT NULL AUTO_INCREMENT,\
			`uid` int(10) NOT NULL COMMENT '用户id',\
			`permission` varchar(20) NOT NULL COMMENT '权限',\
			PRIMARY KEY (`id`) \
			)")
