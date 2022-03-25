from Domain.student import Students
from Repos.Repo_vector import Repository
from Repos.student_repo import StudentRepo


class StudentsTextFileRepository(StudentRepo):  ###################################################################################

    def __init__(self, students=None):
        # student repo has a list of all students
        super().__init__()
        self.read_text_file()

    def add_student(self, student):
        super().add_student(student)
        self.write_text_file()

    def update(self, student_id, name):
        super().update(student_id, name)
        self.write_text_file()

    def remove_student(self, student_id):
        super().remove_student(student_id)
        self.write_text_file()

    def write_text_file(self):
        f = open("students.txt", "w")
        try:
            for p in self._student_list:
                person_str = str(p.student_id) + ";" + p.name + "\n"
                f.write(person_str)
            f.close()
        except Exception as e:
            print("An error occurred -" + str(e))

    def read_text_file(self):
        #self._student_list = []
        self._student_list = Repository(list())
        try:
            f = open("students.txt", "r")
            line = f.readline().strip()
            while len(line) > 0:
                line = line.split(";")
                a = Students(line[0], str(line[1]))
                self.add_student(a)
                line = f.readline().strip()
            f.close()
        except IOError as e:
            """
                Here we 'log' the error, and throw it to the outer layers 
            """
            print("An error occured - " + str(e))
            raise e
        return self._student_list
