class Calculator:
    def add(self, a, b):
        return a + b
    
    def subtract(self, a, b):
        return a - b
    
    def multiply(self, a, b):
        return a * b
    
    def divide(self, a, b):
        if b != 0:
            return a / b
        else:
            return "Error: Division by zero"

# Read the input integers
a, b = map(int, input().split())

# Create an instance of the Calculator class
calculator = Calculator()

# Perform the operations and print the results
print(calculator.add(a, b))
print(calculator.subtract(a, b))
print(calculator.multiply(a, b))
print(calculator.divide(a, b))
