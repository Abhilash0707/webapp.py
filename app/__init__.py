from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


app=Flask(__name__)
app.config['SECRET_KEY']='ca874ee4eb013eda02ac5f8c687dd702'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'  # SQLite URI
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
bcrypt=Bcrypt(app)
login_manager=LoginManager(app)
login_manager.login_view='login'
login_manager.login_message_category='info'

@app.cli.command('create-db')
def create_db():
    """Create the database tables."""
    db.create_all()
    print("Database tables created.")


from app import routes
