def get_product_details(product_id):
    products = {
        "123456": {"name": "Wireless Mouse", "category": "Electronics", "price": 500, "stock": 10},
        "789012": {"name": "Running Shoes", "category": "Sports", "price": 600, "stock": 5},
        "345678": {"name": "Coffee Maker", "category": "Home Appliances", "price": 700, "stock": 2},
    }
    if product_id in products:
        return products[product_id]
    else:
        raise Exception("Product not found")

def handle_product_request(product_id):
    #..... YOUR CODE STARTS HERE .....
    
    print("Request handled")
    try: 
        product = get_product_details(product_id)
        return f"Product found: {product['name']}, Category: {product['category']}, Price: {product['price']}, Stock: {product['stock']}"
    except: 
        return "Product not found"
    
    
    #..... YOUR CODE ENDS HERE .....

# Get input from the user
user_input = input()

# Call the handle_product_request function with user input
result = handle_product_request(user_input)
print(result)