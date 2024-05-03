class Player:
    def __init__(self, name, goals=0):
        #..... YOUR CODE STARTS HERE .....
    
        self._name=name
        self._goals = 0 
        self.goals = goals
    
    @property
    def goals(self):
        return self._goals
    
        #..... YOUR CODE ENDS HERE .....

    #..... YOUR CODE STARTS HERE .....
    
    @goals.setter
    def goals(self,value):
        try: 
            value = int(value)
            if value < 0: 
                self._goals=0 
            else: 
                self._goals = value 
                
        except ValueError: 
            self._goals=0
            
    @property 
    def name(self):
        return self._name
        
    
    #..... YOUR CODE ENDS HERE .....
            
def clean_input(value):
    return str(value.strip())
    
name, goal = map(clean_input, input().strip().split(","))
next_goal = input()

player = Player(name, goal)
print(name)
print(player.goals)
player.goals =next_goal
print(player.goals)