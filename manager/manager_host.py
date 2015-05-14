#coding:utf-8
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


class HostHandler(BaseHandler):

    '管理主机'

    @tornado.web.authenticated
    def get(self):
    	self.get_secure_cookie("username")
    	select = db_operation('select * from yw_host').select()

        self.render('manager/manager_host.html',select=select)

    def post(self):

    	'新建主机'

    	hostname = self.get_argument('create_hostname')
    	hostip = self.get_argument('create_ip')
    	osname = self.get_argument('create_osname')
    	cpuinfo = self.get_argument('create_cpuinfo')
    	meminfo = self.get_argument('create_meminfo')
    	statusinfo = self.get_argument('create_statusinfo')
        argument_data = {
         
              'hostname':hostname,
              'hostip':hostip,
              'cpuinfo':cpuinfo,
              'meminfo':meminfo,
              'statusinfo':statusinfo
        }
        sql = 'insert into yw_host (name,ip,system,cpu,mem,status)\
        values("%(hostname)s","%(hostip)s",%(cpuinfo)s,%(meminfo)s,"%(statusinfo)s")' % argument_data

        select_name = db_operation('select name,ip from yw_user where ip="%s"' % hostip).select()
        if select_name:

            message = yanzheng(1,'创建成功','创建失败,主机已存在')
            return self.write(message)
        
        data = db_operation(sql).update() 
        message = yanzheng(data,'主机创建失败','主机创建成功')
        self.write(message)

class Edit_HostHandler(BaseHandler):
    
    '编辑主机'

    @tornado.web.authenticated
    def post(self):
        
        id = self.get_argument('id')
        hostname = self.get_argument('hostname')
        hostip = self.get_argument('hostip')
        osname = self.get_argument('osname')
        cpuinfo = self.get_argument('cpuinfo')
        meminfo = self.get_argument('meminfo')

        argument_data = {
            'id':id,
            'hostname':hostname,
            'hostip':hostip,
            'osname':osname,
            'cpuinfo':cpuinfo,
            'meminfo':meminfo
        }
            
        sql = 'update yw_host set \
        name=%(hostname)s,ip=%(hostip)s,system="%(osname)s", cpu=%(cpuinfo)s, mem=%(meminfo), where id=%(id)s' % argument_data        

        data = db_operation(sql).update()
        message = yanzheng(data,'用户修改成功','用户修改失败')
        self.write(message)

class Del_HostHandler(BaseHandler):

    '删除主机'

    @tornado.web.authenticated
    def post(self):
     
        delete = self.get_argument('delete')
        sql = 'delete from yw_host where id=%s' % delete
        data = db_operation(sql).delete() 
        message = yanzheng(data,'主机删除成功','主机删除失败')
        self.write(message)
