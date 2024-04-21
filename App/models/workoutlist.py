from App.database import db

class WorkoutList(db.Model):
  routineid = db.Column(db.Integer, db.ForeignKey('routine.id'), primary_key=True)
  workoutid=db.Column(db.Integer,db.ForeignKey('workout.id'),primary_key=True)

  def __init__(self, routineid, workoutid):
    self.routineid=routineid
    self.workoutid=workoutid

  def get_json(self):
    return{
      'routineid': self.routineid,
      'workoutid': self.workoutid
    }

  
  