# coding=utf-8
from controller.base.FrameController import FrameController
import model.user.UserLogin
import web
from _mysql_exceptions import IntegrityError

class RegisterResult(FrameController):
    def process(self):
        i = web.input()
        
        m = model.user.UserLogin.UserLogin()
        try:
            uid = m.insert({'loginname':i.loginname,'password':m.str_md5(i.password)})
        except IntegrityError:
            self.setVariable('msg','存在同名用户，无法重复注册')
        else:
            self.setVariable('msg','注册成功')
            
            mUserInfo = model.Model.Model('userinfo')
            mUserInfo.insert({
                'uid' : uid,
                'nickname' : i.nickname,
                'email' : i.email
            });
