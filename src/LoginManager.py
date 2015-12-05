# coding=UTF-8
'''
Created on 2015-12-4

@author: write_1
'''
from config import CurrentLoginPosi
def teacherLogin():
    print "请输入您的用户名和密码"
    username = raw_input("username:")
    possword = raw_input("posswd:")
    print "Teacher Login success"
    CurrentLoginPosi = 1
    #对比成功之后就进去了
    return
def studentLogin():
    username = raw_input("username:")
    possword = raw_input("posswd:")
    print "Student Login success"
    CurrentLoginPosi = 2    
    return

def root():
    username = raw_input("username:")
    possword = raw_input("posswd:")
    if username=="root" and possword=="root":
        print "manager Login success"
        CurrentLoginPosi = 3    
    return

LoginWai = dict()
LoginWai[1] = teacherLogin
LoginWai[2] = studentLogin
LoginWai[3] = root                




