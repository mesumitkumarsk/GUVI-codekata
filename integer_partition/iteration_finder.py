class Calculation:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def find_iteration(self):
        #..... YOUR CODE STARTS HERE .....

        if self.x > self.y: 
            return 1
            
        years = 0 
        while self.x <= self.y:
            self.x *= 3
            self.y *= 2 
            years += 1 
        return years

        #..... YOUR CODE ENDS HERE .....

if __name__ == "__main__":
    x, y = map(int, input().split())
    calculation = Calculation(x, y)
    result = calculation.find_iteration()
    if result is not None:
        print(result)