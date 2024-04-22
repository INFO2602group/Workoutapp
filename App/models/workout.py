from App.database import db

class Workout(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    excercise=db.Column(db.String(75),nullable=False)
    exercise_type=db.Column(db.String(100),nullable=False)
    Targeted_body_part=db.Column(db.String(100),nullable=False)


    def __init__(self, id,excercise,exercise_type,Targeted_body_part,Video_Link):
        self.id=id
        self.excercise=excercise
        self.exercise_type=exercise_type
        self.Targeted_body_part=Targeted_body_part
        self.Video_Link=Video_Link


    def get_json(self):
        return{
       'id': self.id,
       'excercise': self.excercise,
       'Targeted_body_part': self.Targeted_body_part,
       'Video_Link':self.Video_Link
        }

    # end def


