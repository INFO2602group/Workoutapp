from App.database import db

class Routine(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    exercises = db.relationship('Exercise', backref='routine', lazy=True)

    def __init__(self, name, description):
        self.name = name
        self.description = description

    def get_json(self):
        return{
            'id': self.id,
            'name': self.name,
            'description': self.description
        }

    def add_exercise(self, exercise):
        self.exercises.append(exercise)

    def remove_exercise(self, exercise):
        self.exercises.remove(exercise)

    def get_exercises(self):
        return self.exercises