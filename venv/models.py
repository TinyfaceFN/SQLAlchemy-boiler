from flask_sqlalchemy import SQLAlchemy

#sets db to launch SQLALCHEMY 
db = SQLAlchemy()

#calls logic to connect to adatabase  

# models here 
class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer(), primary_key = True , autoincrement = True)

    first_name = db.Column(db.Text())

    last_name = db.Column(db.Text())

    image_url = db.Column(db.Text(),default='https://static.vecteezy.com/system/resources/thumbnails/009/734/564/small_2x/default-avatar-profile-icon-of-social-media-user-vector.jpg')




def connect_db(app):
    db.app = app
    db.init_app(app)
