import math

class Shape:
    #..... YOUR CODE STARTS HERE .....
    
    def area(self):
        pass
    
    def perimeter(self):
        pass
    
    #..... YOUR CODE ENDS HERE .....

class Circle(Shape):
    #..... YOUR CODE STARTS HERE .....
    
    def area(self, radius):
        self.radius = radius
        return math.pi*self.radius*self.radius
        
    def perimeter(self, radius):
        self.radius = radius 
        return 2*math.pi*self.radius
    
    #..... YOUR CODE ENDS HERE .....

class Rectangle(Shape):
    #..... YOUR CODE STARTS HERE .....
    
    def area(self, length, breadth):
        self.length = length 
        self.breadth = breadth
        return self.length*self.breadth
        
    def perimeter(self, length, breadth):
        self.length = length
        self.breadth = breadth 
        return 2*(self.length+self.breadth)
            
    #..... YOUR CODE ENDS HERE .....

class Triangle(Shape):
    #..... YOUR CODE STARTS HERE .....
    
    def perimeter(self,a,b,c):
        return a+b+c
    
    def area(self,a,b,c):
        s = (a+b+c)/2
        return math.sqrt(s*(s-a)*(s-b)*(s-c)) 
    
    #..... YOUR CODE ENDS HERE .....

def main():
    shape_classes = {'circle': Circle(), 'rectangle': Rectangle(), 'triangle': Triangle()}
    while True:
        shape = input().lower()
        if shape == 'quit':
            print("Quitting the program.")
            break
        elif shape not in shape_classes:
            print("Invalid input. Please enter a valid shape (circle/rectangle/triangle).")
            continue

        dimensions = list(map(float, input().split()))
        print("Area of the {}: {:.2f}".format(shape, shape_classes[shape].area(*dimensions)))
        print("Perimeter of the {}: {:.2f}".format(shape, shape_classes[shape].perimeter(*dimensions)))

if __name__ == "__main__":
    main()