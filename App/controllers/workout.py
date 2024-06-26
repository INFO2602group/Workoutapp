from App.models import workout
from App.database import db
'''
def initialize_db():
  db.drop_all()
  db.create_all()
  with open('App/excercises.csv', mode='r', encoding='utf-8') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
      workout = Workout(id=row['ID'],
                        Name=row['Name'],
                        exercise_type=row['exercise_type'],
                        Targeted_body_part=row['Targeted_body_part'],
                        Video_Link=row['Video_Link'])
      db.session.add(workout)
    db.session.commit()
    return None'''

def get_exercise(id):
  return Workout.query.get(id)

def get_all_users():
  return Workout.query.all()

 