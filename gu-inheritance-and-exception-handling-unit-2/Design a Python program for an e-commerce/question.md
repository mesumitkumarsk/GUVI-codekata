Design a Python program for an e-commerce platform that sells products. Each product on the platform has a name, price, and seller. There are two types of products: new and used. Used products have an additional attribute: condition.

Create classes to represent a Product, NewProduct, and UsedProduct. Use inheritance and the super() function to avoid code duplication. Write a method in each class to print the details of the product.

Sample Input:

Laptop, 1200.99, ElectronicsHub
Smartphone, 450.50, TechResell, Good

Sample Output:

New Product: Laptop, Price: $1200.99, Seller: ElectronicsHub
Used Product: Smartphone, Price: $450.50, Seller: TechResell, Condition: Good

Explanation:

In the sample output, each line represents the details of a product:

The first line is the details of a new product. It's a Laptop with a price of $1200.99 sold by ElectronicsHub.
The second line is the details of a used product. It's a Smartphone with a price of $450.50 sold by TechResell and its condition is Good.
These details are printed by calling the print_details() method of each product object. The method is defined in each class and prints the details specific to that product.

This is an example of single level inheritance, where the NewProduct and UsedProduct classes inherit from a common base class (Product). The base class defines properties and methods common to all products (like name, price, and seller), while the derived classes add properties and methods specific to new and used products. The super() function is used to call a method in the parent class from the child class.

Constraints:

The name of the product and the seller is a string and can contain any printable ASCII characters.
The price of the product is a float and can be any positive number.
The condition of the used product is a string and can contain any printable ASCII characters.