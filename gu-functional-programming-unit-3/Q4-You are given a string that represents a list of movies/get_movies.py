import re

def get_movies(data):
    #..... YOUR CODE STARTS HERE .....
    
    pattern = r'\s*([^,(]+) \((\d{4})\)'
    
    return re.findall(pattern, data)
   
    
    #..... YOUR CODE ENDS HERE .....
    
if __name__ == "__main__":
    data = input().strip()
    print(get_movies(data))