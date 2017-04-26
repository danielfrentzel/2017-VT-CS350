import sqlite3
import os
from flask import Flask, render_template, request

app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

x=0
y=0

DATABASE = 'myapp.db'
def connect_db():
    return sqlite3.connect(DATABASE)

#diplays the add location forum
@app.route('/AddLocation')
def addLocation():
    global x, y
    x = request.args.get('x')
    y = request.args.get('y')
    db = connect_db()
    cur = db.execute("select * from locations")
    entries = [dict(location_id=row[0], location_name=row[1], location_description=row[2], location_x=row[3], location_y=row[4]) for row in cur.fetchall()]
    cur = db.execute("select * from pictures")
    pictures = [dict(location_id=row[0], file_location=row[1]) for row in cur.fetchall()]
    db.close()
    return render_template('AddLocation.html', entries=entries, pictures=pictures, x=x, y=y)

#adds locations from /AddLocation forum and displays list of the locations in db. Also allows user to upload img
@app.route('/LocationAdded')
def addLocations():
    global x, y
    location_name = request.args.get('location_name')
    location_description = request.args.get('location_description')
    location_x = str(int(x) - 16)
    location_y = str(int(y) - 25)

    db = connect_db()
    sql = "insert into locations (location_name, location_description, location_x, location_y) values (?, ?, ?, ?)"
    db.execute(sql, [location_name, location_description, location_x, location_y])
    entries = [dict(location_name=location_name, location_description=location_description, location_x=location_x, location_y=location_y)]
    db.commit()
    db.close()
    x=0
    y=0
    return render_template('LocationAdded.html', entries=entries)

#uploads images from /locationAdded forum and then displays img list
@app.route("/upload", methods=["POST"])
def upload():
    target = os.path.join(APP_ROOT, 'imgs/')
    print(target)
    location_id = request.args.get('location_id')

    if not os.path.isdir(target):
        os.mkdir(target)

    for file in request.files.getlist("file"):
        print(file)
        filename = file.filename
        destination = "/".join([target, filename])
        print(destination)
        file.save(destination)


    db = connect_db()
    sql = "insert into pictures (location_id, img1) values (?, ?)"
    db.execute(sql, [location_id, "imgs/" + filename])
    entries = [dict(location_id = location_id, file_location = "imgs/" + filename)]
    db.commit()
    db.close()

    return render_template("ImgUploaded.html", entries=entries)

#used for deleting the location in the database from all the tables
@app.route('/DeleteLocation')
def DeleteLocation():
    location_id = request.args.get('location_id')
    db = connect_db()
    sql = "Select * from locations where location_id = (?)"
    cur = db.execute(sql, [location_id])
    entries = [dict(location_id=row[0], location_name=row[1], location_description=row[2]) for row in cur.fetchall()]
    sql = "DELETE FROM locations WHERE location_id = (?)"
    db.execute(sql, [location_id])
    sql = "DELETE FROM pictures WHERE location_id = (?)"
    db.execute(sql, [location_id])
    db.commit()
    db.close()

    return render_template("LocationDeleted.html", entries=entries)

#displays map and options
@app.route('/')
def index():
    db = connect_db()
    cur = db.execute("select * from locations")
    entries = [dict(location_id=row[0], location_name=row[1], location_description=row[2], location_x=row[3],
                    location_y=row[4]) for row in cur.fetchall()]
    return render_template('index.html', entries=entries)

if __name__ == "__main__":
    app.run()
