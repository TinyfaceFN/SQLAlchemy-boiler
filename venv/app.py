from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension 
from models import db, connect_db, User
# import seed
# User 

app = Flask(__name__)

# SQLALCHEMY logic
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///test_userdatabase'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#Print all SQL statements to the terminal (helpful for debugging)
app.config['SQLALCHEMY_ECHO'] = True

# debuglogic
app.config['SECRET_KEY'] = '1234'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

with app.app_context():
    connect_db(app)
    db.create_all()
# seed.seed_data()    

# db.session.add()    
# db.session.commit() 


@app.route('/')
def home():
    # lists users  
    users = User.query.all()
    return render_template('welcomepage.html',users=users)

@app.route('/', methods=['POST'])
def homepost():  
    new_first = request.form['first_name']
    new_last = request.form['last_name']
    if request.form['image_url']:
         new_url = request.form['image_url']     
         new_user = User(first_name=new_first, last_name=new_last, image_url=new_url)
    else:
           new_user = User(first_name=new_first, last_name=new_last)
    db.session.add(new_user)
    db.session.commit()
    return redirect('/')

@app.route('/edit/user<int:user_id>')
def edit_user(user_id):
    user = User.query.filter_by(id =user_id).first()
    return render_template('edituser.html',user=user)

@app.route('/edit/user<int:user_id>', methods = ['POST'])
def edit_user_post(user_id):
    user = User.query.get(user_id)
    if request.form['first_name']:
         new_first = request.form['first_name']
         user.first_name = new_first
    if request.form['last_name']:
         new_last = request.form['last_name']
         user.last_name = new_last
    if request.form['image_url']:
         new_url = request.form['image_url']
         user.image_url = new_url
    # new_user = User.query.filter_by(id=user_id)(first_name=new_first, last_name=new_last, image_url=new_url)
    db.session.add(user)
    db.session.commit()
    return redirect('/')

@app.route('/<int:user_id>')
def user_info(user_id):
      users = User.query.filter_by(id=user_id).first()
      return render_template('userinfo.html', users=users)

@app.route('/newuser')
def new_user():
    return render_template('newuser.html')

@app.route('/delete/user<int:users_id>',methods=['POST'])
def delete_post(users_id):
     to_be_deleted = User.query.get(users_id)
     db.session.delete(to_be_deleted)
     db.session.commit()
     return redirect('/')


app.run(debug=True)
debug=True
# seed.seed_data()