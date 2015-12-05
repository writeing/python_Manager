# coding=UTF-8
'''
Created on 2015-12-3

@author: write_1
'''

grade = dict()

class Grade(object):
    '''
    classdocs
    '''    
    def __init__(self):
        '''
        Constructor
        '''        
        self.grade["yuwen"] = 0
    
        self.grade["shuxue"] = 0
    
        self.grade["yingyu"] = 0
class wenke(Grade):
    def __init__(self):
        super()
        self.grade["zhengzhi"] = 0
        self.grade["lishi"] = 0
        self.grade["dili"] = 0

class like(Grade):
    def __init__(self):
        super()
        self.grade["wuli"] = 0    
        self.grade["huaxue"] = 0    
        self.grade["shengwu"] = 0
