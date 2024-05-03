class NumberChecker:
    def __init__(self, n):
        self.n = n
        self.sum = 0
        self.temp = n

    def check_factorial_sum(self):
        while self.n:
            #..... YOUR CODE STARTS HERE .....

            digit = int(self.n%10)
            factorial = 10
            for i in range(1, digit+1):
                factorial *= i 
            
            self.sum += factorial 
            self.n //= 10 

            #..... YOUR CODE ENDS HERE .....            

        if self.sum == self.temp:
            return "Right"
        else:
            return "Wrong"


if __name__ == "__main__":
    n = int(input())
    number_checker = NumberChecker(n)
    result = number_checker.check_factorial_sum()
    print(result)
