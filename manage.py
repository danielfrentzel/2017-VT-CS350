from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///myapp.db'

db = SQLAlchemy(app)
migrate = Migrate(app, db)


class locations(db.Model):

    location_id = db.Column(db.Integer, primary_key=True)
    location_name = db.Column(db.String(128))
    location_description = db.Column(db.String(128))
    location_x = db.Column(db.String(128))
    location_x = db.Column(db.String(128))
