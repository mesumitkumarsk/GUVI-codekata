# GUVI - Codekata

This repository contains solutions for **GUVI Courses** questions available on the Codekata platform hosted by guvi.com. Specifically tailored for students at **Galgotias University**, the repository covers topics, including 
<br>1. **GU - Introduction To Oops: Unit 1** 
<br>2. **GI - Inheritance And Exception Handling: Unit 2**
<br>3. **GU - Functional Programming: Unit 3**
<br>
<br> --> **Assignment Question of the following courses : -**
<br>1. **Python Zero to Hero Assignments**
<br>2. **100 Days of Python Beginner Assignments**
<br>3. **100 Days of Python Intermediate Assignments**
<br>4. **100 Days of Python Advance Assignments**
<br>5. **100 Days of Python Expert Assignments**

<h3>Repository Structure:</h3>
Each question is organized within its dedicated folder. The folder names are based on initial words from the question, ensuring easy navigation. Inside each folder, you’ll find two essential files:

<h3>Question File (.md):</h3>
&emsp; Contains the full question, providing context and details.

<h3>Solution File (.py):</h3>
&emsp; Contains the actual solution code for the respective question.


CREATE TABLE Persons (
    PersonID int,
    LastName varchar(255),
    FirstName varchar(255),
    Address varchar(255),
    City varchar(255)
);

INSERT INTO Persons VALUES (101, 'Bob', 'Alice', 'Sector', 'UP');
INSERT INTO Persons VALUES (102, 'Kumar', 'Sachin', 'Sector One', 'UP');
INSERT INTO Persons VALUES (103, 'Bhatt', 'Mahesh', 'Sector Two', 'UP'); 

SELECT * FROM Persons;

ALTER TABLE Persons ADD Email varchar (255);
ALTER TABLE Persons RENAME Email to Personal;
ALTER TABLE Persons DROP COLUMN Personal;


 UPDATE Persons SET LastName= 'Albert' , FirstName='Gilbert' WHERE PersonID=101;


