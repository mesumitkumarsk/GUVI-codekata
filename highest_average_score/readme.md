Lucas, a university student, is working on a project where he needs to process a set of student records. He is given a list of students where each record contains the student's name and marks in three subjects: Math, Physics, Biology. Each subject's mark is within the range 0-100. He needs to return the name of the student with the highest average score.

If there is more than one student who has the highest average score, Lucas needs to return the first student in the list.

Input:

The first line contains an integer 'n' (1 <= n <= 1000) - representing the number of students.
The 'n' following lines each contain a string and three space-separated integers.
Output:

Print the name of the student who has the highest average score.
Sample Input:

5
John 85 90 82
Alice 90 91 92
Bob 80 79 81
Lucas 88 90 92
Maria 90 91 90
Sample Output:

Alice
Note: The five students' average scores are as follows:

John's average is 85.67
Alice's average is 91
Bob's average is 80
Lucas's average is 90
Maria's average is 90.33
Alice has the highest average score and showcases the best performance among all students.

