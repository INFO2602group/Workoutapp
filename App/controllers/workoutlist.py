from App.models import workoutlist
from App.database import db

def add_workout(routineid, workoutid):
  newworkoutlist=workoutlist(routineid=routineid, workoutid=workoutid)
  db.session.add(newworkoutlist)
  db.session.commit()

def removeworkout(routineid,workout)
  workout=workoutlist.query.filter_by(routineid=routineid,workoutid=workoutid).frist
  db.session.remove(workout)
  db.session.commit()