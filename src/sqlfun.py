# coding=UTF-8
'''
Created on 2015-12-5

@author: write_1
'''
import sqlite3
from __builtin__ import str, int

class datafun(object):
    '''
    classdocs
    '''
    con = ""
    # 连接，和创建数据库
    def connectsql(self):
        self.con = sqlite3.connect("../database/P_Manager.db")
        self.con.row_factory = sqlite3.Row
        self.cur = self.con.cursor()        
    # 获取所有的数据
    # 参数tablename  是一个字符串
    # 返回值是一个dict数组
    def getAlldata(self, tablenname):
#         self.cur = self.con.curson()
        self.connectsql()
        cmddata = "select * from (?)"
        cmddata = cmddata.replace('?', tablenname)
        datasql = self.cur.execute(cmddata)
        datasql = datasql.fetchall()        
        self.closedatabase()
        return datasql
    #  获取一个数据
    #  参数cmd是一个数组 第一个参数是表名，第二个参数是需要筛选的变量，第三个是匹配变量
    #  返回一条数据，是一个dict
    
    def getOnedata(self, tablename, var_data, pipeidata):
        self.connectsql()
        cmddata = "select * from ? where ? = ? "
        cmddata = cmddata.replace('?', tablename, 1)
        cmddata = cmddata.replace('?', var_data, 1)
        if type(pipeidata) == str:
            cmddata = cmddata.replace('?', "\""+pipeidata+"\"", 1)
        else:
            cmddata = cmddata.replace('?', pipeidata, 1)
        datasql = self.cur.execute(cmddata)        
        datasql = datasql.fetchone()
        self.closedatabase()
        return datasql
    
# for t in [('2006-03-28', 'BUY', 'IBM', 1000, 45.00),
#           ('2006-04-05', 'BUY', 'MSFT', 1000, 72.00),
#           ('2006-04-06', 'SELL', 'IBM', 500, 53.00),
#          ]:
#     c.execute('insert into stocks values (?,?,?,?,?)', t)

	# 函数功能: 插入数据，
	# 函数参数: tablename,插入的表格名称,dictdata 插入的数据（字典）,datalen，插入的数据长度，不同的数据长度不一样
	# 函数备注:
    def Insertdata(self, tablename, dictdata=None, datalen=6):
        self.connectsql()
        cmddata = "insert into x values(?)"
        cmddata = cmddata.replace('x', tablename, 1)
        for i in range(datalen - 1):
            cmddata = cmddata.replace('?', "??", 1)
        strCmd = cmddata
        for i in dictdata:                
            for j in range(datalen - 1):
                if type(i[j]) == int:
                    strCmd = strCmd.replace('?', str(i[j]) + ',' , 1)
                else:                    
                    strCmd = strCmd.replace('?',"\'"+ i[j]+"\'" + ',', 1)                    
                    
            if type(i[j+1]) == int:
                    strCmd = strCmd.replace('?', str(i[j+1]), 1)
            else:
                    strCmd = strCmd.replace('?',"\'"+ i[j+1]+"\'", 1)  
                    
            print strCmd                                
            self.cur.execute(strCmd)
            strCmd = cmddata       
        self.con.commit()
        self.closedatabase()           
            
    # 根据ID来删除某条数据                  
	# 函数功能：删除数据，根据ID
	# 函数参数：tablename,删除数据的表格名称，id用户的ID
	# 函数备注：
    def DropdateforId(self, tablename, id):
        self.connectsql()
        cmddata = "drop table x where id = ?"
        cmddata = cmddata.replace('x', tablename, 1)
        cmddata = cmddata.replace('?', id, 1)
        self.cur.execute(cmddata)
        self.con.commit()
        self.closedatabase()
    
	# 函数功能:更新数据库参数
	# 函数参数:tablename 表格名称 ,var_data 需要被跟新的数据名称，pipeidata,被输入的数据，id=ID
	# 函数备注:
    def UpdateforId(self, tablename, var_data, pipeidata, id):
        self.connectsql()
        cmddate = "update ? set ? = ? where id = ?"
        cmddate = cmddate.replace('?', tablename, 1)
        cmddate = cmddate.replace('?', var_data, 1)
        cmddate = cmddate.replace('?', pipeidata, 1)    
        cmddate = cmddate.replace('?', id, 1)
        self.cur.execute(cmddate)
        self.con.commit()
        self.closedatabase()
    # 函数功能：关闭数据库
    def closedatabase(self):
        self.con.close()    
        
    def __init__(self):
        '''
        Constructor
        '''
        
