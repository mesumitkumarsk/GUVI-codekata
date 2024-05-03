Design a Python program that uses single level inheritance to model a school. The school has two types of people: students and teachers. Both students and teachers have a name and an age. However, a student also has a department, while a teacher has a subject they teach.

Create classes to represent both a student and a teacher, and use inheritance to avoid code duplication. Write a method in each class to print the details of the student or teacher.

Sample Input:

Ravi Kumar, 20, Computer Science
Dr. Srinivasan, 45, Data Structures and Algorithms

Sample Output:

Student: Ravi Kumar, Age: 20, Department: Computer Science
Teacher: Dr. Srinivasan, Age: 45, Subject: Data Structures and Algorithms

Explanation:

In the sample output, each line represents the details of a person in the school:

The first line is the details of a student. It's Ravi Kumar who is 20 years old and studying Computer Science.
The second line is the details of a teacher. It's Dr. Srinivasan who is 45 years old and teaches Data Structures and Algorithms.
These details are printed by calling the print_details() method of each person object. The method is defined in each class and prints the details specific to that person.

This is an example of single level inheritance, where the Student and Teacher classes inherit from a common base class (Person). The base class defines properties and methods common to all people (like name and age), while the derived classes add properties and methods specific to students and teachers (like grade and subject).

Constraints:

The name of the student or teacher is a string and can contain any printable ASCII characters.
The age of the student or teacher is an integer and can be any positive integer.
The department of the student is a string and can contain any printable ASCII characters.
The subject of the teacher is a string and can contain any printable ASCII characters.