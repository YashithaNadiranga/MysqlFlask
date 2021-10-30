import mysql.connector
from collections import namedtuple
from mysql.connector.connection import MySQLConnection

Student = namedtuple("Student","id name dob grade address parent_name")

class StudentRecordHelper:
    db : MySQLConnection

    def __init__(self,db):
        self.db = db

    def get_all(self):
        cur =self.db.cursor()
        sql = "SELECT * From student"
        cur.execute(sql)
        results = cur.fetchall()
        students = []
        for re in results:
            st = Student(*re)
            students.append(st)
        return students


def connect_db() -> MySQLConnection:
    return mysql.connector.connect(
    host="localhost",
    user = "root",
    password="1234",
    database="ijse_db"
)