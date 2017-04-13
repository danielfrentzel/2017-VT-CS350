import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)

DATABASE = 'myapp.db'
def connect_db():
    return sqlite3.connect(DATABASE)

@app.route('/AddLocation')
def addLocation():
    return render_template('AddLocation.html')

@app.route('/LocationAdded')
def addLocations():
    location_id = request.args.get('location_id')
    location_name = request.args.get('location_name')
    location_description = request.args.get('location_description')
    db = connect_db()
    sql = "insert into locations (location_id, location_name, location_description) values (?, ?, ?)"
    db.execute(sql, [location_id, location_name, location_description])
    db.commit()
    cur = db.execute("select * from locations")
    entries = [dict(location_id=row[0], location_name=row[1], location_description=row[2]) for row in cur.fetchall()]
    db.close()
    return render_template('LocationList.html', entries=entries)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run()
