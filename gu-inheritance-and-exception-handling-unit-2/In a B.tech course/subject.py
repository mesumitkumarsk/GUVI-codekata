from abc import ABC, abstractmethod

class Subject(ABC):
    #..... YOUR CODE STARTS HERE .....
    
    @abstractmethod 
    def has_lab(self):
        pass 
    @abstractmethod
    def has_project(self):
        pass 
    @abstractmethod
    def get_theory_marks(self):
        pass
    
    #..... YOUR CODE ENDS HERE .....

class LabSubject(Subject):
    def has_lab(self):
        #..... YOUR CODE STARTS HERE .....
    
        return True
    
        #..... YOUR CODE ENDS HERE .....
    
    def has_project(self):
        #..... YOUR CODE STARTS HERE .....
    
        return False    
    
        #..... YOUR CODE ENDS HERE .....
    
    def get_theory_marks(self):
        #..... YOUR CODE STARTS HERE .....
    
        return 70
    
        #..... YOUR CODE ENDS HERE .....

class ProjectSubject(Subject):
    def has_lab(self):
        #..... YOUR CODE STARTS HERE .....
    
        return False
    
        #..... YOUR CODE ENDS HERE .....
    
    def has_project(self):
        #..... YOUR CODE STARTS HERE .....
    
        return True
    
        #..... YOUR CODE ENDS HERE .....
    
    def get_theory_marks(self):
        #..... YOUR CODE STARTS HERE .....
    
        return 80 
    
        #..... YOUR CODE ENDS HERE .....

class TheorySubject(Subject):
    def has_lab(self):
        #..... YOUR CODE STARTS HERE .....
    
        return False
    
        #..... YOUR CODE ENDS HERE .....
    
    def has_project(self):
        #..... YOUR CODE STARTS HERE .....
    
        return False
    
        #..... YOUR CODE ENDS HERE .....
    
    def get_theory_marks(self):
        #..... YOUR CODE STARTS HERE .....
    
        return 90
    
        #..... YOUR CODE ENDS HERE .....
        
def call_func(cls, func):
    value = None
    
    if (func == "has_lab()"):
        value = cls.has_lab()
        
    elif(func == "has_project()"):
        value = cls.has_project()
        
    elif(func == "get_theory_marks()"):
        value = cls.get_theory_marks()
        
    return value

# Getting input from the user
lab_class, lab_func = input().strip().split(".")
project_class, project_func = input().strip().split(".")
theory_class, theory_func = input().strip().split(".")

if (lab_class == 'LabSubject()'):
    lab = LabSubject()
    print(call_func(lab, lab_func))

if(project_class == "ProjectSubject()"):
    project = ProjectSubject()
    print(call_func(project, project_func))
    
if(theory_class == "TheorySubject()"):
    theory = TheorySubject()
    print(call_func(theory, theory_func))