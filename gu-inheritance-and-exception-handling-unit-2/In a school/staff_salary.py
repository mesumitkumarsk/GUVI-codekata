from abc import ABC, abstractmethod

class StaffMember(ABC):
    @abstractmethod
    def get_salary(self):
        pass

    #..... YOUR CODE STARTS HERE .....
    
class Teacher(StaffMember):
    def get_salary(self):
        return 3000

class Janitor(StaffMember):
    def get_salary(self):
        return 2000
        
class Administrator(StaffMember):
    def get_salary(self):
        return 4000
    
    #..... YOUR CODE ENDS HERE .....
        
def call_func(cls, func):
    value = None
    cls_obj = None
    
    if (cls == "Teacher()"):
        cls_obj = Teacher()
    
    elif(cls == "Janitor()"):
        cls_obj = Janitor()
        
    elif(cls == "Administrator()"):
        cls_obj = Administrator()
    
    if (func == "get_salary()"):
        value = cls_obj.get_salary()
        
    return value

for _ in range(3):
    cls, func = input().strip().split(".")
    print(call_func(cls, func))