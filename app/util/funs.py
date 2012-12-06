# -*- coding: utf-8 -*-

def isInt(s):
	if s[0] in ('-', '+'):
		return s[1:].isdigit()
	return s.isdigit()
