import pickle

from Repos.grade_repo import GradeRepo


class GradePicklRepo(GradeRepo):
    def __init__(self):
        super().__init__()
        self.read_binary_file()

    def add_grade(self, grade):
        super().add_grade(grade)
        self.write_binary_file()

    def remove_student(self, student_id):
        super().remove_student(student_id)
        self.write_binary_file()

    def remove_student_and_gives_list(self, student_id):
        super().remove_student_and_gives_list(student_id)
        self.write_binary_file()

    def remove_student_and_gives_list_2(self, student_id):
        super().remove_student_and_gives_list_2(student_id)
        self.write_binary_file()

    def remove_discipline_and_gives_list(self, discipline_id):
        super().remove_discipline_and_gives_list(discipline_id)
        self.write_binary_file()

    def remove_discipline(self, discipline_id):
        super().remove_discipline(discipline_id)
        self.write_binary_file()

    def write_binary_file(self):
        f = open("Grades.pickle", "wb")
        pickle.dump(self._grade_list, f)
        f.close()

    def read_binary_file(self):
        result = []
        try:
            f = open("Grades.pickle", "rb")
            v = []
            v = pickle.load(f)
            for i in v:
                self._grade_list.append(i)

        except EOFError:
            """
                This is raised if input file is empty
            """
            return []
        except IOError as e:
            """
                Here we 'log' the error, and throw it to the outer layers 
            """
            print("An error occured - " + str(e))
            raise e