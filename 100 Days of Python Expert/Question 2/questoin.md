You are required to implement a Python program to handle HTTP methods: GET, POST, PUT, and DELETE. Your program should perform different actions based on the HTTP method received.

Input:

The input consists of the following:

HTTP method (GET, POST, PUT, or DELETE).
Data payload (for POST and PUT methods).

Output:

The output is the result of the action performed based on the HTTP method:

For GET method: Print "Requested resource data"
For POST method: Print "Resource created successfully: {payload}"
For PUT method: Print "Resource updated successfully: {payload}"
For DELETE method: Print "Resource deleted successfully"

Sample Input:

POST
{"name": "John", "age": 25}

Sample Output:

Resource created successfully: {"name": "John", "age": 25}