You are implementing a simple calculator. Write a Python class Calculator with static methods add, subtract, multiply, and divide that perform the respective operations.

Input:

num1: a float, the first number.
num2: a float, the second number.
Output:

The function should return the result of the operation.
Sample Input:

Calculator.add(5, 3)

Sample Output:

8

Explanation:

The class Calculator has static methods add, subtract, multiply, and divide which perform the respective operations. Static methods, marked with the @staticmethod decorator, don't take a self or cls parameter. This means you can't modify object state or class state within a static method. However, they're useful when you need to perform a utility function that doesn't modify the state of the object or class, like in this case where we're performing simple mathematical operations.

