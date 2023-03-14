from flask import Flask
from .config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import psycopg2

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate= Migrate(app, db)


from app import views

conn = psycopg2.connect(
    host="localhost",
    database="project1",
    user="postgres",
    password= "Psalm1:3!"
)
cur = conn.cursor()

cur.execute("""
    CREATE TABLE IF NOT EXISTS properties (
        propertyid SERIAL PRIMARY KEY,
        title VARCHAR(255) NOT NULL,
        bathnum INTEGER NOT NULL,
        bednum INTEGER NOT NULL,
        location VARCHAR(255) NOT NULL,
        proptype VARCHAR(255) NOT NULL,
        price FLOAT NOT NULL,
        descr TEXT NOT NULL,
        photo VARCHAR(255) NOT NULL
    );
""")

conn.commit()

cur.close()
conn.close()