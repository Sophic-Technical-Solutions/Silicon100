
class Student:
   
    def __init__(self, name, grades):
        self._name = name
        self._grades = grades  # Internal attribute (indicated by _)
    
    @property
    def grades(self):
        return self._grades
    
    @grades.setter
    def grades(self, value):
        self._grades = value
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        self._name = value

    
    
