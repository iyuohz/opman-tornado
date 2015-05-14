#coding:utf-8
import tornado.web
from login import BaseHandler
from dh import dh

class AdminHandler(BaseHandler):
     
     '主机监控、管理功能'
     @tornado.web.authenticated

     def get(self):
        
        name = self.get_secure_cookie("username") 
        dh_data = dh(host='active') 
        self.render('admin.html',dh=dh_data)

