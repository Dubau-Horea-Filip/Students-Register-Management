from Repos.discipline_repo import *
# Discipline: discipline_id, name
from service.undo_service import *
import random


class DisciplineService:
    def __init__(self, discipline_repo,undo_service):

        self._repo = discipline_repo
        self._undo_service = undo_service

    def update_discipline(self, discipline_id, name):
        self._repo.update(discipline_id, name)

    def new(self):

        self._repo._discipline_list.repository = []
        self._repo._discipline_list.index = -1

        # nume = ['Maths','Info','English','Algebra']
        nume = ['Maths', 'Info', 'English', 'Algebra', 'Geography', 'Hystory', 'Arts & Crafts', 'Music', 'Sports',
                'Logic']
        x = 0
        while  len(self._repo._discipline_list) < 10:
            y = random.randint(100, 999)
            y = str(y)
            stud = Disciplines(y, random.choice(nume))
            if self.find_discipline(y) == 0 and self.find_discipline_by_name(stud.name) == 0:
                self._repo.add_discipline(stud)
                x = x + 1

    def create_discipline(self, discipline_id, name):
        '''

        :param discipline_id:
        :param name:
        :return:

        '''
        if self.find_discipline(discipline_id) == 1:
            raise ValueError('discipline already exists')
        if self.find_discipline_by_name(name) == 1:
            raise ValueError('discipline already exists')
        discipline_id = str(discipline_id)
        if self.find_discipline(discipline_id) == 0 and self.find_discipline_by_name(name) == 0:
            a = Disciplines(discipline_id, name)

            self._repo.add_discipline(a)

            fun_undo = FunctionCall(self.remove_discipline, discipline_id)
            fun_redo = FunctionCall(self.create_discipline_wundo, discipline_id, name)
            self._undo_service.record(Operation(fun_undo, fun_redo))

    def create_discipline_wundo(self, discipline_id, name):
        a = Disciplines(discipline_id, name)
        self._repo.add_discipline(a)

    def remove_discipline(self, discipline_id):
       dis =  self._repo.remove_discipline(discipline_id)
       '''
       fun_undo = FunctionCall(self.create_discipline_wundo, dis.discipline_id, dis.name)
       fun_redo = FunctionCall(self.remove_discipline_wundo, discipline_id)
       self._undo_service.record(Operation(fun_undo, fun_redo))
       '''


    def remove_discipline_wundo(self, discipline_id):
        dis = self._repo.remove_discipline(discipline_id)

    def find_discipline(self, discipline_id):
        x = 0

        the_list = self.get_all()
        while x < len(the_list):
            if the_list[x].discipline_id == discipline_id:
                return 1
            else:
                x = x + 1
        return 0

    def find_discipline_name_by_id(self, discipline_id):
        x = 0
        the_list = self.get_all()
        while x < len(the_list):
            if the_list[x].discipline_id == discipline_id:
                return the_list[x].name
            else:
                x = x + 1
        return 0

    def find_discipline_by_name(self, name):
        x = 0
        the_list = self._repo.get_all()
        while x < len(the_list):
            if the_list[x].name == name:

                return 1
            else:
                x = x + 1
        return 0

    def get_all(self):
        return self._repo.get_all()

    def find_discipline_name(self, name):
        ok = 0
        x = 0
        list = []
        while x < len(self._repo.discipline_list):
            y = self._repo.discipline_list[x].name
            y = str(y).lower()
            name = str(name).lower()
            if name in y:  # s1.contains(s2)
                ok = ok + 1
                list.append(self._repo._discipline_list[x])
                # print (self._repo._student_list[x])
                x = x + 1

            else:
                x = x + 1

        if ok == 0:
            return 'no discipline with the given name'
        return list

    def find_discipline_id(self, discipline_id):
        ok = 0
        x = 0
        list = []
        while x < len(self._repo._discipline_list):
            if discipline_id in self._repo._discipline_list[x].discipline_id:
                ok = ok + 1
                list.append(self._repo._discipline_list[x])
                # print (self._repo._discipline_list[x])
                x = x + 1

            else:
                x = x + 1

        if ok == 0:
            return 'no discipline with the given id'
        return list

    def find_discipline_print(self, id):
        ok = 0
        x = 0
        list = []
        while x < len(self._repo._discipline_list):
            if id == self._repo._discipline_list[x].discipline_id:

                return (self._repo._discipline_list[x])
                # print (self._repo._discipline_list[x])
                x = x + 1

            else:
                x = x + 1


