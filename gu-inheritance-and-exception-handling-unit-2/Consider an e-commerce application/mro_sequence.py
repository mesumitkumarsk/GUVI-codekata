class Product:
    def get_details(self):
        pass

class Book(Product):
    def get_details(self):
        pass

class Electronics(Product):
    def get_details(self):
        pass

class EBook(Book, Electronics):
    pass

class Apparel(Product):
    pass

class SmartWatch(Apparel, Electronics):
    pass

class Furniture(Product):
    pass

class SmartFurniture(Furniture, Electronics):
    pass

class Organic(Product):
    pass

class Grocery(Product):
    pass

class OrganicGrocery(Grocery, Organic):
    pass

def mro_sequence(cls):
    #..... YOUR CODE STARTS HERE .....
    
    return[c._name_ for c in cls.mro()]
    
    #..... YOUR CODE ENDS HERE .....

class_name = input()

cls = globals()[class_name]

# Print the MRO sequence
print(mro_sequence(cls))