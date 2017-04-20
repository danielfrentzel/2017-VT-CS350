import sqlite3
import os
from flask import Flask, render_template, request

app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

DATABASE = 'myapp.db'
def connect_db():
    return sqlite3.connect(DATABASE)

#diplays the add location forum
@app.route('/AddLocation')
def addLocation():
    return render_template('AddLocation.html')

#adds locations from /AddLocation forum and displays list of the locations in db. Also allows user to upload img
@app.route('/LocationAdded')
def addLocations():
    location_id = request.args.get('location_id')
    location_name = request.args.get('location_name')
    location_description = request.args.get('location_description')
    # ukygt
    db = connect_db()
    sql = "insert into locations (location_id, location_name, location_description) values (?, ?, ?)"
    db.execute(sql, [location_id, location_name, location_description])
    db.commit()
    cur = db.execute("select * from locations")
    entries = [dict(location_id=row[0], location_name=row[1], location_description=row[2]) for row in cur.fetchall()]
    db.close()
    return render_template('LocationList.html', entries=entries)

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
    db.commit()
    cur = db.execute("select * from pictures")
    entries = [dict(location_id=row[0], file_location=row[1]) for row in cur.fetchall()]
    db.close()

    return render_template("complete.html", entries=entries)

#displays location list and allows user to upload images
@app.route("/LocationList")
def LocationList():
    db = connect_db()
    cur = db.execute("select * from locations")
    entries = [dict(location_id=row[0], location_name=row[1], location_description=row[2]) for row in cur.fetchall()]
    db.close()

    return render_template('LocationList.html', entries=entries)

#displays img list
@app.route("/viewImgList")
def viewImgList():
    db = connect_db()
    cur = db.execute("select * from pictures")
    entries = [dict(location_id=row[0], file_location=row[1]) for row in cur.fetchall()]
    db.close()

    return render_template("complete.html", entries=entries)

#displays map and options
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run()
