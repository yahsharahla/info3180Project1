from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://action@localhost/action'
db = SQLAlchemy(app)
app.config['SECRET_KEY'] = "s3cr3t jhbijo kkii"
UPLOAD_FOLDER = './filefolder'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


from app import views, models
