# -*- coding: utf-8 -*-

import time

def isInt(s):
	if s[0] in ('-', '+'):
		return s[1:].isdigit()
	return s.isdigit()

def timeStamp2Str(t):
	time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(t))
