#coding:utf-8
import os
import sys
import logging
import tornado.web
import tornado.ioloop
from tornado.options import define,options

sys.path.append('./manager')
from login import LoginHandler
from login import LogoutHandler

from admin import AdminHandler

from manager_user import UserHandler, Edit_UserHandler, Del_UserHandler
from manager_grp import GroupHandler, Del_GroupHanler, Edit_GroupHanler
from manager_host import HostHandler

handlers=[
		(r'/',LoginHandler),
		(r'/logout',LogoutHandler),
		(r"/op-admin",AdminHandler),
		(r"/manager_user",UserHandler),
		(r"/edit_user",Edit_UserHandler),
		(r"/del_user",Del_UserHandler),
		(r"/manager_group",GroupHandler),
		(r"/del_grp",Del_GroupHanler),
		(r"/edit_grp",Edit_GroupHanler),
		(r"/host",HostHandler),
		]
settings={
		'debug' : True,
		'static_path':os.path.join(os.path.dirname(__file__),'static'),
		'template_path':os.path.join(os.path.dirname(__file__),'template'),
		'cookie_secret': 'bZJc2sWbQLKos6GkHn/VB9oXwQt8S0R0kRvJ5/xJ89E=',
		'login_url':'/',
		}

app=tornado.web.Application(handlers,**settings)
options.parse_command_line()
logging.debug("debug ...")
options.parse_command_line()
app.listen(8888)
tornado.ioloop.IOLoop.instance().start()
