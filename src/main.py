# coding=UTF-8
'''
Created on 2015-12-4

@author: write_1
'''
from config import CurrentLoginPosi
from LoginManager import LoginWai


def Interface():
    print "1:新建班级"
    print "2:新建任课老师"
    print "3:新建班主任"
    print "4:drop student"
    print "5:drop teacher"
    print "6:drop charge"
    print "7:exit"
    select = input("your choose")
    
    
    
    
    
def main():
    print "请选择你要登陆的用户"    
    result = input("1:老师\t2:学生\t3:管理员\n:")
    LoginWai[result]
    Interface()
if __name__ == '__main__':
    main()
