Consider an election scenario where we have different roles such as Citizen, Politician, and PublicServant. Both Politician and PublicServant are subclasses of Citizen. Now, we have a new role Mayor who is both a Politician and a PublicServant. The Mayor class inherits from both Politician and PublicServant.

Each of these classes has a method role_duties() that describes the duties of the role. However, when a Mayor object calls this method, which method should it execute? This is known as the Diamond Problem.

Write a Python function mro_sequence(cls) that takes a class cls as input and returns the Method Resolution Order (MRO) for that class as a list of class names.

Sample Input:

Mayor

Sample Output:

['Mayor', 'Politician', 'PublicServant', 'Citizen', 'object']

Explanation:

In Python, the Method Resolution Order (MRO) is the order in which the base classes are searched when executing a method. Python uses an algorithm called C3 Linearization, or just C3, to compute this order. In the given example, the MRO for class Mayor is Mayor -> Politician -> PublicServant -> Citizen -> object. This means that if a Mayor object calls the role_duties() method, it will first look for this method in the Mayor class. If it doesn't find it there, it will look in the Politician class, then in the PublicServant class, and finally in the Citizen class.

Constraints:

The input class cls is a valid Python class.
The class hierarchy can have multiple levels of inheritance but does not contain any circular inheritance.