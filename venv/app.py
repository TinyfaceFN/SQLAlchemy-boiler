from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension 
from models import db, connect_db
app = Flask(__name__)

# SQLALCHEMY logic
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///DATABASENAME'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#Print all SQL statements to the terminal (helpful for debugging)
app.config['SQLALCHEMY_ECHO'] = True

# debuglogic
app.config['SECRET_KEY'] = '1234'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)

# db.session.add()    
# db.session.commit() 

@app.route('/')
def home():
    # some thing 
    return 

