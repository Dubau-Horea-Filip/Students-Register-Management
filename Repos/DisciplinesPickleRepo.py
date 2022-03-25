
from Repos.discipline_repo import DisciplineRepo
import pickle

class DisciplinesPickleRepo(DisciplineRepo):
    def __init__(self, disciplines=None):
        super().__init__()
        self._discipline_list = []
        #self.new()
        #self.write_binary_file()

        self.read_binary_file()

    def add_all(self, discipline_list):
        super().add_all(discipline_list)
        self.write_binary_file()

    def update(self, discipline_id, name):
        super().update(discipline_id, name)
        self.write_binary_file()

    def add_discipline(self, discipline):
        super().add_discipline(discipline)
        self.write_binary_file()

    def remove_discipline(self, discipline_id):
         super().remove_discipline(discipline_id)
         self.write_binary_file()


    def new(self):
        super().new()

    def write_binary_file(self):
        f = open("disciplines.pickle", "wb")
        pickle.dump(self._discipline_list, f)
        f.close()

    def read_binary_file(self):
        result = []
        try:
            f = open("disciplines.pickle", "rb")
            v = []
            v = pickle.load(f)
            for i in v:
                self._discipline_list.append(i)

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

