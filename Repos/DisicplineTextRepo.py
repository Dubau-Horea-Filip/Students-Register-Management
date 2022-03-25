from Domain.discipline import Disciplines
from Repos.discipline_repo import DisciplineRepo


class DisciplinesTextFileRepository(DisciplineRepo):  ######################################################################
    def __init__(self, disciplines=None):
        super().__init__()
        self._discipline_list = []
        self.read_text_file()

    def update(self, discipline_id, name):
        super().update(discipline_id, name)
        self.write_text_file()

    def add_discipline(self, discipline):
        super().add_discipline(discipline)
        self.write_text_file()

    def remove_discipline(self, discipline_id):
         super().remove_discipline(discipline_id)
         self.write_text_file()


    def write_text_file(self):
        f = open("disciplines.txt", "w")
        try:
            for p in self._discipline_list:
                person_str = str(p.discipline_id) + ";" + p.name + "\n"
                f.write(person_str)
            f.close()
        except Exception as e:
            print("An error occurred -" + str(e))

    def read_text_file(self):
        self._discipline_list = []
        try:
            f = open("disciplines.txt", "r")
            line = f.readline().strip()
            while len(line) > 0:
                line = line.split(";")
                a = Disciplines(line[0], str(line[1]))
                self._discipline_list.append(a)
                line = f.readline().strip()
            f.close()
        except IOError as e:
            """
                Here we 'log' the error, and throw it to the outer layers 
            """
            print("An error occured - " + str(e))
            raise e
        return self._discipline_list

