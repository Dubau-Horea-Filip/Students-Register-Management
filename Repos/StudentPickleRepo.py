from Repos.student_repo import StudentRepo
import pickle


class StudentsPickleFileRepo(StudentRepo):
    def __init__(self, students=None):
        super().__init__()

        self.read_binary_file()
        #self.new()
        #self.write_binary_file()



    def add_student(self, student):
        super().add_student(student)
        self.write_binary_file()

    def update(self, student_id, name):
        super().update(student_id, name)
        self.write_binary_file()

    def remove_student(self, student_id):
        super().remove_student(student_id)
        self.write_binary_file()

    def new(self):
        super().new()


    def write_binary_file(self):
        f = open("students.pickle", "wb")

        pickle.dump(self.students_list, f)

        f.close()


    def read_binary_file(self):

        try:
            f = open("students.pickle", "rb")
            v = []
            v = pickle.load(f)
            for i in v:
                self.add_student(i)

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
