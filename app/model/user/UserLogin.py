import model.Base

class UserLogin(model.Base.Base):
	def __init__(self):
		super(UserLogin,self).__init__('logininfo')
