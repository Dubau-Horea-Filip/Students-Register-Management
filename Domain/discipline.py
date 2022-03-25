
#Discipline: discipline_id, name


class DisciplineException(Exception):
    def __init__(self, msg):
        self._msg = msg

class Disciplines:

    def __init__(self, discipline_id, name):
        
        self._discipline_id = discipline_id
        self._name = name


        DisciplineValidator.validate(self)



        
        
      

    @property
    def discipline_id(self):
        return self._discipline_id

    @property
    def name(self):
        return self._name

   
    @discipline_id.setter
    def discipline_id(self,value):
        self.discipline_id= value

    @name.setter
    def name(self,value):
        self._name=value


    def __str__(self):
        return 'ID: ' + str(self.discipline_id) + ' ' + 'NAME: ' + str(self.name)

class DisciplineValidator:
    @staticmethod
    def validate( discipline):
        '''
        Validate a given Discipline
        :param Discipline:
        :return:
        '''
       
        if discipline.name == '':
            raise DisciplineException('Name field should not be empty!')
        if discipline.discipline_id == '':
            raise DisciplineException('Id field should not be empty!')
       
        if len(discipline.discipline_id) < 3:
            raise DisciplineException('The client id should have 4 char str!')

def test_Discipline():
    c = Disciplines('1387187890', 'Pop Maria')
    assert c.discipline_id == '1387187890'
    assert c.name == 'Pop Maria'
    c.name = 'Ana'
    assert c.name == 'Ana'



test_Discipline()





def test_Discipline_Validator():

    try:
        s = Disciplines('712173991303', '')
        DisciplineValidator.validate(s)
        assert False
    except DisciplineException as s:
        # print (s)
        
        assert True

   


test_Discipline_Validator()
