class Item:
    def __init__(self, title, price):
        #..... YOUR CODE STARTS HERE .....
    
        self.title = title
        self.price = price 
    
        #..... YOUR CODE ENDS HERE .....

    def change_price(self, new_price):
        #..... YOUR CODE STARTS HERE .....
        
        self.new_price = new_price 
        self.price = self.new_price 
    
        #..... YOUR CODE ENDS HERE .....

    def print_details(self):
        #..... YOUR CODE STARTS HERE .....
    
        print(f"Item: {self.title}, priced at ${self.price}")
    
        #..... YOUR CODE ENDS HERE .....


class Book(Item):
    def __init__(self, title, author, price):
        #..... YOUR CODE STARTS HERE .....
    
        super().__init__(title,price)
        self.author=author 
    
        #..... YOUR CODE ENDS HERE .....

    def print_details(self):
        #..... YOUR CODE STARTS HERE .....
    
        print(f"Book: {self.title} by {self.author}, priced at ${self.price}")
    
        #..... YOUR CODE ENDS HERE .....


class Magazine(Item):
    def __init__(self, title, price, issue):
        #..... YOUR CODE STARTS HERE .....
    
        super().__init__(title, price)
        self.issue = issue
    
        #..... YOUR CODE ENDS HERE .....

    def print_details(self):
        #..... YOUR CODE STARTS HERE .....
    
        print(f"Magazine: {self.title}, Issue No. {self.issue}, priced at ${self.price}")
    
        #..... YOUR CODE ENDS HERE .....


def clean_input(ip):
    return str(ip.strip())
    
book_title, book_author, book_price = map(clean_input, input().strip().split(","))
mz_title, mz_price, mz_issue = map(clean_input, input().strip().split(","))

book1 = Book(book_title, book_author, book_price)
magazine1 = Magazine(mz_title, mz_price, mz_issue)

# Printing initial details
book1.print_details()
magazine1.print_details()

# Changing prices
book1.change_price(input())
magazine1.change_price(input())

# Printing updated details
book1.print_details()
magazine1.print_details()