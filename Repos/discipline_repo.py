from Domain.discipline import Disciplines
import random
from Repos.Repo_vector import Repository


class DisciplineRepo:
    def __init__(self, disciplines=None):

        self._discipline_list = Repository(list())


    @property
    def discipline_list(self):
        return self._discipline_list

    def get_all(self):
        '''
        :return: the discipline list
        '''
        return self._discipline_list.repository


    def add_discipline(self, discipline):
        '''
        it apends the given discipline to the discipline list
        '''

        self._discipline_list.add_item(discipline)
        #self._discipline_list.repository.append(discipline)


    def update(self, discipline_id, name):


        for discipline in self._discipline_list:
            if discipline_id == discipline.discipline.id:
                discipline.name = name



        """
        list_iterator = iter(self._discipline_list)
        while True:
            try:
                student = next(list_iterator)
            except StopIteration:
                break
            else:
                if discipline_id == student.discipline.id:
                    student.name = name

       

        :param discipline_id:
        :param name:
        :return: the function seaches the list of discipline for the given id and changes the name for the given one
        
        x = 0
        while x < len(self._discipline_list):
            if self._discipline_list[x].discipline_id == discipline_id:
                self._discipline_list[x].name = name
                x = x + 1
            else:
                x = x + 1
        """
    def remove_discipline(self, discipline_id):
        list_iterator = iter(self._discipline_list)
        while True:
            try:
                student = next(list_iterator)
            except StopIteration:
                break
            else:
                if student.student_id == discipline_id:
                    del self._discipline_list[self._discipline_list.index]
        '''

        :param discipline_id:
        :return:  removes the discipline whith the given id
        
        x = 0
        while x < len(self._discipline_list):
            if self._discipline_list[x].discipline_id == discipline_id:
                a=self._discipline_list[x]
                del self._discipline_list[x]
                return a
            else:
                x = x + 1
        '''

        # self._discipline_list = list(filter(discipline_id, self._discipline_list))
    def new(self):
        # nume = ['Maths','Info','English','Algebra']
        nume = ['Maths', 'Info', 'English', 'Algebra', 'Geography', 'Hystory', 'Arts & Crafts', 'Music', 'Sports',
                'Logic']
        self._discipline_list = Repository(list())
        x = 0
        while x < 10:
            y = random.randint(100, 999)
            y = str(y)
            stud = Disciplines(y, random.choice(nume))
            if self.find_discipline(y) == 0 and self.find_discipline_by_name(stud.name) == 0:
                self.add_discipline(stud)
                x = x + 1

    def find_discipline_by_name(self, name):
        x = 0
        the_list = self.get_all()
        while x < len(the_list):
            if the_list[x].name == name:

                return 1
            else:
                x = x + 1
        return 0

    def find_discipline(self, discipline_id):
        x = 0
        the_list = self.get_all()
        while x < len(the_list):
            if the_list[x].discipline_id == discipline_id:
                return 1
            else:
                x = x + 1
        return 0

#x = StudentRepo()
#y = Students('122343', 'ana')
#x.add_student(y)

def test_init_disciplines():

    disciplinesa = [Disciplines('12375', 'maths'), Disciplines('155624', 'fghX'), Disciplines('12565', 'Yzdfg')]

    repo = DisciplineRepo(disciplinesa)
    assert len(repo.discipline_list) == 3
    return repo


def test_add_disciplines():
    repo = test_init_disciplines()
    repo.add_discipline(Disciplines('1223', 'Ana'))
    assert len(repo.discipline_list) == 4

def test_remove_disciplines():
    repo = test_init_disciplines()
    repo.remove_discipline('12375')
    assert len(repo.discipline_list) == 2



#test_init_disciplines()
#test_add_disciplines()
#test_remove_disciplines()

