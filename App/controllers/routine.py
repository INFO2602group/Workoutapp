from App.models import routine
from App.database import db

def add_routine(self, name, description)
  newroutine = Routine(name=name, description=description)
  db.session.add(newroutine)
  db.session.commit()
  return newroutine
