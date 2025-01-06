from app import db, app
from sqlalchemy import inspect

with app.app_context():
    inspector = inspect(db.engine)
    tables = inspector.get_table_names()  # Fetch table names
    print("Tables:", tables)
