# # models it is python class with represent the table in the database 

# from app import db  # Import the db instance from your application

# class Task(db.Model):  # Define the Task model
#     id = db.Column(db.Integer, primary_key=True)  # Define the id column as an integer primary key
#     title = db.Column(db.String(100), nullable=False)  # Define the title column as a string with a maximum length of 100 characters, and it cannot be null
#     status = db.Column(db.String(20), default="pending")  # Define the status column as a string with a maximum length of 20 characters, defaulting to "pending"

from app import db  # Import the db instance from your application

class Task(db.Model):  # Define the Task model
    id = db.Column(db.Integer, primary_key=True)  # Define the id column as an integer primary key
    title = db.Column(db.String(100), nullable=False)  # Define the title column as a string with a maximum length of 100 characters, and it cannot be null
    status = db.Column(db.String(20), default="pending")  # Define the status column as a string with a maximum length of 20 characters, defaulting to "pending"

    def __repr__(self):
        return f"<Task {self.id}: {self.title} ({self.status})>"

