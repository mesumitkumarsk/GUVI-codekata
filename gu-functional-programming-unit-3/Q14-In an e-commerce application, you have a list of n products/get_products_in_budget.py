import re

def get_products_in_budget(budget, products):
    #..... YOUR CODE STARTS HERE .....
    
    sorted_products = sorted(products, key=lambda x : x[1])
    
    current_total = 0 
    
    for product in sorted_products: 
        product_id, price = product 
        if current_total + price <= budget: 
            yield product 
            current_total += price 
        else: 
            break
    
    #..... YOUR CODE ENDS HERE .....
        
def replace_non_alphanumeric(text, replacement=''):
    return re.sub(r'[^a-zA-Z0-9,]', replacement, text)
        
def clean_input(value):
    value = replace_non_alphanumeric(value).split(',')
    
    id, price = list(map(lambda x: x.strip(), value))
    
    return (id, int(price))
    
if __name__ == "__main__":
    budget = int(input())
    products = input()
    
    products = list(map(clean_input, products.strip().replace('[', '').replace(']', '').split('),')))
    
    for product in get_products_in_budget(budget, products):
        print(product)