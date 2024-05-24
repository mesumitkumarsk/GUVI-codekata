class Student:
    def __init__(self, name, scores):
        self._name = name  # protected attribute
        self.__scores = scores  # private attribute

    def calculate_average(self):
        return sum(self.__scores) / len(self.__scores)

    def get_name(self):  # public method to access protected attribute
        return self._name


class TopStudentFinder:
    def __init__(self):
        self.max_avg = -1.0
        self.top_student = ""

    def find_top_student(self, students):
        #..... YOUR CODE STARTS HERE .....

        for student in students: 
            avg = student.calculate_average()
            if avg > self.max_avg: 
                self.max_avg = avg
                self.top_student = student.get_name()

        #..... YOUR CODE ENDS HERE .....
    def get_top_student(self):
        return self.top_student


if __name__ == "__main__":
    n = int(input())
    students_data = []

    for _ in range(n):
        student_info = input().split()
        name = student_info[0]
        scores = list(map(int, student_info[1:]))
        students_data.append(Student(name, scores))

    #..... YOUR CODE STARTS HERE .....

top_student_finder = TopStudentFinder()
top_student_finder.find_top_student(students_data)
print(top_student_finder.get_top_student())

    #..... YOUR CODE ENDS HERE .....
