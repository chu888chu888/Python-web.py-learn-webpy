class user:
	def GET(self,render,arr):
		if( arr.length > 1 ):
			fun = arr[1]
			if(fun == 'info'):
				return self.userInfo(userId)
			if(fun == 'loginresult'):
				return self.loginresult()
		else:
			return self.login()
		
	def userInfo(self,userId):
		data = {'id':userId}
		return render.userInfo(data)
	
	def login(self):
		return render.login()
	
	def loginresult(self):
		return render.loginresult()
