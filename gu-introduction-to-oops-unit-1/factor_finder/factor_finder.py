class FactorFinder:
    def __init__(self, n):
        self.n = n

    def find_factors(self):
        def backtrack(remaining, start, path, result):
            #..... YOUR CODE STARTS HERE .....

            if(remaining ==1):
                result.append(path)
                return
            
            for i in range(start, self.n+1):
                if remaining%i!=0:
                    continue
                if i == self.n: 
                    backtrack(remaining//i,i,path+[1,i],result)
                    continue
                backtrack(remaining//i,i,path+[i],result)

            #..... YOUR CODE ENDS HERE .....

        result = []
        backtrack(self.n, 2, [], result)
        return result

if __name__ == '__main__':
    n = int(input())
    factor_finder = FactorFinder(n)
    print(factor_finder.find_factors())
