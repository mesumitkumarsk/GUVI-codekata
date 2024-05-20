You are organizing a marriage function and you have a list of tasks to be done. Each task has a time duration. You want to keep track of the total time taken by all tasks. Write a Python class MarriageFunction with a class method do_task that simulates doing a task and keeps track of the total time taken by all tasks.

Input:

task: a tuple. The first element is the task name (a string), and the second element is the task duration in seconds (an integer).
Output:

The function should print the task name and the time taken by the task in the format: f"{task[0]} took {round(end - start, 2)} seconds
Sample Input:

[("Decorating the hall", 2)]

Sample Output:

Decorating the hall took 2.0 seconds

Explanation:

The class MarriageFunction has a class method do_task which simulates doing a task by sleeping for the duration of the task. The method adds the time taken by the task to the total_duration class variable and prints the task name and the time taken by the task. This demonstrates how class variables can be used to keep track of state across multiple method calls. In the context of organizing a marriage function, this can be useful to keep track of how long all tasks take in total.

