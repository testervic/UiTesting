#coding:utf-8
import MySQLdb
from common.log import *

class mysql_handle():

    def __init__(self, host, port, user, password):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = ''
        self.conn = ''
        self.cur = ''
        #数据库连接状态，0为未连接，1为已连接
        self.status = 0

    #连接数据库
    def mysql_connect(self):
        try:
            self.conn = MySQLdb.connect(host = self.host, passwd = self.password, port = self.port, user = self.user)        
            self.cur = self.conn.cursor()
            self.status = 1
            logging.info('数据库连接成功.')
        except MySQLdb.Error, e:
            logging.error('数据库连接失败.\n\tERROR:'.decode('utf-8') + str(e))

    #选择指定库
    def mysql_select_db(self, database):
        self.database = database
        try:
            self.conn.select_db(database)
            logging.info('选择数据库:'.decode('utf-8') + database + '成功.'.decode('utf-8'))
        except MySQLdb.Error, e:
            logging.error('选择数据库:'.decode('utf-8') + database + '失败.'.decode('utf-8') + '\n\tERROR:' + str(e))

    #关闭数据库
    def mysql_close_db(self):
        self.conn.close()
        logging.info('数据库关闭成功.')


    #sql查询命令执行,返回执行结果
    def exc_sql(self,sql):
        try:
            #返回结果list保存, return_result[0]为查询结果行数, return_result[1]为查询结果详细数据
            return_result = []
            return_result.append(self.cur.execute(sql))
            return_result.append(self.cur.fetchall())
            #logging.info('SQL执行成功:'.decode('utf-8') + sql)
            return return_result
        except MySQLdb.Warning, w:
            logging.warning('WARNING:' + str(w))
            return 0
        except MySQLdb.Error, e:
            logging.error('SQL执行失败!\n\tSQL:('.decode('utf-8') + sql + ')\n\tERROR:' + str(e))
            return 0
            
        
        


    


