class Note:

    def __init__(self, id, grade):
        self._id = id
        self._grade = grade

    @property
    def id(self):
        return self._id

    @property
    def grade(self):
        return self._grade

    def __lt__(self, other):
        if self._grade < other.grade:
            return True
        return False
