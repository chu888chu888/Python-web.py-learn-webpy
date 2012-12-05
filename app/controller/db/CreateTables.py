# -*- coding: utf-8 -*-

from controller.base.WebPageController import WebPageController
import db.DbCreator

class CreateTables(WebPageController):
	def process(self):
		DbCreator = db.DbCreator.DbCreator()
		self.m_db = DbCreator.create()
		self.m_db.query('''CREATE TABLE IF NOT EXISTS `logininfo` (
			`uid` int(10) NOT NULL AUTO_INCREMENT,
			`loginname` varchar(60) NOT NULL,
			`password` varchar(60) NOT NULL,
			PRIMARY KEY (`uid`),
			UNIQUE KEY `loginname` (`loginname`)
			)''')
		self.m_db.query('''CREATE TABLE IF NOT EXISTS `userinfo` (
			`uid` int(10) NOT NULL,
			`nickname` varchar(60) NOT NULL,
			`email` varchar(60) NOT NULL,
			`avatar` varchar(100),
			PRIMARY KEY (`uid`)
			)ENGINE=MyISAM DEFAULT CHARSET=utf8''')
		self.m_db.query('''CREATE TABLE IF NOT EXISTS `problem` (
			`pid` int(10) NOT NULL AUTO_INCREMENT COMMENT '内部id,题号由时间排序得到',
			`title` varchar(60) NOT NULL COMMENT '题目标题',
			`addtime` int(11) NOT NULL COMMENT '添加时间，时间戳',
			`time_limit` int(10) NOT NULL COMMENT '单位：ms' ,
			`memory_limit` int(10) NOT NULL COMMENT '单位：kb' ,
			`description` TEXT NOT NULL ,
			`input` TEXT NOT NULL,
			`output` TEXT NOT NULL,
			`sample_input` TEXT NOT NULL,
			`sample_output` TEXT NOT NULL,
			`hint` TEXT NOT NULL,
			`source` varchar(100) NOT NULL,
			`authorid` int(10) NOT NULL,
			PRIMARY KEY (`pid`)
			)ENGINE=MyISAM DEFAULT CHARSET=utf8''')
		self.m_db.query('''CREATE TABLE IF NOT EXISTS `problem_num`(
			`pnum` int(10) NOT NULL COMMENT '题号',
			`pid` int(10) NOT NULL COMMENT '题目真实id',
			PRIMARY KEY (`pnum`)
			)''')
		self.m_db.query('''CREATE TABLE IF NOT EXISTS `permission`(
			`id` int(10) NOT NULL AUTO_INCREMENT,
			`uid` int(10) NOT NULL COMMENT '用户id',
			`permission` varchar(20) NOT NULL COMMENT '权限',
			PRIMARY KEY (`id`)
			)''')
		self.m_db.query('''CREATE TABLE IF NOT EXISTS `submit`(
			`id` int(10) NOT NULL AUTO_INCREMENT,
			`pid` int(10) NOT NULL COMMENT '题目id',
			`uid` int(10) NOT NULL COMMENT '用户id',
			`judgeResultId` int(10) NOT NULL COMMENT '结果id，默认为-1',
			`addtime` int(11) NOT NULL COMMENT '添加时间，时间戳',
			`language` varchar(30) NOT NULL COMMENT '语言',
			`code` TEXT NOT NULL,
			PRIMARY KEY (`id`)
			)ENGINE=MyISAM DEFAULT CHARSET=utf8''')
		self.m_db.query('''CREATE TABLE IF NOT EXISTS `judge_result`(
			`id` int(10) NOT NULL AUTO_INCREMENT,
			`sid` int(10) NOT NULL COMMENT 'submit id',
			`juid` int(10) NOT NULL COMMENT 'judge 用户 id',
			`result` varchar(20) NOT NULL,
			`addtime` int(11) NOT NULL COMMENT '添加时间，时间戳',
			PRIMARY KEY (`id`)
			)ENGINE=MyISAM DEFAULT CHARSET=utf8''')
		self.m_db.query('''CREATE TABLE IF NOT EXISTS `user_setting`(
			`id` int(10) NOT NULL AUTO_INCREMENT,
			`key` varchar(100) NOT NULL,
			`uid` int(10) NOT NULL,
			`value` varchar(100) NOT NULL,
			PRIMARY KEY (`id`),
			INDEX uk ( `key`, `uid` )
			)ENGINE=MyISAM DEFAULT CHARSET=utf8''')
		self.m_db.query('''CREATE TABLE IF NOT EXISTS `discuss_topic`(
			`id` int(10) NOT NULL AUTO_INCREMENT,
			`pid` int(10) NOT NULL COMMENT '题目id',
			`uid` int(10) NOT NULL COMMENT '用户id',
			`ctime` int(11) NOT NULL COMMENT '创建时间',
			`mtime` int(11) NOT NULL COMMENT '修改时间',
			`rtime` int(11) NOT NULL COMMENT '最后回复时间',
			`rid` int(10) NOT NULL COMMENT '最后回复id',
			`title` varchar(100) NOT NULL COMMENT '标题',
			`text` TEXT NOT NULL COMMENT '正文',
			PRIMARY KEY (`id`)
			)ENGINE=MyISAM DEFAULT CHARSET=utf8''')
		self.m_db.query('''CREATE TABLE IF NOT EXISTS `discuss_reply`(
			`id` int(10) NOT NULL AUTO_INCREMENT,
			`tid` int(10) NOT NULL COMMENT '主题id',
			`uid` int(10) NOT NULL COMMENT '用户id',
			`rid` int(10) NOT NULL COMMENT '回复某个回复',
			`ctime` int(11) NOT NULL COMMENT '创建时间',
			`mtime` int(11) NOT NULL COMMENT '修改时间',
			`text` TEXT NOT NULL COMMENT '正文',
			PRIMARY KEY (`id`)
			)ENGINE=MyISAM DEFAULT CHARSET=utf8''')
