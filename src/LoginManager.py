# coding=UTF-8
'''
Created on 2015-12-4

@author: write_1
'''
from config import CurrentLoginPosi
from sqlfun import datafun
# 函数作用：登陆，
# 函数参数：ID，1，2，3，教师，学生，管理员
# 函数备注：

def login(ID):
	username = raw_input("username:")	
	possword = raw_input("posswd:")    
	if ID==1:	
		if isPass('teacher_login', username, possword):
			print "teacher_login success"
			CurrentLoginPosi = 1 
			return True   
		else:
			print "用户或者密码输入错误"
			return False
	if ID==2:	
		if isPass('student_login', username, possword):
			print "student_login success"
			CurrentLoginPosi = 2 
			return True   
		else:
			print "用户或者密码输入错误"
			return False
	if ID==3:	
		if isPass('Manager_login', username, possword):
			print "manager Login success"
			CurrentLoginPosi = 3 
			return True   
		else:
			print "用户或者密码输入错误"
			return False
# 函数作用：验证是否登陆成功
# 函数参数：rablename,连接的数据库名称，username，输入的用户名，posswd输入的用户密码
# 函数备注：
def isPass(tablename,username,posswd):
    datacon = datafun()    #创建一个数据库操作对象
    UserInfor = datacon.getAlldata(tablename)
#     for managerObject in UserInfor:
    if posswd == UserInfor[0]['posswd'] and username==UserInfor[0]['username']:            
       return True
    else:
        return False



