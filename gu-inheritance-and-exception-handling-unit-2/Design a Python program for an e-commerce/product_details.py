class Product:
    def __init__(self, name, price, seller):
        #..... YOUR CODE STARTS HERE .....
    
        self.name = name
        self.price = price
        self.seller = seller 
    
        #..... YOUR CODE ENDS HERE .....

    def print_details(self):
        #..... YOUR CODE STARTS HERE .....
        
        pass 
    
    
        #..... YOUR CODE ENDS HERE .....

class NewProduct(Product):
    def print_details(self):
        #..... YOUR CODE STARTS HERE .....
    
        return(f"New Product: {self.name}, Price: ${self.price}, Seller: {self.seller}")
    
        #..... YOUR CODE ENDS HERE .....

class UsedProduct(Product):
    def __init__(self, name, price, seller, condition):
        #..... YOUR CODE STARTS HERE .....
    
        super().__init__(name,price,seller)
        self.condition = condition 
    
        #..... YOUR CODE ENDS HERE .....

    def print_details(self):
        #..... YOUR CODE STARTS HERE .....
        
        return(f"Used Product: {self.name}, Price: ${self.price}, Seller: {self.seller}, Condition: {self.condition}")
    
        #..... YOUR CODE ENDS HERE .....

# Get input from the user
product1_info = input().split(", ")
product2_info = input().split(", ")

# Create product objects
product1 = NewProduct(*product1_info)
if len(product2_info) == 4:
    product2 = UsedProduct(*product2_info)
else:
    product2 = None

# Print details
print(product1.print_details())
if product2:
    print(product2.print_details())