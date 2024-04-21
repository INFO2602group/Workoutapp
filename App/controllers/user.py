from App.models import User
from App.database import db
from App.models.workout import Workout
import csv

def create_user(username, password):
    newuser = User(username=username, password=password)
    db.session.add(newuser)
    db.session.commit()
    return newuser

def get_user_by_username(username):
    return User.query.filter_by(username=username).first()

def get_user(id):
    return User.query.get(id)

def get_all_users():
    return User.query.all()

def get_all_users_json():
    users = User.query.all()
    if not users:
        return []
    users = [user.get_json() for user in users]
    return users

def update_user(id, username):
    user = get_user(id)
    if user:
        user.username = username
        db.session.add(user)
        return db.session.commit()
    return None
  
def initialize_db():
  db.drop_all()
  db.create_all()
  with open('App/exercises.csv', mode='r', encoding='utf-8') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
      list = Workout(id=row['id'],
                        excercise=row['name'],
                        exercise_type=row['exercise_type'],
                        Targeted_body_part=row['Targeted_body_part'],
                        Video_Link=row['Video_Link'])
      db.session.add(list)
    db.session.commit()
    return None
 