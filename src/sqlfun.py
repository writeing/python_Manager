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
    def connectsql(self):
        self.con = sqlite3.connect("..\database\P_Manage")
        self.con = sqlite3.Row
    
    def getAlldata(self,tablenname):
        self.cur = self.con.curson()
        datasql = self.cur.execute("select * from (?)",tablenname)
        datasql.fetchall()
        return datasql
    def getOnedata(self,cmd=None):
        datasql = self.cur.execute("select * from (?) where (?)=(?)",cmd)
        datasql.fetchone()
        return datasql
    
# for t in [('2006-03-28', 'BUY', 'IBM', 1000, 45.00),
#           ('2006-04-05', 'BUY', 'MSFT', 1000, 72.00),
#           ('2006-04-06', 'SELL', 'IBM', 500, 53.00),
#          ]:
#     c.execute('insert into stocks values (?,?,?,?,?)', t)

    def Insertdata(self,tablename,dictdata=None,datalen=6):
        cmddata = "insert into x value{?}"
        cmddata = cmddata.replace('x',tablename,1)
        for i in range(datalen-1):
            cmddata = cmddata.replace('?', "??",1)
        strCmd = cmddata
        for i in dictdata:                
            for j in range(datalen-1):
                strCmd = str.replace('?',i[j]+',',1)
            strCmd = str.replace('?',i[j+1],1)        
            self.cur.execute(strCmd)
            strCmd = cmddata       
    def DropdateforId(self,tablename,id):
        cmddata = "drop table x where id = ?"
        cmddata = cmddata.replace('x', tablename,1)
        cmddata = cmddata.replace('?',id,1)
        self.cur.execute(cmddata)
    def closedatabase(self):
        self.con.close()    
    def __init__(self):
        '''
        Constructor
        '''
        
