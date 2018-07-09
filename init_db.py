import sqlite3
from flask import Flask
from os import path

app = Flask(__name__)

ROOT = path.dirname(path.realpath(__file__))
DATABASE = 'myapp.db'


def init_db():
    # db = sqlite3.connect(DATABASE)
    db = sqlite3.connect(path.join(ROOT, DATABASE))

    with app.open_resource('db.sql', mode='r') as f:
        sql = f.read()

    print(sql)
    db.cursor().execute(sql)
    db.commit()
    db.close()


if __name__ == "__main__":
    init_db()
