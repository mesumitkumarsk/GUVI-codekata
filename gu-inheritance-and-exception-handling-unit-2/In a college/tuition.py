class Student:
    #..... YOUR CODE STARTS HERE .....
    
    def get_fee(self):
        pass
    
    #..... YOUR CODE ENDS HERE .....

class Undergraduate(Student):
    def get_fee(self):
        #..... YOUR CODE STARTS HERE .....
    
        return 5000
    
        #..... YOUR CODE ENDS HERE .....

class Graduate(Student):
    def __init__(self, credits):
        #..... YOUR CODE STARTS HERE .....
    
        self.credits = credits
    
        #..... YOUR CODE ENDS HERE .....

    def get_fee(self):
        #..... YOUR CODE STARTS HERE .....
    
        return self.credits*50
    
        #..... YOUR CODE ENDS HERE .....

credits = int(input())

undergraduate = Undergraduate()
graduate = Graduate(credits)

programs = [undergraduate, graduate]
for program in programs:
    print(program.get_fee())