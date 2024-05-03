import sys

def get_ints(): 
    return map(int, sys.stdin.readline().split())

for _ in range(int(input())):
    lst = list(get_ints())
    
    #..... YOUR CODE STARTS HERE .....
    
    l,r,m = lst[0], lst[1], lst[2]
    for i in range(l,r+1):
        x1 = m%i 
        x2 = i - (m%i)
        if i<=m and x1 <= (r-l):
            a = i 
            b = r 
            c = r-x1
            i = r+2 
            break 
        elif x2 <= (r-l):
            a = i 
            b = r-x2 
            c=r 
            i = r+2 
            break 
    print(a,end=" ")
    print(b, end= " ") 
    
    print(c)
    
    #..... YOUR CODE ENDS HERE .....