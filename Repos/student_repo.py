from Domain.student import Students
from Domain.student import *
import random

from Repos.Repo_vector import Repository


class StudentRepo:
    def __init__(self, students=None):
        # self._student_list = []

        self._student_list = Repository(list())

    @property
    def students_list(self):
        return self._student_list

    def get_all(self):
        # returns the student list
        return self._student_list.repository

    def add_student(self, student):
        '''

        :param student:
        it appends the new student  to the list
        '''
        self._student_list.add_item(student)

    def update(self, student_id, name):

        list_iterator = iter(self._student_list)
        while True:
            try:
                student = next(list_iterator)
            except StopIteration:
                break
            else:
                if student_id == student.student_id:
                    student.name = name

        '''

        :param student_id:
        :param name:
        :changes the name of the given id student whith a new one from console

        x = 0
        while x < len(self._student_list):
            if self._student_list[x].student_id == student_id:
                self._student_list[x].name=name
                x=x+1
            else:
                x = x + 1
        '''

    def remove_student(self, student_id):
        list_iterator = iter(self._student_list)
        while True:
            try:
                student = next(list_iterator)
            except StopIteration:
                break
            else:
                if student.student_id == student_id:
                    del self._student_list[self._student_list.index]
        '''

        :param student_id:
        it removes the student whith the given student id from the list

        x = 0
        while x < len(self._student_list):
            if self._student_list[x].student_id == student_id:

                a=  self._student_list[x]
                del self._student_list[x]
                return a
            else:
                x = x + 1

        # self._student_list = list(filter(student_id, self._student_list))
'''

    def new(self):
        self._student_list = Repository(list())
        # generates 10 random student
        prenume = ['Andreea', 'Diana', 'Andrei', 'Vlad', 'Darius', 'George', 'Mihai', 'Jessy', 'Georgi', 'Ioana',
                   'Alex', 'Razvan', 'Dan']
        nume = ['Popescu', 'Radu', 'Ionescu', 'Dumitru', 'Stan', 'Gheorghe', 'Lupu', 'Craciun', 'Stoica', 'Avram']
        while len(self._student_list) < 10:
            y = random.randint(100, 999)
            y = str(y)
            stud = Students(y, random.choice(prenume) + ' ' + random.choice(nume),911)
            if self.find_student(y) == 0:
                self.add_student(stud)

    def find_student(self, student_id):

        x = 0
        while x < len(self._student_list):
            if self._student_list[x].student_id == student_id:
                return 1
            else:
                x = x + 1
        return 0
