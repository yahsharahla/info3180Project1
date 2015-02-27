"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/

This file creates your application.
"""

from app import app
from flask import render_template, request, redirect, url_for, Flask
from .form import profileForm
from . import models
from app import db
from app.models import profile_user
import os
from werkzeug import secure_filename
from os import path

# Routing for your application.
    
@app.route('/')
def home():
    return render_template('home.html')	  

@app.route('/profile/', methods = ["POST", "GET"])
def profile_add():
    """up loads the profile to database"""
    form = profileForm()
    if request.method == "POST":
      first_name = request.form['first_name']
      last_name = request.form['last_name']
      age = request.form ['age']
      sex = request.form ['sex']
      file_upload = request.files['image']
      filename = file_upload.filename
      file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
      user = models.profile_user(first_name,last_name,age,sex, file_path)
      file_upload.save(file_path)
      #db.session.add(user)
      #db.session.commit()
      return "I am {} {} of age {} and i am a {} {}".format(first_name, last_name, age, sex, file_path)
    return render_template('profile.html', form = form)


@app.route('/profiles/')
def profiles_view():
    """view the list of profiles"""
    return "list of profiles"
	#return render_template('about.html')


###
# The functions below should be applicable to all Flask apps.
###

@app.route('/profile/<int:id>')
def profile_user(id):
   """Send your static text file."""
   return "profile {}".format(id)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=600'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port=8080)
