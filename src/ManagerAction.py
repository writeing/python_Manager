# coding=UTF-8
'''
Created on 2015-12-6

@author: write_1
'''
from student import Student
from sqlfun import datafun

classed = []
def createClass():
    class_id = raw_input("classed:")    
    classed.append(class_id)
    print "班级创建成功，请输入学生信息"
    if not addStudent():
        print "插入学生信息失败"        
        return False
    else:
        print "插入学生信息成功"
        return True 

    
def addStudent():
    studict = []
    class_id = classed.pop()
    while True:
        sID = raw_input("ID:")
        if sID == "#":
            break 
        sName = raw_input("name:")
        banji = class_id
        dorm = input("dorm:")
        sex = raw_input("sex:")
        age = input("age:")
        stuClass = Student(sID,sName,banji,dorm,sex,age)
        studict.append(stuClass.getStudentArray())
        print stuClass.getStudentArray()          
    sqlVar = datafun()    
    sqlVar.Insertdata("student_infor", studict)
    
    rData = sqlVar.getOnedata("student_infor", 'id', studict[0][0])
    print rData['id']    
    if rData['id'] == studict[0][0]:        
        return True
    else:
        print rData['name']
        return False
    
selectfun={1:createClass,
#            2:addTeacher,
#            3:addCharge,
#            4:delStudent,
#            5:delTeacher,
#            6:delCharge,
           7:exit}    
    
    
    
    