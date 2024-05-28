You are given a JSON string representing a list of dictionaries where each dictionary contains information about a person. Your task is to write a Python program to extract the names of all the people whose age is greater than or equal to 30 and whose nationality is "USA".

Input:

The input consists of a JSON string representing a list of dictionaries. Each dictionary contains the following keys: "name", "age", and "nationality". Each key-value pair is separated by a comma. The entire JSON string is enclosed in square brackets.

Output:

Print the names of all the people whose age is greater than or equal to 30 and whose nationality is "USA", separated by a space. If there are no such people, print "No matching people found".

Sample Input:

[{"name": "Alice", "age": 25, "nationality": "USA"}, {"name": "Bob", "age": 40, "nationality": "UK"}, {"name": "Charlie", "age": 35, "nationality": "USA"}, {"name": "David", "age": 30, "nationality": "Canada"}]

Sample Output:

Charlie