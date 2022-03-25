from Repos.DisciplinesPickleRepo import DisciplinesPickleRepo
from Repos.DisicplineTextRepo import DisciplinesTextFileRepository
from Repos.GradePickleRepo2 import GradePicklRepo
from Repos.StudentPickleRepo import StudentsPickleFileRepo
from Repos.StudentTextRepo import StudentsTextFileRepository
from UI.console import  *
from service.grade_service import *
from service.discipline_service import *
from service.student_service import *
from Repos.GradeTextRepo2 import *
from settings import *
from service.undo_service import *

a=Settings()
v= a.read()

print(v[0])
print('random generation=',v[1])


if v[0] == 'inmemory':

    student_repo = StudentRepo()
    undo_service = UndoService()
    student_service = StudentService(student_repo, undo_service)

    discipline_repo = DisciplineRepo()
    discipline_service = DisciplineService(discipline_repo, undo_service)

    grade_repo = GradeRepo()
    grade_service = GradeService(grade_repo)

    # Program start
    the_program = Menu_UI(student_service, discipline_service, grade_service, undo_service,v[1])

    the_program.start()

elif v[0] == 'text_files':

    student_repo = StudentsTextFileRepository()
    undo_service = UndoService()
    student_service = StudentService(student_repo, undo_service)

    discipline_repo = DisciplinesTextFileRepository()
    discipline_service = DisciplineService(discipline_repo, undo_service)

    grade_repo = GradeTextFileRepository()
    grade_service = GradeService(grade_repo)
    from service.undo_service import *

    # Program start
    the_program = Menu_UI(student_service, discipline_service, grade_service, undo_service,v[1])

    the_program.start()


elif v[0] == "pickle":
    #Pickle
    # Student initialization
    student_repo = StudentsPickleFileRepo()
    undo_service = UndoService()
    student_service = StudentService(student_repo, undo_service)

    discipline_repo = DisciplinesPickleRepo()
    discipline_service = DisciplineService(discipline_repo, undo_service)

    #grade_repo = GradeTextFileRepository()
    grade_repo = GradePicklRepo()
    grade_service = GradeService(grade_repo)
    from service.undo_service import *

    # Program start
    the_program = Menu_UI(student_service, discipline_service, grade_service, undo_service,v[1])

    the_program.start()

else:
    print('ivalid method')