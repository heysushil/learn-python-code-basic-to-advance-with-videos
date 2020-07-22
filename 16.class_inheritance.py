# inheritance:

'''
Inheritance: 2 types 
1. multilevel:
    a Parent Class
    b child class
    c child class
    d child class

    a => b => c => d

2 multiple:
    a b c => Parent Class
    d => Child Class


class = class is a combination of 
    varibale = attribute
    funciton = method

Main Class = Super / Parent Class

Sub class = Sub class / Child Class
'''

# parent class
class AClassParent:
    # construecter
    def __init__(self, name):
        self.name = name

    def userNameOutput(self):
        print('''
        -----------------------------------
                A Parent Class Data
        -----------------------------------
        User Name: {}        
        '''.format(self.name))

# child class
# know we are inherit parent class 
class BChildClass(AClassParent):
    def __init__(self, name, course):
        self.course = course
        # name will pass to super class constructer
        super().__init__(name)

    def userNameAndCourseDetail(self):
        print('Couser name: ',self.course)

    def couserOutput(self):
        print('''
        -----------------------------------
                B Child Class Data
        -----------------------------------
        Course Name: {}        
        '''.format(self.course))   

# creat c class
class C_ChildClass(BChildClass):
    def __init__(self, name, course, address):
        self.address = address
        super().__init__(name, course)

    def addressOutput(self):
        print('Your address: ',self.address)

# enter user name
name = input('Enter your name: ')
course = input('Enter your couser name: ')
address = input('Enter your address: ')

# A class creat object
# parentObj = AClassParent(name)
# parentObj.userNameOutput()

# B class object
# bClassObj = BChildClass(name, course)
# bClassObj.userNameOutput()
# bClassObj.userNameAndCourseDetail()

# C class object
cClassObj = C_ChildClass(name, course, address)
cClassObj.userNameOutput()
cClassObj.userNameAndCourseDetail()
cClassObj.addressOutput()

# for multiple class use
class MainClass1:
    def __init__(self, firstCom):
        self.firstCom = firstCom

    def firstComapnyName(self):
        print('\nFirst Comany name: ',self.firstCom)

class MainClass2:
    def __init__(self, secondCom):
        self.secondCom = secondCom

    def seconCompanyName(self):
        print('Second Comapy name: ',self.secondCom)

# child class which inherit 2 parent class detials
class ChildClassUsing2parentClass(MainClass1, MainClass2):
    def __init__(self, firsCompany, secondComapy, message):
        MainClass1.__init__(self, firsCompany)
        MainClass2.__init__(self, secondComapy)
        self.message = message

    def messageOutput(self):
        print('Welcome to our channel.')


childObjFor2Parent = ChildClassUsing2parentClass('firstComapy', 'secondComapy', 'message')
# first parent methods
childObjFor2Parent.firstComapnyName()
# second parent mehtod
childObjFor2Parent.seconCompanyName()
# child message methos
childObjFor2Parent.messageOutput()

'''
Program:

1. create class
'''