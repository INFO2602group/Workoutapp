from App.database import db

class WorkoutList(db.Model)
  routineid= db.Column(db.Integer, primary_key=True,db.ForeignKey('routine.id'))
  workoutid=db.Column(db.Integer,primary_key=True,db.ForeignKey('workout.id'))

  def __init__(self, routineid, workoutid)
    self.routineid=routineid
    self.workoutid=workoutid

  def get_json(self):
    return{
      'routineid': self.routineid,
      'workoutid': self.workoutid
    }

  
  