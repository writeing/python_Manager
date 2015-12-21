# coding=UTF-8


# classed = "班主任"
# grade = "wuli"
# 
# print (classed=="班主任" and grade=="wuli")


import sqlite3
import MySQLdb
import string
from __builtin__ import int, str

# def dict_factory(cursor, row):
#     d = {}
#     for idx, col in enumerate(cursor.description):
#         d[col[0]] = row[idx]
#     return d
# 
#  
conn = sqlite3.connect("../database/P_Manager.db")
 
conn.row_factory = sqlite3.Row
# 
dataSql = conn.cursor()
#dataSql.execute("'create database '")
#dataSql.execute("create table student_infor( id VARCHAR(1,10) primary key)")
 
tablename = ('student_infor','1234567')
# cmddata = []
# cmddata.append('student_infor')
cmd = "select * from ? where id= '1234567'"
cmd = cmd.replace('?',tablename[0],1)
dataSql.execute(cmd)
data = dataSql.fetchall()
print data[0]["id"]
# dictdata=[
#           ('wang','dw','ds','das','da','aaa'),
#           ('xian','dw','ds','das','da','ccc'),
#           ('chao','dw','ds','das','da','ddd'),
#         ]
# def setInsertdata(tablename,dictdata=None,datalen=6):
#     cmddata = "insert into x value{?}"
#     cmddata = cmddata.replace('x',tablename,1)
#     for i in range(datalen-1):
#         cmddata = cmddata.replace('?', "??",1)
#     str = cmddata
#     for i in dictdata:                
#         for j in range(datalen-1):
#             str = str.replace('?',i[j]+',',1)
#         str = str.replace('?',i[j+1],1)
#         print str
#         str = cmddata
# setInsertdata('studeint_infor',dictdata, 4)
# 
id = "wamh"
stuArray = (id,id)
# 
# stuArray.append("xian")
# stuArray.append("chao")
# 
# sss.append(stuArray)
# stuArray.append("da")
# stuArray.append("sha")
# stuArray.append("bi")
# sss = [] 
# sss.append(stuArray)
dictdata=[
          (123,'dw','ds','das','da','aaa'),
          ('xian','dw','ds','das','da','ccc'),
          ('chao','dw','ds','das','da','ddd'),
        ]
for i in dictdata:
    if type(i[0]) == str:
        print i[0]
    




















