from flask import Flask, render_template, redirect, url_for, request
from db_helper import connect_db , StudentRecordHelper

app = Flask(__name__)

db = connect_db()
st_db_Helper = StudentRecordHelper(db)

@app.route("/")
def index():
    students = st_db_Helper.get_all()
    context ={
        "name" : "Student List",
        "student" : students
    }
    return render_template("index.html", **context)

@app.route("/student/create",methods =["GET","POST"])
def insert_student():
    if(request.method =="POST"):
        data = request.form
        # st = (data.get("name"),(data.get("dob"),(data.get("grade"),(data.get("address"),(data.get("parent_name"))
        # st_db_Helper.insert(st)
    return render_template("student/create.html")


if __name__ =="__main__":
    app.run(debug=True)