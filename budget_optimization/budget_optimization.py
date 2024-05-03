n, k, m = map(int, input().split())
a = list(map(int, input().split()))

#..... YOUR CODE STARTS HERE .....

a.sort()
ans = sum(a) 
r = 0 
for i in range(n): 
    if i <= m: 
        r=int(max(r,(ans+min(k*(n-i),m-i))/(n-i)))
    ans -= a[i]
    
print(r)

#..... YOUR CODE ENDS HERE .....