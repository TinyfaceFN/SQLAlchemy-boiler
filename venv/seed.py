from models import db, User
from app import app 

def seed_data():
    # Ensure the app context is available
    with app.app_context():
        # Drop all tables and recreate them (optional, useful for development)
        db.drop_all()
        db.create_all()

        # Create sample users
        user1 = User(first_name='Alice', last_name='Smith')
        user2 = User(first_name='Bob', last_name='Brown')
        user3 = User(first_name='Charlie', last_name='Davis')

        # Add users to the session
        db.session.add(user1)
        db.session.add(user2)
        db.session.add(user3)  

        # Commit the session
        db.session.commit()
        print('NEW DATABASE SEEDED')
seed_data()