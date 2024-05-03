Design a Python program that uses multiple inheritance to model an e-commerce platform. The platform sells two types of products: physical products and digital products. Both types of products have a name and a price. However, a physical product also has a shipping weight, while a digital product has a file size.

Create classes to represent both types of products and use multiple inheritance to create a third class that represents a product that is both physical and digital (for example, a video game that can be purchased as a physical disc or downloaded digitally).

Write a method in each class to print the details of the product.

Sample Input:

Book, 9.99, 1.0
Ebook, 6.99, 2
Video Game, 59.99, 0.2, 25

Sample Output:

Physical Product: Book, Price: $9.99, Shipping Weight: 1.0 kg
Digital Product: Ebook, Price: $6.99, File Size: 2 MB
Hybrid Product: Video Game, Price: $59.99, Shipping Weight: 0.2 kg, File Size: 25 GB

Explanation:

In the sample output, each line represents the details of a product:

The first line is the details of a physical product. It’s a book with a price of $9.99 and a shipping weight of 1.0 kg.
The second line is the details of a digital product. It’s an Ebook with a price of $6.99 and a file size of 2 MB.
The third line is the details of a hybrid product. It’s a video game with a price of $59.99, a shipping weight of 0.2 kg, and a file size of 25 GB.
These details are printed by calling the print_details() method of each product object. The method is defined in each class and prints the details specific to that class. For the HybridProduct class, which inherits from both PhysicalProduct and DigitalProduct, the print_details() method prints the details of both the physical and digital aspects of the product.