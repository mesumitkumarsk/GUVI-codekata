class User:
    def __init__(self, name, user_type):
        #..... YOUR CODE STARTS HERE .....
    
        self.name = name 
        self.user_type = user_type 
    
        #..... YOUR CODE ENDS HERE .....

    def borrow_book(self, book_title):
        #..... YOUR CODE STARTS HERE .....
    
        self.book_title = book_title
        return f'Book \"{self.book_title}\" successfully borrowed by {self.name}.'
    
        #..... YOUR CODE ENDS HERE .....

class Faculty(User):
    def __init__(self, name):
        #..... YOUR CODE STARTS HERE .....
    
        self.name = name
        
    
        #..... YOUR CODE ENDS HERE .....

    def borrow_book(self, title):
        #..... YOUR CODE STARTS HERE .....
    
        self.title = title 
        return f'DVD \"{self.title}\" successfully borrowed by {self.name}.'
    
        #..... YOUR CODE ENDS HERE .....

def main():
    while True:
        name = input()
        user_type = input().lower()
        if user_type == "faculty":
            user = Faculty(name)
        else:
            user = User(name, user_type)

        item_title = input()
        if user_type == "faculty":
            if "DVD" in item_title:
                print(user.borrow_book(item_title))
            else:
                print("Faculty members can only borrow DVDs.")
        else:
            print(user.borrow_book(item_title))

        choice = input().lower()
        if choice != "yes":
            print("Quitting the program.")
            break

if __name__ == "__main__":
    main()