from flask.ext.wtf import Form
from wtforms import TextField, FileField, SelectField
from flask_wtf.file import FileField, FileAllowed, FileRequired
#otherfieldsincludePasswordField
from wtforms.validators import Required, Email, InputRequired

class profileForm(Form):
  first_name = TextField('first_name',validators=[Required()])
  last_name = TextField('last_name',validators=[Required()])
  age = TextField('age',validators=[Required()])
  sex = SelectField(u'sex', choices=[('Male', 'Male'), ('Female', 'Female')])
  image = FileField('file', validators=[FileRequired(), FileAllowed(['jpg', 'png'], 'Images only!')])