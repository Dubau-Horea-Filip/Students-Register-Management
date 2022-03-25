from service.undo_service import *

class Wundo_service_students:
    def __init__(self, student_service , grade_service, undo_service, a, b, v):
        self._student_service = student_service
        self._grade_service = grade_service
        self._undo_service = undo_service
        self._a = a
        self._b = b
        self._v = v

    def remove(self):
        self._student_service.remove_student(self._a)
        self._grade_service.remove_by_student_id_2(self._a)


    def add(self):
        self._grade_service.give_grades(self._v)
        self._student_service.create_student_wundo(self._a,self._b)


    def remove_undo(self):
        self._student_service.remove_student(self._a)
        self._grade_service.remove_by_student_id_2(self._a)

        fun_undo = FunctionCall(self.add)
        fun_redo = FunctionCall(self.remove)
        self._undo_service.record(Operation(fun_undo, fun_redo))

class Wundo_service_discipline:
    def __init__(self, disicipline_service , grade_service, undo_service, a, b, v):
        self._discipline_service = disicipline_service
        self._grade_service = grade_service
        self._undo_service = undo_service
        self._a = a
        self._b = b
        self._v = v

    def remove(self):
        self._discipline_service.remove_discipline(self._a)
        self._grade_service.remove_by_student_id_2(self._a)


    def add(self):
        self._grade_service.give_grades(self._v)
        self._discipline_service.create_discipline_wundo(self._a,self._b)



    def remove_undo(self):
        self._discipline_service.remove_discipline(self._a)
        self._grade_service.remove_by_student_id_2(self._a)

        fun_undo = FunctionCall(self.add)
        fun_redo = FunctionCall(self.remove)
        self._undo_service.record(Operation(fun_undo, fun_redo))



