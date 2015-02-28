from app import db

class profile_user(db.Model):
  id=db.Column(db.Integer,primary_key=True)
  first_name = db.Column(db.String(80))
  last_name = db.Column(db.String(120))
  username = db.Column(db.String(120))
  age = db.Column(db.String(3))
  sex = db.Column(db.String(6))
  image = db.Column(db.String(100))

  def __init__(self,first_name ,last_name,username, age, sex, image):
      self.first_name = first_name
      self.last_name = last_name
      self.username = username
      self.age = age
      self.sex = sex
      self.image = image

  def __repr__(self):
      return'<profile_user %r %r>' %(self.first_name, self.last_name)
