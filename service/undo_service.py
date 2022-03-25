class UndoService:
    def __init__(self):

        self._history = []
        self._index = -1

    def record(self, operation):


        self._history = self._history[0:self._index + 1]
        self._history.append(operation)

        self._index += 1

    def undo(self):
        if self._index == -1:
            raise ValueError('no more undo available')

        operation = self._history[self._index]
        operation.undo()
        self._index -= 1

    def redo(self):
        if self._index + 1 == len(self._history):
            raise ValueError('no more redo available')

        self._index += 1
        operation = self._history[self._index]
        operation.redo()


class Operation:
    def __init__(self, fun_undo, fun_redo):
        self._fun_undo = fun_undo
        self._fun_redo = fun_redo

    def undo(self):
        self._fun_undo()

    def redo(self):
        self._fun_redo()


class FunctionCall:
    def __init__(self, fun_name, *fun_params):
        self._fun_name = fun_name
        self._fun_params = fun_params

    def call(self):
        self._fun_name(*self._fun_params)

    def __call__(self):
        self.call()
