from flask_sqlalchemy import SQLAlchemy

#sets db to launch SQLALCHEMY 
db = SQLAlchemy()

#calls logic to connect to adatabase  
def connect_db(app):
    db.app = app
    db.init_app(app)

# models here 