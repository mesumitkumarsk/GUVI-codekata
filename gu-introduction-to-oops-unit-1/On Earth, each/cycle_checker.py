class CycleChecker:
    def __init__(self, f):
        self.f = f
        self.n = len(f)

    def check_cycle(self):
        #..... YOUR CODE STARTS HERE .....

        for i in range(self.n):
            a = i 
            b = self.f[i]-1
            c = self.f[b]-1
            d = self.f[c]-1
            
            if d == a and a!= b and b!=c and c!=d:
                return "YES"
        return "NO"

        #..... YOUR CODE ENDS HERE .....        
 
if __name__ == "__main__":
    n = int(input())
    f = list(map(int, input().split()))

    #..... YOUR CODE STARTS HERE .....

    cycle_checker = CycleChecker(f)
    result = cycle_checker.check_cycle()
    print(result)

    #..... YOUR CODE ENDS HERE .....
