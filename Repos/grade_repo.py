from Domain.grade import *

#Grade: discipline_id, student_id, grade_value
from Repos.Repo_vector import Repository


class GradeRepo:
    def __init__(self, grades=None):

        #self._grade_list = []
        self._grade_list= Repository(list())



    @property
    def grades_list(self):
        return self._grade_list

    def add_all(self, grade_list):
        x = len(grade_list)
        self._grade_list.repository = grade_list
        self._grade_list.index = x

    def add_grade(self, grade):
        #self._grade_list.append(grade)
        self._grade_list.add_item(grade)

    def get_all(self):
        return self._grade_list.repository

    def remove_student(self, student_id):
        list_iterator = iter(self._grade_list)
        while True:
            try:
                student = next(list_iterator)
            except StopIteration:
                break
            else:
                if student.student_id == student_id:
                    del self._grade_list[self._grade_list.index]

        '''
        x = 0

        while x < len(self._grade_list):
            if self._grade_list[x].student_id ==student_id:

                del self._grade_list[x]
            else:
                x = x + 1
        '''

    def remove_student_and_gives_list(self, student_id):
        x = 0
        l=[]
        while x < len(self._grade_list.repository):
            if self._grade_list.repository[x].student_id == student_id:
                l.append(self._grade_list[x])
                x = x+1

            else:
                x = x + 1
        return l

    def remove_student_and_gives_list_2(self, student_id):
        x = 0
        l = []
        while x < len(self._grade_list.repository):
            if self._grade_list.repository[x].student_id == student_id:
                l.append(self._grade_list.repository[x])
                del self._grade_list.repository[x]


            else:
                x = x + 1
        return l


    def remove_discipline_and_gives_list(self, discipline_id):
        x = 0
        l=[]
        while x < len(self._grade_list):
            if self._grade_list.repository[x].discipline_id ==discipline_id:
                l.append(self._grade_list.repository[x])
                del self._grade_list[x]

            else:
                x = x + 1
        return l
    def remove_discipline(self, discipline_id):
        x = 0
        while x < len(self._grade_list):
            if self._grade_list.repository[x].discipline_id ==discipline_id:
                a=self._grade_list.repository[x]
                del self._grade_list[x]
                return a
            else:
                x = x + 1

