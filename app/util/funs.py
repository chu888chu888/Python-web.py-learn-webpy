# -*- coding: utf-8 -*-

import time

def isInt(s):
	if s[0] in ('-', '+'):
		return s[1:].isdigit()
	return s.isdigit()

def timeStamp2Str(t):
	return time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(t))

def timeStamp2Short(t):
	now = time.localtime()
	sti = time.localtime(t)
	
	if now.tm_year != sti.tm_year:
		return time.strftime('%Y',sti)
	elif now.tm_mon != sti.tm_mon or now.tm_mday != sti.tm_mday:
		return time.strftime('%m-%d',sti)
	else:
		return time.strftime('%H:%M',sti)
