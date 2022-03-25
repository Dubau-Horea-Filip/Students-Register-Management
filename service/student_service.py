from Repos.student_repo import *
from service.undo_service import *
#student: student_id, name
from Domain.student import *
from service.undo_service import *
import random
from tests import *
class StudentService:
    def __init__(self, student_repo,undo_service):

        self._repo = student_repo
        self._undo_service = undo_service


    def create_student(self, student_id, name ):
        '''

        :param student_id:
        :param name:
        :return:

        '''
        if self.find_student(student_id) == 1:
            raise ValueError('student already exists')
        a=Students(student_id,name)

        self._repo.add_student(a)

        fun_undo = FunctionCall(self.remove_student_wundo, student_id)
        fun_redo = FunctionCall(self.create_student_wundo, student_id,name)
        self._undo_service.record(Operation(fun_undo, fun_redo))

    def create_student_wundo(self,student_id,name):
        if self.find_student(student_id) == 1:
            raise ValueError('student already exists')
        a = Students(student_id, name)
        self._repo.add_student(a)

    def remove_student_wundo(self, student_id):
        student = self._repo.remove_student(student_id)
    def remove_student(self, student_id):

        student = self._repo.remove_student(student_id)



    def get_all(self):
         return self._repo._student_list

    def update_student(self,student_id, name):
        self._repo.update(student_id, name)


    def find_student_name_from_id(self,id):
        x = 0
        _student_list= self.get_all()
        while x < len(_student_list):
            if _student_list[x].student_id == id:
                return _student_list[x].name

            else:
                x = x + 1

    def find_student_name(self,student_name):
        ok = 0
        x = 0
        list = []
        while x < len(self._repo._student_list):
            y = self._repo._student_list[x].name
            y=str(y).lower()
            name=str(student_name).lower()
            if name in y:
                ok = ok + 1
                list.append(self._repo._student_list[x])
                # print (self._repo._student_list[x])
                x = x + 1

            else:
                x = x + 1

        if ok == 0:
            return 'no student with the given name'
        return list
    def find_student_id(self,student_id):
        ok=0
        x = 0
        list=[]
        while x < len(self._repo._student_list):
            if student_id in self._repo._student_list[x].student_id  :
                ok=ok+1
                list.append( self._repo._student_list[x])
                #print (self._repo._student_list[x])
                x = x + 1

            else:
                x = x + 1

        if ok == 0:
            return 'no student with the given id'
        return list
        #print (list)

    def find_student_print(self,id):
        x = 0
        while x < len(self._repo._student_list):
            if self._repo._student_list[x].student_id == id:

                return self._repo._student_list[x]


            else:
                x = x + 1
        return 0
    def find_student(self,student_id):

        x = 0
        while x < len(self._repo._student_list):
            if self._repo._student_list[x].student_id == student_id:
               return 1
            else:
                x = x + 1
        return 0










