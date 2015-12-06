# coding=UTF-8
'''
Created on 2015-12-5

@author: write_1
'''
import sqlite3
from __builtin__ import str

class datafun(object):
    '''
    classdocs
    '''
    # 连接，和创建数据库
    def connectsql(self):
        self.con = sqlite3.connect("..\database\P_Manage")
        self.con = sqlite3.Row
    
    # 获取所有的数据
    # 参数tablename  是一个字符串
    # 返回值是一个dict数组
    def getAlldata(self, tablenname):
        self.cur = self.con.curson()
        cmddata = "select * from (?)"
        cmddata = cmddata.replace('?', tablenname)
        datasql = self.cur.execute(cmddata)
        datasql.fetchall()
        return datasql
    #  获取一个数据
    #  参数cmd是一个数组 第一个参数是表名，第二个参数是需要筛选的变量，第三个是匹配变量
    #  返回一条数据，是一个dict
    
    def getOnedata(self, tablename, var_data, pipeidata):
        cmddata = "select * from (?) where (?)=(?)"
        cmddata = cmddata.replace('?', tablename, 1)
        cmddata = cmddata.replace('?', var_data, 1)
        cmddata = cmddata.replace('?', pipeidata, 1)
        datasql = self.cur.execute(cmddata)
        datasql.fetchone()
        return datasql
    
# for t in [('2006-03-28', 'BUY', 'IBM', 1000, 45.00),
#           ('2006-04-05', 'BUY', 'MSFT', 1000, 72.00),
#           ('2006-04-06', 'SELL', 'IBM', 500, 53.00),
#          ]:
#     c.execute('insert into stocks values (?,?,?,?,?)', t)




    #     插入数据，可以插入一条，或者是多条
    def Insertdata(self, tablename, dictdata=None, datalen=6):
        cmddata = "insert into x value{?}"
        cmddata = cmddata.replace('x', tablename, 1)
        for i in range(datalen - 1):
            cmddata = cmddata.replace('?', "??", 1)
        strCmd = cmddata
        for i in dictdata:                
            for j in range(datalen - 1):
                strCmd = str.replace('?', i[j] + ',', 1)
            strCmd = str.replace('?', i[j + 1], 1)        
            self.cur.execute(strCmd)
            strCmd = cmddata       
            
            
    # 根据ID来删除某条数据                  
    def DropdateforId(self, tablename, id):
        cmddata = "drop table x where id = ?"
        cmddata = cmddata.replace('x', tablename, 1)
        cmddata = cmddata.replace('?', id, 1)
        self.cur.execute(cmddata)
        
    def UpdateforId(self, tablename, var_data, pipeidata, id):
        cmddate = "update ? set ? = ? where id = ?"
        cmddate = cmddate.replace('?', tablename, 1)
        cmddate = cmddate.replace('?', var_data, 1)
        cmddate = cmddate.replace('?', pipeidata, 1)    
        cmddate = cmddate.replace('?', id, 1)
        self.cur.execute(cmddate)
        
        
    def closedatabase(self):
        self.con.close()    
    def __init__(self):
        '''
        Constructor
        '''
        
