import json
from io import StringIO

def passed_students(scores):
    #..... YOUR CODE STARTS HERE .....
    
    passing_scores = list(filter(lambda x: x >= 60, scores))
    return passing_scores
    
    #..... YOUR CODE ENDS HERE .....

if __name__ == "__main__":
    scores = json.load(StringIO(input().strip()))
    passed_students = passed_students(scores)
    
    print(passed_students)