class NumberProcessor:
    def __init__(self, l):
        self.l = l
        self.s = 0
        self.odd = 0
        self.nz = 0

    def process_numbers(self):
        #..... YOUR CODE STARTS HERE .....

        self.l.sort()
        pay = 0 
        for i in self.l: 
            if int(i)<0: 
                pay = (-1*int(i))
            elif int(i) > 0: 
                pay+=int(i)
                
        b = []
        for i in self.l: 
            if i == "0": 
                b.append(False)
            else: 
                b.append(True)
        if True not in b: 
            pay = len(self.l)
        return pay

       #..... YOUR CODE ENDS HERE .....        
  

if __name__ == "__main__":
    n = int(input())
    l = str(input()).split(" ")

    number_processor = NumberProcessor(l)
    result = number_processor.process_numbers()
    print(result)
