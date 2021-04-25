from flask import Flask, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy
import os
app= Flask(__name__)
app.config('SECRET')
app.config['SECRET_KEY']='secret'
app.config['SQLALCHEMY_DATABASE_URI']=os.environ.get("DATABASE_URL")
db = SQLAlchemy(app)
class User(db.Model):
    __tablename__='users'
    id = db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String,unique=True)
    email=db.Column(db.String, unique=True)

db.init_app()

@app.route("/new",methods=['get','post'])
def new():
    if request.method=='POST':
        email=request.form['email']
        name = request.form['name']

        user = User(name=name,email=email)
        db.session.add(user)
        db.session.commit()
    return render_template("new.html")

@app.route("/user/<username>")
def users(username):
    user=User.query.filter_by(name=username).first()
    if user is None:
        return "No user found"
    else:
        return user.email

