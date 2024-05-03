class ItemNotFoundError(Exception):
    pass

def get_stock(item):
    stock = {
        "Apples": 50,
        "Oranges": 30,
        "Grapes": 0,
    }
    if item in stock:
        return stock[item]
    else:
        raise ItemNotFoundError("Item not found")

def handle_stock_request(item):
    #..... YOUR CODE STARTS HERE .....
    
    try: 
        stock = get_stock(item)
        return f"Stock for {item}: {stock}"
    except ItemNotFounderror: 
        return "Item not found"
    
    #..... YOUR CODE ENDS HERE .....

user_input = input()

print(handle_stock_request(user_input))