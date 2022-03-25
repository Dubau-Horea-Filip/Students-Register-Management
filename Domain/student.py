
class Students:

    def __init__(self, student_id, name,group):
        
        self._student_id = student_id
        self._name = name
        self._group = group





        
      

    @property
    def student_id(self):
        return self._student_id

    @property
    def name(self):
        return self._name

    @property
    def group(self):
        return self._group

   
    @student_id.setter
    def student_id(self,value):
        self.student_id= value

    @name.setter
    def name(self,value):
        self._name=value

    @group.setter
    def group(self, value):
        self._group = value


    def __str__(self):
        return 'ID: ' + str(self.student_id) + ' ' + 'NAME: ' + str(self.name)  + 'GROUP: ' + str(self._group)


def test_student():
    c = Students('1387187890', 'Pop Maria',"913")
    assert c.student_id == '1387187890'
    assert c.name == 'Pop Maria'
    c.name = 'Ana'
    assert c.name == 'Ana'



test_student()








