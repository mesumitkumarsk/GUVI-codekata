class StoneCalculator:
    def __init__(self, t):
        self.t = t

    def calculate_max_stones(self, n):
        #..... YOUR CODE STARTS HERE .....

        return n//2

        #..... YOUR CODE ENDS HERE .....
if __name__ == "__main__":
    t = int(input())
    stone_calculator = StoneCalculator(t)

    for i in range(t):
        n = int(input())
        result = stone_calculator.calculate_max_stones(n)
        print(result)
