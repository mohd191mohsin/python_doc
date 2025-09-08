# Python Database Connectivity (SQLite, MySQL, SQLAlchemy)

```python
# SQLite
import sqlite3

# Connect to database
conn = sqlite3.connect("example.db")
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER
)
""")

# Insert data
cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Alice", 25))
conn.commit()

# Query data
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()
for row in rows:
    print(row)

# Close connection
conn.close()

# MySQL (using mysql-connector)
import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="testdb"
)

cursor = db.cursor()
cursor.execute("SELECT * FROM users")
for row in cursor.fetchall():
    print(row)

db.close()

# SQLAlchemy (ORM)
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

engine = create_engine("sqlite:///example.db")
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# Add new user
new_user = User(name="Bob", age=30)
session.add(new_user)
session.commit()

# Query users
users = session.query(User).all()
for u in users:
    print(u.id, u.name, u.age)
