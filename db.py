#coding:utf-8
import torndb
from config import Get_data

getdata = Get_data('./config.ini')

dbhost = getdata.Show_option_data('db','db_host')
dbname = getdata.Show_option_data('db','db_name')
dbuser = getdata.Show_option_data('db','db_user')
dbpass = getdata.Show_option_data('db','db_pass')

class db_operation(object):
    'MySQL的增删改查'
    def __init__(self,sql):
        try:
            db = torndb.Connection(dbhost,dbname,user=dbuser,password=dbpass)
            self.sql = sql
            self.db = db
        except Exception,e:
            print '数据库连接失败!'

    def select(self):
        try:
            select_data = self.db.query(self.sql)
            return select_data
        except Exception,e:
            print self.sql
            print 'SQL 语法有问题!'
        finally:
            self.db.close()

    def update(self):
        try:
            update_data = self.db.execute(self.sql)
            return update_data
        except Exception,e:
            print self.sql
	    print 'SQL 语法有问题!'
	finally:
	    self.db.close()

    def delete(self):
        try:
	    delete_data = self.db.execute(self.sql)
	    return delete_data
	except Exception,e:
	    print self.sql
	    print 'SQL 语法有问题!'
	finally:
	    self.db.close()

