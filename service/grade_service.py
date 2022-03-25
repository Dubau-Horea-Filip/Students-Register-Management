from Domain.note import Note
from Repos.grade_repo import *
#Grade: discipline_id, student_id, grade_value
import random
import collections

import operator
class GradeService:
    def __init__(self, grade_repo):

        self._repo = grade_repo


    def create_grade(self,discipline_id, student_id, grade_value ):
        '''

        :param discipline_id:
        :param student_id:
        :return:

        '''
        a = Grades(discipline_id, student_id, grade_value)

        self._repo.add_grade(a)

        # self._repo.add_all(new_car)

    def remove_by_student_id(self, student_id):
        return self._repo.remove_student_and_gives_list(student_id)

    def remove_by_student_id_2(self, student_id):
        return self._repo.remove_student_and_gives_list_2(student_id)

    def remove_by_discipline_id(self, discipline_id):
        return self._repo.remove_discipline_and_gives_list(discipline_id)

    def give_grades(self,list):
        for x in list:
            self._repo.add_grade(x)

    def find_discipline(self, discipline_id):
        x = 0
        while x < len(self._repo._discipline_list):
            if self._repo._discipline_list[x].discipline_id == discipline_id:
                return 1
            else:
                x = x + 1
        return 0
    def get_all(self):
        # return self._grades_list
        list = self._repo.get_all()
        for l in list :
            print (l)
    def find_student(self,student_id):

        x = 0
        while x < len(self._repo._student_list):
            if self._repo._student_list[x].student_id == student_id:

               return 1


            else:
                x = x + 1
        return 0



    def filter(self, a:Note):
        if a.grade < 5:
            return True
        else:
            return False


    def avarage(self):

        #self._repo.grades_list.sort(self._repo._student_list.repository,self.fail)
        list1 = []
        rez={}
        # pune intr un vector materiile
        mat={}
        x=0
        while x < len(self._repo.grades_list):
            if self._repo.grades_list[x].discipline_id not in mat:
                mat[ self._repo.grades_list[x].discipline_id ] = 0
            x=x+1
        #print (mat)
        #print ('1')
        for z in mat:
            #print (z)

            students_dict={}    #students_dict = {'123': 0,'231':0},
            students_dict_tmes = {}          # mat = {'116': 0, '543': 0, '740': 0, '876': 0, '528': 0, '837': 0, '857': 0}
            x=0
            while x < len(self._repo.grades_list):
                if self._repo.grades_list[x].discipline_id == z:
                    if self._repo.grades_list[x].student_id not in students_dict :
                        students_dict[ self._repo.grades_list[x].student_id ] = 0
                        students_dict[self._repo.grades_list[x].student_id] += self._repo.grades_list[x].grade
                        students_dict_tmes[self._repo.grades_list[x].student_id] = 1
                    else:
                        students_dict[self._repo.grades_list[x].student_id] += self._repo.grades_list[x].grade
                        students_dict_tmes[self._repo.grades_list[x].student_id] += 1
                x=x+1





            for xx in students_dict:
                a=int(students_dict[xx])
                b=int(students_dict_tmes[xx])

                y =  a/ b


                c=5
                if y < c:
                    rez[xx] = 'fail'
                    list1.append(Note(xx, y))

        for x in list1:
            print(x.id,x.grade)

        list2 = []
        list3 = []

        a = Repository([])
        list2 = a.filter(list1,self.filter)

        for x in list2:
            for y in list2:
                if x.id == y.id:
                    del y

        for x in list2:
            # print(x.grade, x.id)
            list3.append(x.id)


        return list3

    def best_sort(self,a:Note,b:Note):
        if a > b:
            return True
        else:
            return False



    def best(self):





        rez = {}
        times={}
        # pune intr un vector materiile
        mat = {}
        x = 0
        while x < len(self._repo.grades_list):
            if self._repo.grades_list[x].discipline_id not in mat:
                mat[self._repo.grades_list[x].discipline_id] = 0
            x = x + 1
        # print (mat)
        # print ('1')
        for z in mat:
            # print (z)

            students_dict = {}  # students_dict = {'123': 0,'231':0},
            students_dict_tmes = {}  # mat = {'116': 0, '543': 0, '740': 0, '876': 0, '528': 0, '837': 0, '857': 0}
            x = 0
            while x < len(self._repo.grades_list):
                if self._repo.grades_list[x].discipline_id == z:
                    if self._repo.grades_list[x].student_id not in students_dict:
                        students_dict[self._repo.grades_list[x].student_id] = 0
                        students_dict[self._repo.grades_list[x].student_id] += self._repo.grades_list[x].grade
                        students_dict_tmes[self._repo.grades_list[x].student_id] = 1
                    else:
                        students_dict[self._repo.grades_list[x].student_id] += self._repo.grades_list[x].grade
                        students_dict_tmes[self._repo.grades_list[x].student_id] += 1
                x = x + 1
            for xx in students_dict:
                a = int(students_dict[xx])
                b = int(students_dict_tmes[xx])
                y = a / b
                if xx not in rez:
                    rez[xx]=y
                    times[xx]=1
                else:
                    rez[xx] += y
                    times[xx] += 1


            # print(students_dict)

        # print('2')
        list=[]
        list2=[]
        list3=[]
        x=0
        for xx in rez:
            rez[xx]=rez[xx]/times[xx]
            list3.append(Note(xx,rez[xx]))
            list.append(rez[xx])
            list2.append(xx)
            x+=1

        list4 = []
        list5 = []

        a = Repository([])
        list4 = a.sort(list3,self.best_sort)



        for x in list4:
            #print(x.grade, x.id)
            list5.append(x.id)


        '''
        for x in range(0,len(list)):
            for y in range(x,len(list)):
                if list[x] < list[y] :
                    aux=list[x]
                    list[x]=list[y]
                    list[y]=aux
                    aux = list2[x]
                    list2[x] = list2[y]
                    list2[y] = aux
        '''



        return list5    ###########################################################################################

    def materii(self):
        rez={}
        # pune intr un vector materiile
        mat={}
        mat_times={}
        x=0
        while x < len(self._repo.grades_list):
            if self._repo.grades_list[x].discipline_id not in mat:
                mat[ self._repo.grades_list[x].discipline_id ] = 0
                mat_times[self._repo.grades_list[x].discipline_id] = 0
            x=x+1
        #print (mat)
        #print ('1')
        for z in mat:
            #print (z)

            students_dict={}    #students_dict = {'123': 0,'231':0},
            students_dict_tmes = {}          # mat = {'116': 0, '543': 0, '740': 0, '876': 0, '528': 0, '837': 0, '857': 0}
            x=0
            while x < len(self._repo.grades_list):
                if self._repo.grades_list[x].discipline_id == z:
                    if self._repo.grades_list[x].student_id not in students_dict :
                        students_dict[ self._repo.grades_list[x].student_id ] = 0
                        students_dict[self._repo.grades_list[x].student_id] += self._repo.grades_list[x].grade
                        students_dict_tmes[self._repo.grades_list[x].student_id] = 1
                    else:
                        students_dict[self._repo.grades_list[x].student_id] += self._repo.grades_list[x].grade
                        students_dict_tmes[self._repo.grades_list[x].student_id] += 1
                x=x+1
            for xx in students_dict:
                a=int(students_dict[xx])
                b=int(students_dict_tmes[xx])
                y =  a/ b
                #y=int(y)
                mat[z]+=y
                mat_times[z]+=1
            #print(students_dict)
       # print(mat,mat_times)
        list=[]
        list2=[]
        list3=[]
        for xx in mat:

            mat[xx] = (mat[xx])/ (mat_times[xx])
            #mat[xx]=int(mat[xx])
            list3.append(Note(xx,mat[xx]))
            list.append(mat[xx])
            list2.append(xx)



        for x in range(0,len(list)):
            for y in range(x,len(list)):
                if list[x] < list[y] :
                    aux=list[x]
                    list[x]=list[y]
                    list[y]=aux
                    aux = list2[x]
                    list2[x] = list2[y]
                    list2[y] = aux

        list4 = []
        list5 = []

        a = Repository([])
        list4 = a.sort(list3, self.best_sort)

        for x in list4:
            #print(x.id,x.grade)
            list5.append(x.id)


        #print (list,list2)
        return list5




