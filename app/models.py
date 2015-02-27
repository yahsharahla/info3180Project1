from app import db

class profile_user(db.Model):
  id=db.Column(db.Integer,primary_key=True)
  first_name = db.Column(db.String(80),unique = True)
  last_name = db.Column(db.String(120),unique = True)
  age = db.Column(db.String(3), unique = True)
  sex = db.Column(db.String(6), unique = True)
  image = db.Column(db.String(100), unique = True)

  def __init__(self,first_name ,last_name, age, sex, image):
      self.first_name = first_name
      self.last_name = last_name
      self.age = age
      self.sex = sex

  def __repr__(self):
      return'<profile_user %r %r>' %(self.first_name, self.last_name)
