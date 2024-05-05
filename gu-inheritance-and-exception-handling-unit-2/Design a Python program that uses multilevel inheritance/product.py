class Product:
    def __init__(self, name, price):
        #..... YOUR CODE STARTS HERE .....
    
        self.name = name
        self.price = price
    
        #..... YOUR CODE ENDS HERE .....

class PhysicalProduct(Product):
    def __init__(self, name, price, weight):
        #..... YOUR CODE STARTS HERE .....
    
        self.name = name 
        self.price = price 
        self.weight = weight 
                
        #..... YOUR CODE ENDS HERE .....

    def print_details(self):
        #..... YOUR CODE STARTS HERE .....
    
        print(f"Physical Product: {self.name}, Price: ${self.price}, Shipping Weight: {self.weight} kg")
    
        #..... YOUR CODE ENDS HERE .....

class DigitalProduct(Product):
    def __init__(self, name, price, file_size):
        #..... YOUR CODE STARTS HERE .....
    
        self.name = name
        self.price = price 
        self.file_size = file_size 
    
        #..... YOUR CODE ENDS HERE .....

    def print_details(self):
        #..... YOUR CODE STARTS HERE .....
    
        print(f"Digital Product: {self.name}, Price: ${self.price}, File Size: {self.file_size} MB")
    
        #..... YOUR CODE ENDS HERE .....
        
class HybridProduct(PhysicalProduct, DigitalProduct):
    def __init__(self, name, price, weight, file_size):
        #..... YOUR CODE STARTS HERE .....
    
        super().__init__(name, price, weight) 
        DigitalProduct.__init__(self, name, price, file_size)
        
        #..... YOUR CODE ENDS HERE .....
        
    def print_details(self):
        #..... YOUR CODE STARTS HERE .....
    
        print(f"Hybrid Product: {self.name}, Price: ${self.price}, Shipping Weight: {self.weight} kg, File Size: {self.file_size} GB")
    
        #..... YOUR CODE ENDS HERE .....
        

def clean_input(value):
    return str(value.strip())
    

if __name__ == '__main__':
    pp_name, pp_price, shipping_weight = map(clean_input, input().strip().split(','))
    physical_product = PhysicalProduct(pp_name, pp_price, shipping_weight)
    
    dp_name, dp_price, file_size = map(clean_input, input().strip().split(','))
    digital_product = DigitalProduct(dp_name, dp_price, file_size)
    
    hp_name, hp_price, hp_shipping_weight, hp_file_size = map(clean_input, input().strip().split(','))
    hybrid_product = HybridProduct(hp_name, hp_price, hp_shipping_weight, hp_file_size)
    
    physical_product.print_details()
    digital_product.print_details()
    hybrid_product.print_details()