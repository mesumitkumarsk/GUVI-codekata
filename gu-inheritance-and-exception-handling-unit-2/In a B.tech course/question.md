In a B.Tech course, there are several subjects, each with a different method of evaluation. Some subjects have lab work, some have project work, and some have only theory exams. Define an interface Subject with the methods has_lab(), has_project(), and get_theory_marks(). Then, define three classes LabSubject, ProjectSubject, and TheorySubject that implement this interface according to the following rules:

LabSubject returns True for has_lab(), False for has_project(), and a fixed score of 70 for get_theory_marks().
ProjectSubject returns False for has_lab(), True for has_project(), and a fixed score of 80 for get_theory_marks().
TheorySubject returns False for both has_lab() and has_project(), and a fixed score of 90 for get_theory_marks().
Sample Input:

LabSubject().has_lab()
ProjectSubject().has_project()
TheorySubject().get_theory_marks()

Sample Output:

True
True
90

Explanation:

The LabSubject class returns True for has_lab(), indicating that the subject has lab work. The ProjectSubject class returns True for has_project(), indicating that the subject has project work. The TheorySubject class returns 90 for get_theory_marks(), indicating that the theory marks for the subject are 90.