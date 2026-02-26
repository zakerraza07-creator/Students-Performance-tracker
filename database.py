import mysql.connector

def create_connection():
    con=mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="raza@123",
        database="student_db"
    )
    return con
