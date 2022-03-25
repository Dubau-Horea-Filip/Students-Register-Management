from Domain.student import *
import random
from Domain.grade import *
from Repos.Repo_vector import Repository
from service.undo_service import *
from service.remove_wundo import *
class Menu_UI:
    def __init__(self, student_service, discipline_service, grade_service,undo_service,generator):
        self._student_service    = student_service
        self._discipline_service = discipline_service
        self._grade_service      =  grade_service
        self._undo_service       = undo_service
        self._generator          = generator

    def print_menu(self):
        print('1:add student')
        print('2:remove student')
        print('3:update student')
        print('4:list students')
        print('5:add discipline')
        print('6:remove discipline')
        print('7:update discipline')
        print('8:list discipline')
        print('9:add grade')
        print('10:list grades')
        print('11:Search for student')
        print('12:Search for disciplines')
        print('13:statistic: Students failing')
        print('14:statistic: Students with the best school situation')
        print('15:statistic: Disciplines descending order of the average grade')
        print('16:Undo')
        print('17:redo')


    # Student: student_id, name
    def add_student_ui(self):

        a=input('student_id(at leadt 3 digits):')
        b=input('student name:')

        self._student_service.create_student(a,b)




    def remove_student_ui(self):
        a = input('student_id(at leadt 3 digits) that you want to remove:')
        b = self._student_service.find_student_name_from_id(a)
        v = self._grade_service.remove_by_student_id(a)

        #for x in v:
         #   print (x)

        re=Wundo_service_students(self._student_service, self._grade_service, self._undo_service,a,b,v)
        re.remove_undo()





    def update_student_ui(self):
        a = input('student_id(at leadt 3 digits) that you want to update:')
        b = input('student new name:')
        c= self._student_service. find_student_name_from_id(a)
        self._student_service.update_student(a,b)

        fun_undo = FunctionCall(self._student_service.update_student, a, c)
        fun_redo = FunctionCall(self._student_service.update_student, a, b)
        self._undo_service.record(Operation(fun_undo, fun_redo))
    def list_student_ui(self):

        list = self._student_service._repo.get_all()
        for l in list:
            print(l)



    def add_discipline_ui(self):
        a = input('discipline_id(at leadt 3 digits):')
        b = input('discipline name:')
        try:

            self._discipline_service.create_discipline(a,b)
        except ValueError as e:
            print(e)


    def remove_discipline_ui(self):
        a = input('discipline_id(at leadt 3 digits) that you want to remove:')
        b=self._discipline_service.find_discipline_name_by_id(a)
        self._discipline_service.remove_discipline(a)
        v=self._grade_service.remove_by_discipline_id(a)

        #for x in v:
        #    print (x)
        re = Wundo_service_discipline(self._discipline_service, self._grade_service, self._undo_service, a, b, v)
        re.remove_undo()



        

    def remove_discipline_wundo(self,a):
        self._discipline_service.remove_discipline(a)
        self._grade_service.remove_by_discipline_id(a)





    def update_discipline_ui(self):
        a = input('discipline_id(at leadt 3 digits) that you want to update:')
        b = input('discipline new name:')

        c = self._discipline_service.find_discipline_name_by_id(a)

        self._discipline_service.update_discipline(a, b)

        fun_undo = FunctionCall(self._discipline_service.update_discipline, a, c)
        fun_redo = FunctionCall(self._discipline_service.update_discipline, a, b)
        self._undo_service.record(Operation(fun_undo, fun_redo))

    def list_discipline_ui(self):
        list =self._discipline_service.get_all()
        for l in list:
            print(l)
    def add_grade_ui(self):
        # reads from console the discipline and student id and grade and sents it to service
        a = input('discipline_id(at leadt 3 digits):')
        b = input('student_id(at leadt 3 digits):')
        c = input ('Grade(between 1 and 10):')
        x = self._student_service.find_student(b)
        if x == 0:
            raise ValueError('student  nonexistent')

        y = self._discipline_service.find_discipline(a)

        if y == 0 :
            raise ValueError(' discipline nonexistent')

        self._grade_service.create_grade(a, b,c)


    def list_grade_ui(self):
        list = self._grade_service._repo.get_all()
        for l in list:
            print(l)

    def search_student_ui(self):
        print('1:Search by id')
        print('2:Search by name')
        command = input("Enter command: ")
        command=int(command)
        if command != 1 and  command != 2 :
            raise Exception('invalid comand')
        else :
            if command == 1:
                a = input('student_id(at leadt 3 digits):')
                a= self._student_service.find_student_id(a)
                if isinstance(a, str) :
                    print (a)
                else:
                    for b in a:
                        print (b)
            else:
                b = input('student name:')
                b = self._student_service.find_student_name(b)
                if isinstance(b, str):
                    print(b)
                else:
                    for a in b:
                        print(a)

    def search_discipline_ui(self):
        print('1:Search by id')
        print('2:Search by title')
        command = input("Enter command: ")
        command = int(command)
        if command != 1 and command != 2:
            raise Exception('invalid comand')
        else :
            if command == 1:
                a = input('discipline_id(at leadt 3 digits):')
                a= self._discipline_service.find_discipline_id(a)
                if isinstance(a, str) :
                    print (a)
                else:
                    for b in a:
                        print (b)
            else:
                b = input('discipline name:')
                b = self._discipline_service.find_discipline_name(b)
                if isinstance(b, str):
                    print(b)
                else:
                    for a in b:
                        print(a)
    def avg(self):
        x = (self._grade_service.avarage())
        print ('students failing at one or more disciplines:')
        for y in x:
            print(self._student_service.find_student_print(y))

    def sorted(self):
        x=self._grade_service.best()
        print('students with the best school situation')
        for y in x:
            print(self._student_service.find_student_print(y))

    def disciplines(self):
        x=self._grade_service.materii()
        print('sorted in descending order of the average grade received by all students enrolled at that discipline')
        for y in x:
            print(self._discipline_service.find_discipline_print(y))

    def undo_ui(self):
        self._undo_service.undo()


    def redo_ui(self):
        self._undo_service.redo()

    def save(self):
        self._student_service._repo.write_text_file()




    def start(self):                         #################################
        print('Start the program')
        if self._generator == 'true':

            self._student_service._repo.new()


            #self._discipline_service._repo._discipline_list = []

            self._discipline_service.new()

            #self._grade_service._repo._grade_list.repository = []
            #self._grade_service._repo._grade_list.index = -1

            self._grade_service._repo._grade_list = Repository(list())

            xx=0

            while xx < 10:

                y = random.randint(100, 999)
                y = str(y)
                if self._student_service.find_student(y) == 1:

                    z = random.randint(100, 999)
                    z = str(z)
                    x = random.randint(1, 10)
                    if self._discipline_service.find_discipline(z) == 1 and self._student_service.find_student(y) == 1:
                        xx = xx + 1
                        self._grade_service.create_grade(z, y, x)


        self.print_menu()
        cont = True
        # add, remove, update, and list both students and disciplines.
        command_dict = {'1': self.add_student_ui, '2': self.remove_student_ui, '3': self.update_student_ui, '4': self.list_student_ui,'5': self.add_discipline_ui,
                        '6': self.remove_discipline_ui, '7': self.update_discipline_ui, '8': self.list_discipline_ui, '9':self.add_grade_ui,'10':self.list_grade_ui,
                        '11':self.search_student_ui,'12':self.search_discipline_ui,'13':self.avg ,'14':self.sorted,'15':self.disciplines,
                        '16':self.undo_ui,'17':self.redo_ui,
                        '18':self.save}

        while cont is True:


            command = input("Enter command: ")

            if command == '0':
                cont = False

            elif command in command_dict:

                try:
                    command_dict[command]()
                except Exception as ve:
                    print(str(ve))
            else:
                print('Invalid command!')




