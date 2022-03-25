
#Grade: discipline_id, student_id, grade_value


class StudentException(Exception):
    def __init__(self, msg):
        self._msg = msg

class Grades:

    def __init__(self, discipline_id, student_id, grade_value):

        self._student_id = student_id
        self._discipline_id = discipline_id
        self._grade = grade_value

        StudentValidator.validate(self)




    @property
    def student_id(self):
        return self._student_id

    @property
    def discipline_id(self):
        return self._discipline_id

    @property
    def grade(self):
        return self._grade


    @student_id.setter
    def student_id(self,value):
        self.student_id= value

    @grade.setter
    def grade(self,value):
        self._grade=value


    def __str__(self):
        return 'Student ID: ' + str(self.student_id) + ' ' + 'Discipline ID: ' + str(self.discipline_id) + ' ' + 'Grade: ' + str(self.grade)

class StudentValidator:
    @staticmethod
    def validate( student):
        '''
        Validate a given student
        :param student:
        :return:
        '''

        if student.grade == '':
            raise StudentException('Grade field should not be empty!')
        if student.student_id == '':
            raise StudentException('Id field should not be empty!')

        if len(student.student_id) < 3:
            raise StudentException('The client id should have 4 char str!')

def test_student():
    c = Grades('Pop Maria','1387187890' ,10)
    assert c.student_id == '1387187890'
    assert c.grade == 10
    c.grade = 11
    assert c.grade == 11



test_student()





def test_Student_Validator():

    try:
        s = Grades('712173991303', '','asdvf')
        StudentValidator.validate(s)
        assert False
    except StudentException as s:
       # print (s)

        assert True




test_Student_Validator()