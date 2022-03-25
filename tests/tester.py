import unittest
import random
from Repos.student_repo import *
from service.student_service import *
from service.grade_service import *
from service.discipline_service import *

class StuentUnitTest(unittest.TestCase):
    def setUp(self):
        self._repo= StudentRepo()
        self._service= StudentService(self._repo)
        self._service.new()

    def test_add(self):
        x='1234'
        y='David'
        lengh = len(self._service.get_all())
        self._service.create_student(x,y)
        self.assertEqual(len(self._service.get_all()),lengh+1)

    def test_remove(self):
        x = '1234'
        y = 'David'
        lengh = len(self._service.get_all())
        self._service.create_student(x, y)
        self.assertEqual(len(self._service.get_all()), lengh + 1)
        self._service.remove_student('1234')
        self.assertEqual(len(self._service.get_all()), lengh )

    def test_update(self):
        x = '1234'
        y = 'David'
        lengh = len(self._service.get_all())
        self._service.create_student(x, y)
        #self.assertEqual(len(self._service.get_all()), 11)
        self._service.update_student('1234','Philip')
        self.assertEqual('Philip',self._service.find_student_print('1234').name)

    def test_create(self):
        x = '1234'
        y = 'David'
        Students(x,y)
        self.assertEqual(x,'1234')
        self.assertEqual(y,'David')


class GradeUnitTest(unittest.TestCase):
    def setUp(self):
        self._repo= GradeRepo()
        self._service= GradeService(self._repo)
        self._service.create_grade('1123', '4255', 8)
        self._service.create_grade('1223', '4225', 9)
        self._service.create_grade('1243', '4295', 5)
        self._service.create_grade('1203', '4215', 2)



    def test_add(self):
        self._service.create_grade('1263','42745',8)

    def test_avarage(self):

        a=self._service.avarage()
        
        self._service.best()
        self._service.materii()

    def test_init_grades(self):
        gradesa = [Grades('12375', '4562', 'sfdbgx'), Grades('155624', 'fghX', 'sfdbgf'),
                   Grades('12565', 'Yzdfg', 'fvdbgxf')]

        repo = GradeRepo(gradesa)
        self.assertEqual(len(repo.grades_list),3)
        return gradesa




    def test_add_grades(self):
        repo = test_init_grades()
        repo.add_grade(Grades('1223', 'ghnf', 'dfdbg'))
        assert len(repo.grades_list) == 4


    def test_remove_grades(self):
        repo = test_init_grades()
        repo.remove_student('fghX')
        assert len(repo.grades_list) == 2

    def test_Discipline(self):
        c = Disciplines('1387187890', 'Pop Maria')
        assert c.discipline_id == '1387187890'
        assert c.name == 'Pop Maria'
        c.name = 'Ana'
        assert c.name == 'Ana'





