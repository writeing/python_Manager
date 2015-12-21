# coding=UTF-8
'''
Created on 2015-12-4

@author: write_1
'''
from config import CurrentLoginPosi
from LoginManager import login
from turtle import Turtle
from ManagerAction import selectfun
from __builtin__ import exit

# 界面函数，目前没有加入网页功能还有界面，所以只用了字符串打印的方式
def Interface():
    print "1:新建班级"  #先新建班级，建了之后，再加入学生
    print "2:新建任课老师"
    print "3:新建班主任"
    print "4:drop student"
    print "5:drop teacher"
    print "6:drop charge"
    print "7:exit"
    select = input("your choose")    
    if not selectfun[select]():
        Interface()
    else:
        print "插入了学生信息"
    
    
    
    
def main():
    loginTime=0	 #登陆次数计数
    print "请选择你要登陆的用户"    
    result = input("1:老师\t2:学生\t3:管理员\n您是:")
    while not login(result):     
        loginTime = loginTime+1
        if loginTime>3:     #超过3次就退出       
            print "您输入错误的次数大于3次，"
            input("按任意键退出")
            exit(0)                                         
    Interface()		#界面函数	
if __name__ == '__main__':
    main()
