from App.database import db

class Routine(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    userid= db.Colum(db.Integer, db.ForeignKey('user.id'))
    

    def __init__(self, name, description,userid):
        self.name = name
        self.description = description
        self.userid=userid

    def get_json(self):
        return{
            'id': self.id,
            'name': self.name,
            'description': self.description
            'userid':self.userid'
        }

