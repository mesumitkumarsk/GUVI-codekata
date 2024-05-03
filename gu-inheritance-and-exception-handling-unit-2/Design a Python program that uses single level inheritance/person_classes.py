class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_details(self):
        pass


class Student(Person):
    def __init__(self, name, age, department):
        #..... YOUR CODE STARTS HERE .....
    
        self.name = name 
        self.age = age 
        self.department = department 
    
        #..... YOUR CODE ENDS HERE .....
        
    def print_details(self):
        #..... YOUR CODE STARTS HERE .....
    
        print(f"Student: {self.name}, Age: {self.age}, Department: {self.department}")
    
        #..... YOUR CODE ENDS HERE .....


class Teacher(Person):
    def __init__(self, name, age, subject):
        #..... YOUR CODE STARTS HERE .....
    
        self.name = name 
        self.age = age 
        self.subject = subject 
    
        #..... YOUR CODE ENDS HERE .....

    def print_details(self):
        #..... YOUR CODE STARTS HERE .....
    
        print(f"Teacher: {self.name}, Age: {self.age}, Subject: {self.subject}")
    
        #..... YOUR CODE ENDS HERE .....


def main():
    # Sample Input
    student_info = input().split(", ")
    teacher_info = input().split(", ")

    # Create objects
    student = Student(*student_info)
    teacher = Teacher(*teacher_info)

    # Print details
    student.print_details()
    teacher.print_details()


if __name__ == "__main__":
    main()