import sys
from collections import deque, defaultdict

I = sys.stdin.readline

def ii():
    return int(I().strip())

def li():
    return list(map(int, I().strip().split()))

def mi():
    return map(int, I().strip().split())

def main():
    n, k = mi()
    arr = li()
    
    #..... YOUR CODE STARTS HERE .....
    
    maxlen = 0 
    s = sum(arr)
    if s<=k:
        print(n)
    else: 
        curr = 0 
        j = 0 
        for i in range(n):
            curr+=arr[i]
            while curr>k: 
                curr-=arr[j]
                j+=1
            maxlen=max(maxlen,i-j+1)
        print(maxlen)
    
    #..... YOUR CODE ENDS HERE .....

if __name__ == '__main__':
    main()