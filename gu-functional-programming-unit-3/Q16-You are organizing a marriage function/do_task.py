import time
import re

class MarriageFunction:
    total_duration = 0

    @classmethod
    def do_task(cls, task):
        #..... YOUR CODE STARTS HERE .....
    
        task_name, duration = task 
        start = time.time()
        time.sleep(duration)
        end = time.time()
        elasped_time = end - start
        cls.total_duration += elasped_time
        print(f"{task_name} took {round(elasped_time,2)} seconds")
    
        #..... YOUR CODE ENDS HERE .....
    
def replace_non_alphanumeric(text, replacement=''):
    return re.sub(r'[^a-zA-Z0-9, ]', replacement, text)
        
def clean_input(value):
    value = replace_non_alphanumeric(value).split(',')
    
    id, price = list(map(lambda x: x.strip(), value))
    
    return (id, int(price))
    
if __name__ == "__main__":
    tasks = input()
    
    tasks = list(map(clean_input, tasks.strip().replace('[', '').replace(']', '').split('),')))
    
    for task in tasks:
       MarriageFunction.do_task(task)