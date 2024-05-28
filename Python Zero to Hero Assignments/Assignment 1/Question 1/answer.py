def gcd(num1, num2):
    
    if num1 < 0:
        num1 = -num1
    if num2 < 0:
        num2 = -num2
    while num2:
        num1, num2 = num2, num1 % num2
    return num1

num1, num2 = map(int, input().split())
print(gcd(num1, num2))