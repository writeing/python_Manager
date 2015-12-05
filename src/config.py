# coding=UTF-8
'''
Created on 2015-12-3

@author: write_1
'''


CurrentLoginPosi = 0    #0 没有人    1 学生     2 老师   3  管理员

class Config(object):
    
    def __init__(self):
        '''
        Constructor
        '''
    def setwkclass(self,one,two,three):
        self.one = one
        self.two = two
        self.three = three
        
config = Config()

        
def setGrade(teacher,student,grade):    
    student.grade.grade[teacher.posi] = grade

def setAllwkGrade(teacher,student,yu,shu,wai,zheng,shi,di):  
    if teacher.posi == "班主任":  
        student.grade.grade["yuwen"] = yu
        student.grade.grade["shuxue"] = shu
        student.grade.grade["yingyu"] = wai
        student.grade.grade["zhengzhi"] = zheng
        student.grade.grade["lishi"] = shi
        student.grade.grade["dili"] = di
    
def setAlllkGrade(teacher,student,yu,shu,wai,li,hua,sheng):    
    if teacher.posi == "班主任":
        student.grade.grade["yuwen"] = yu
        student.grade.grade["shuxue"] = shu
        student.grade.grade["yingyu"] = wai
        student.grade.grade["wuli"] = li
        student.grade.grade["huaxue"] = hua
        student.grade.grade["shengwu"] = sheng
        
        
            