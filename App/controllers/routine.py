from App.models import routine
from App.database import db

def add_routine(self, name, description):
  newroutine = Routine(name=name, description=description)
  db.session.add(newroutine)
  db.session.commit()
  return newroutine

def add_exercise(self, exercise):
  self.exercises.append(exercise)

def remove_exercise(self, exercise):
  self.exercises.remove(exercise)

def get_exercises(self):
  return self.exercises
