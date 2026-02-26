from os import name

from database import create_connection

conn=create_connection()
cursor=conn.cursor()

while True:
    print(" \n ### Student Performance Tracker ###")
    print("1 Add students")
    print("2 show students")
    print("3 update students")
    print("4 delete students")
    print("5 show topper")
    print("6 show average")
    print("7 Exit")

    choice=(input("Enter your choice: "))

    if choice=="1":
        num=int(input("how many students you want to add? "))
        for i in range(num):
            print(f"\n # Student {i+1} #")
        

            id=int(input("Enter student id: "))
            name=input("Enter student name:")
            subject=input("Enter student subject: ")
            mark=int(input("Enter student marks: "))

            sql=("INSERT INTO  student(id,name,subject,mark) VALUES (%s,%s,%s,%s)")
            values=(id,name,subject,mark)
            cursor.execute(sql,values)
            conn.commit()

            print("Students added successfully")

        print(f'\n {num} students were added')


    elif choice=="2":
        cursor.execute("SELECT * FROM student ")
        rows=cursor.fetchall()
        print("ID | Name | Subject | Marks")
        for row in rows:
            print(row)

    elif choice=="3":
        students_id=int(input("Enter student id to update: "))
        student_mark=int(input("Enter new marks: "))
        cursor.execute("Update student set marks=%s WHERE id=%s",(student_mark,students_id,))
        conn.commit()
        print("update successfully")

    elif choice=="4":
        students_id=int(input("Enter student id to delete: "))
        cursor.execute("DELETE FROM student WHERE ID=%s",(students_id,))
        print("student id deleted successfully")
        conn.commit()
        conn.commit()

    elif choice=="5":
        cursor.execute("SELECT MAX(mark) FROM student ")
        print("Topper",cursor.fetchone())

    elif choice=="6":
        cursor.execute("SELECT AVG(mark) FROM student ")
        print("Average marks",cursor.fetchone()[0])

    elif choice=="7":
        print("existing progrma")
        break

    else:
        print("invalid choice")




