#coding=utf-8
import pass_jm
import tornado.web

from dh import dh
from db import db_operation
from login import BaseHandler

def yanzheng(data,sucess,error):

    '根据数据库返回来的数据,来返回来alert的值'
    if not  data:
        suce =  '<script>\nalert ("%s")\nwindow.location.href="/manager_user"\n</script>'% sucess 
        return suce
    err =  '<script>\nalert ("%s") \nwindow.location.href="/manager_user"\n</script>'% error
    return err
     

class UserHandler(BaseHandler):

    '管理用户'

    @tornado.web.authenticated
    def get(self):

        self.get_secure_cookie("username")
        select = db_operation('select * from yw_user').select()
        dh_data = dh(user='active') 
        #self.render('manager/user/manager_user.html',dh=dh_data,select=select)
        self.render('manager/user/manager_user.html',select=select)

    def post(self):

        '新建用户'

        username = self.get_argument('create_username')
        ms = self.get_argument('create_ms').encode('utf-8').decode('utf-8')
        password = self.get_argument('create_password','').decode('utf-8')
        create_admin = self.get_argument('create_admin',0)
        create_status = self.get_argument('create_status',0)
        crypt_pass = pass_jm.pass_crypt(password)
        argument_data = {
         
              'username':username,
              'ms':ms,
              'crypt_pass':crypt_pass,
              'create_admin':create_admin,
              'create_status':create_status
        }

        sql = 'insert into yw_user (pin,pwd,isAdmin,isLock,remaks)\
        values("%(username)s","%(crypt_pass)s",%(create_admin)s,%(create_status)s,"%(ms)s")' % argument_data
  
        select_name = db_operation('select pin,pwd from yw_user where pin="%s"' % username).select()
        print select_name
        if select_name:

            message = yanzheng(1,'创建成功','创建失败,用户已存在')
            return self.write(message)
        
        data = db_operation(sql).update()
        print data
        message = yanzheng(data,'用户创建失败','用户创建成功')
        self.write(message)

class Edit_UserHandler(BaseHandler):
    
    '编辑用户'

    @tornado.web.authenticated
    def post(self):
        
        id = self.get_argument('id')
        ms = self.get_argument('ms').encode('utf-8').decode('utf-8')
        password = self.get_argument('password')
        admin = self.get_argument('admin',0)
        status = self.get_argument('status',0)
        crypt_pass = pass_jm.pass_crypt(password)

        argument_data = {
              'id':id,
              'ms':ms,
              'crypt_pass':crypt_pass,
              'admin':admin,
              'status':status
        }

        if password:
            sql = 'update yw_user set \
            pwd="%(crypt_pass)s",isAdmin=%(admin)s,isLock=%(status)s,remaks="%(ms)s" where id=%(id)s' % argument_data            
        else: 
            sql = 'update yw_user set \
            isAdmin=%(admin)s,isLock=%(status)s,remaks="%(ms)s" where id=%(id)s' % argument_data        

        data = db_operation(sql).update()
        print data
        message = yanzheng(data,'用户修改成功','用户修改失败')
        self.write(message)

class Del_UserHandler(BaseHandler):

    '删除用户'

    @tornado.web.authenticated
    def post(self):
     
        delete = self.get_argument('delete')
        sql = 'delete from yw_user where id=%s' % delete
        data = db_operation(sql).delete()
        print data
        message = yanzheng(data,'用户删除成功','用户删除失败')
        self.write(message)

