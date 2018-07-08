from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///myapp.db'

db = SQLAlchemy(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

class locations(db.Model):

    location_id = db.Column(db.Integer, primary_key=True)
    location_name = db.Column(db.String(128))
    location_description = db.Column(db.String(128))
    location_x = db.Column(db.String(128))
    location_x = db.Column(db.String(128))

if __name__ == '__main__':
    manager.run()