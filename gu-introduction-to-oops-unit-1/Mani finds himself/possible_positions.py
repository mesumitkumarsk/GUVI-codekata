n,a,b = map(int, input().split())

#..... YOUR CODE STARTS HERE .....

max_behind = n - a - 1 

possible_positions = min(max_behind, b)

print(possible_positions+1)

#..... YOUR CODE ENDS HERE .....