class Citizen:
    def role_duties(self):
        return "Citizen duties"

class Politician(Citizen):
    def role_duties(self):
        return "Politician duties"

class PublicServant(Citizen):
    def role_duties(self):
        return "Public servant duties"

class Mayor(Politician, PublicServant):
    def role_duties(self):
        return "Mayor duties"

class Voter(Citizen):
    def role_duties(self):
        return "Voter duties"

class Candidate(Citizen):
    def role_duties(self):
        return "Candidate duties"
        
class ElectedOfficial(Voter, Candidate):
    def role_duties(self):
        return "Elected official duties"


class Activist(Citizen):
    def role_duties(self):
        return "Activist duties"

class ActivistPolitician(Activist, Politician):
    def role_duties(self):
        return "Activist politician duties"

class Worker(Citizen):
    def role_duties(self):
        return "Worker duties"

class WorkingPolitician(Worker, Politician):
    def role_duties(self):
        return "Working politician duties"

def mro_sequence(cls):
    #..... YOUR CODE STARTS HERE .....
    
    return[c.__name__ for c in cls.mro()]
    
    #..... YOUR CODE ENDS HERE .....

class_name = input()

cls = globals()[class_name]

# Print the MRO sequence
print(mro_sequence(cls))