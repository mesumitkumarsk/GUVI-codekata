class ElectronicDevice:
    def __init__(self, name, price):
        #..... YOUR CODE STARTS HERE .....
    
        self.name = name
        self.price = price 
    
        #..... YOUR CODE ENDS HERE .....

class Mobile(ElectronicDevice):
    def __init__(self, name, price, screen_size):
        #..... YOUR CODE STARTS HERE .....
    
        super()._init_(name,price)
        self.screen_size=screen_size 
    
        #..... YOUR CODE ENDS HERE .....
        
    def print_details(self):
        #..... YOUR CODE STARTS HERE .....
    
        return(f"Mobile: {self.name}, Price: ${self.price}, Screen Size: {self.screen_size} inches")
    
        #..... YOUR CODE ENDS HERE .....

class Laptop(ElectronicDevice):
    def __init__(self, name, price, screen_resolution):
        #..... YOUR CODE STARTS HERE .....
    
        super()._init_(name, price)
        self.screen_resolution = screen_resolution
    
        #..... YOUR CODE ENDS HERE .....

    def print_details(self):
        #..... YOUR CODE STARTS HERE .....
    
        return(f"Laptop: {self.name}, Price: ${self.price}, Screen Resolution: {self.screen_resolution}")
    
        #..... YOUR CODE ENDS HERE .....

# Get sample input from the user
mobile_input = input().split(", ")
laptop_input = input().split(", ")

# Create objects
mobile = Mobile(*mobile_input)
laptop = Laptop(*laptop_input)

# Print details
print(mobile.print_details())
print(laptop.print_details())