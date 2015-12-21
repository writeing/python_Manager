# coding=UTF-8
'''
Created on 2015-12-3

@author: write_1
'''
from sqlfun import datafun
# 表示现在登录的用户是什么身份
CurrentLoginPosi = 0  # 0 没有人    1 学生     2 老师   3  管理员

# 设置文科的班级是多少，这样能区分文理科的班级
class Config(object):
    
    def __init__(self):
        '''
        Constructor
        '''
    def setwkclass(self, one, two, three):
        self.one = one
        self.two = two
        self.three = three
        
# 构造函数，构造一个对象，这样别的地方就可以直接引用了      
config = Config()       #修改学校班级 文理科分级线的对象
datacon = datafun()		#操作数据库的对象，
#函数功能:设置学生的一门成绩
#函数参数:posi:教师职位，是谁再设置学生的成绩   student_id:学生id，修改谁的成绩，grade，设置的成绩
#函数返回值:返回false，或者true。
#函数备注:
def setGrade(posi, student_id, grade):    
#     student.grade.grade[teacher.posi] = grade    
    datacon.connectsql()
    datacon.UpdateforId('cs', posi, grade, student_id)
    checkdata = datacon.getOnedata('cs', 'id', student_id)
    datacon.closedatabase()
    if checkdata[posi] == grade:
        return True
    else:
        return False        
		
#函数功能:设置学生的所有成绩
#函数参数:posi:教师职位，是谁再设置学生的成绩   student_id:学生id，修改谁的成绩，grade，设置的成绩
#函数返回值:返回false，或者true。
#函数备注: 这个函数的grade是一个数组，
def setAllGrade(posi, student_id, grade):  
    if posi != "班主任":
        return False
      
#     student.grade.grade["yuwen"] = yu
#     student.grade.grade["shuxue"] = shu
#     student.grade.grade["yingyu"] = wai
#     student.grade.grade["zhengzhi"] = zheng
#     student.grade.grade["lishi"] = shi
#     student.grade.grade["dili"] = di
    for i in range(5):
        if not setGrade(posi, student_id, grade[i]):
            return False
    return True   
        
            
