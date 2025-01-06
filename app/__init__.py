from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app=Flask(__name__)
app.config['SECRET_KEY']='ca874ee4eb013eda02ac5f8c687dd702'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'  # SQLite URI
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

@app.cli.command('create-db')
def create_db():
    """Create the database tables."""
    db.create_all()
    print("Database tables created.")


from app import routes
