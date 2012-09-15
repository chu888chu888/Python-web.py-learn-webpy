# coding=utf-8
from controller.base.Controller import Controller
import web

class RegisterResult(Controller):
    def process(self):
        i = web.input()
        self.setVariable('msg','功能未完成')
