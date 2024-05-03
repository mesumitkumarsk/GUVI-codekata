Consider an e-commerce application that uses a class hierarchy to represent different types of products. We have a base class Product and two subclasses Book and Electronics. Both Book and Electronics classes override a method get_details() from the Product class. Now, we have a new product type EBook that is both a Book and an Electronics. The EBook class inherits from both Book and Electronics.

Write a Python function mro_sequence(cls) that takes a class cls as input and returns the Method Resolution Order (MRO) for that class as a list of class names.

Sample Input:

EBook

Sample Output:

['EBook', 'Book', 'Electronics', 'Product', 'object']

Explanation:

In Python, the Method Resolution Order (MRO) is the order in which the base classes are searched when executing a method. Python uses an algorithm called C3 Linearization, or just C3, to compute this order. In the given example, the MRO for class EBook is EBook -> Book -> Electronics -> Product -> object.

Constraints:

The input class cls is a valid Python class.
The class hierarchy can have multiple levels of inheritance but does not contain any circular inheritance.