# coding=UTF-8
'''
Created on 2015-12-3

@author: write_1
'''

from student import Student


class Teacher(object):
    '''
    classdocs
    '''
    stu  = dict()		#忘了
    Classed = set()
    def __init__(self, name,age,sex,posi):
        self.name = name
        self.age = age
        self.sex = sex
        self.posi = posi
        '''
        Constructor
        '''
	# 添加老师的班级，因为一个老师可以带多个班级
    def setClass(self,Class):
        self.Classed.add(Class)
		
    def getClass(self):
        return self.Classed