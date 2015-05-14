#coding:utf-8
import pass_jm
import tornado.web
from datetime import datetime
from db import db_operation

def login_time():

    '记录用户登录时间插入数据库'

    now_time = datetime.now()
    date = now_time.strftime('%Y-%m-%d %I:%M:%S %p')
    return date

def check(name,passwd):

    '用来判断登录名和密码是否正确'

    data = db_operation('select pin,pwd from yw_user where pin="%s"' % name).select()
    if data:
        db_pass = data[0]['pwd']
	if pass_jm.pass_verify(passwd,db_pass):
            return True
	else:
	    return False
    else:
        return False


class BaseHandler(tornado.web.RequestHandler):

    '设置COOKIE'

    def get_current_user(self):
        return self.get_secure_cookie("username")


class LoginHandler(BaseHandler):

    '登录页面,用来判断用户名和密码和跳转相应页面'

    def get(self):
        self.render('login.html')

    def post(self):
        name = self.get_argument('username')
        passwd = self.get_argument('password')

	if not check(name,passwd):
            return self.write('''<script>
                alert ("用户名或密码错误!")
	        window.location.href="/"
		</script>
            ''')
	else:
            db_operation('UPDATE yw_user set login_date="%s" where pin="%s"' % (login_time(),name)).update()
            self.set_secure_cookie("username",name)
            self.redirect('/op-admin')


class LogoutHandler(BaseHandler):

    '退出登录,清除COOKIE'

    def get(self):
        self.clear_cookie("username")
        self.redirect("/")

