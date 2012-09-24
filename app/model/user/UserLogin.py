import model.Model

class UserLogin(model.Model.Model):
	def __init__(self):
		super(UserLogin,self).__init__('logininfo')
