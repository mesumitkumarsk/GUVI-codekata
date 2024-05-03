def get_book_details(isbn):
    books = {
        "1234567890": {"title": "Python Programming", "author": "John Doe", "price": 500, "quantity": 10},
        "9876543210": {"title": "Data Structures and Algorithms", "author": "Jane Doe", "price": 600, "quantity": 5},
        "1111111111": {"title": "Machine Learning", "author": "Sam Smith", "price": 700, "quantity": 2},
    }
    if isbn in books:
        return books[isbn]
    else:
        raise ValueError("Book not found")

def handle_book_request(isbn):
    #..... YOUR CODE STARTS HERE .....
    
    try: 
        book = get_book_details(isbn)
        return f"Book found: {book['title']} by {book['author']}. Price: {book['price']}, Quantity: {book['quantity']}"
    except ValueError: 
        return "Book not found"
    #..... YOUR CODE ENDS HERE .....

isbn = input()
response = handle_book_request(isbn)
print(response)