from flask import Flask, render_template
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
    return render_template("index.html", context = context)

if __name__ =="__main__":
    app.run(debug=True)