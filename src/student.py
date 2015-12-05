# coding=UTF-8
'''
Created on 2015-12-3

@author: write_1
'''

from study import Grade, like, wenke
from __builtin__ import int
from config import config

class Student(object):
    '''
    classdocs
    ''' 
    def SA(self,classg,classed):
        if classg == 1 and classed<config.one:
            return "li"
        if classg == 2 and classed<config.two:
            return "li"
        if classg == 3 and classed<config.three:
            return "li"
        return "wen"                    
# classed��float�� 1.2 2.3 1.13 3.23            ��һλ��ʾ�꼶���ڶ���λ��ʾ�༶����
    def __init__(self,id, name , sex ,age ,classed ):
        self.id = id
        self.sex = sex
        self.name = name
        self.age = age
        self.classGrade = int(classed)
        self.classed = (classed-self.classGrade)*10
        self.sa = Student.SA(self.classGrade,classed)
        if self.sa == "li":
            self.grade = like()
        else:
            self.grade = wenke()
               
        
    def setqinshi(self,qinshi):
        self.qinshi = qinshi
    
        
        