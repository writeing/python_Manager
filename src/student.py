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
	# 函数功能:确认这个班级是文科还是理科
	# 函数参数:classg:年级，classed：班级
	# 函数备注:
    def SA(self,classg,classed):
        if classg == 1 and classed<config.one:
            return "li"
        if classg == 2 and classed<config.two:
            return "li"
        if classg == 3 and classed<config.three:
            return "li"
        return "wen"                    

	
	# 初始化学生数据，输入的数据，
	# 参数：学生ID，学生姓名,学生班级，学生寝室号，性别，年级
    def __init__(self,id, name , classed ,dorm  ,sex ='men',age = 0):
        self.id = id
        self.sex = sex
        self.name = name
        self.age = age
#         self.classGrade = int(classed)
        self.classed = classed#(classed-self.classGrade)*10
#         self.sa = Student.SA(self.classGrade,(classed-self.classGrade)*10)
#         if self.sa == "li":
#             self.grade = like()
#         else:
#             self.grade = wenke()
        self.dorm = dorm
               
    # 函数功能:设置寝室号
	# 函数参数:寝室编号，一个int	
	# 函数备注:
    def setqinshi(self,qinshi):
        self.qinshi = qinshi
    # 函数功能:返回一个学生数组
	# 函数参数:无
	# 函数备注:
    def getStudentArray(self):
        self.stuArray = (self.id,self.name,self.classed,self.dorm,self.sex,self.age)
        return self.stuArray
        
        
           