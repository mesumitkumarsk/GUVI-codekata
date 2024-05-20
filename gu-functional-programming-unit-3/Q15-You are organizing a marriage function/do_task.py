import time

def time_it(func):
    #..... YOUR CODE STARTS HERE .....
    
    def wrapper(task): 
        start = time.time()
        result = func(task) 
        end = time.time()
        print(f"{task[0]} took {round(end - start, 2)} seconds")
        return result
        
    return wrapper
    
    #..... YOUR CODE ENDS HERE .....

@time_it
def do_task(task):
    #..... YOUR CODE STARTS HERE .....
    
    time.sleep(task[1])
    
    #..... YOUR CODE ENDS HERE .....
    
    
if __name__ == "__main__":
    task_name, duration = list(map(lambda x: x.strip(), input().strip().split(',')))
    task = [task_name, int(duration)]
    
    do_task(task)