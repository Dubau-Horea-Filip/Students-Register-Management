from Domain.grade import Grades
from Repos.grade_repo import GradeRepo




class GradeTextFileRepository(GradeRepo):
    def __init__(self):
        super().__init__()
        self.read_text_file()

    def add_grade(self, grade):
        super().add_grade(grade)
        self.write_text_file()

    def remove_student(self, student_id):
        super().remove_student(student_id)
        self.write_text_file()

    def remove_student_and_gives_list(self, student_id):
        super().remove_student_and_gives_list(student_id)
        self.write_text_file()

    def remove_student_and_gives_list_2(self, student_id):
        super().remove_student_and_gives_list_2(student_id)
        self.write_text_file()

    def remove_discipline_and_gives_list(self, discipline_id):
        super().remove_discipline_and_gives_list(discipline_id)
        self.write_text_file()

    def remove_discipline(self, discipline_id):
        super().remove_discipline(discipline_id)
        self.write_text_file()

    def write_text_file(self):
        f = open("grades.txt", "w")
        try:
            for p in self._grade_list:
                person_str = str(p.discipline_id) + ";" + str(p.student_id) + ";" + str(p.grade) + "\n"
                f.write(person_str)
            f.close()
        except Exception as e:
            print("An error occurred -" + str(e))

    def read_text_file(self):


            f = open("grades.txt", "r")
            line = f.readline().strip()
            while len(line) > 0:
                line = line.split(";")
                a = Grades(line[0], line[1],line[2])
                self._grade_list.append(a)
                line = f.readline().strip()
            f.close()
