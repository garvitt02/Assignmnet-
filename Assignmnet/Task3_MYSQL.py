import mysql.connector
from mysql.connector import Error

def create_connection():
    try:
        connection = mysql.connector.connect(
            host='localhost',  
            user='root',  
            password='your_password'  #replace it with ur password
        )
        if connection.is_connected():
            print("Successfully connected to the database")
            return connection
    except Error as e:
        print(f"Error: {e}")
        return None

def create_database_and_table(connection):
    cursor = connection.cursor()
    try:
        cursor.execute("CREATE DATABASE IF NOT EXISTS student_db")
        cursor.execute("USE student_db")
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS students (
                student_id INT AUTO_INCREMENT PRIMARY KEY,
                first_name VARCHAR(255) NOT NULL,
                last_name VARCHAR(255) NOT NULL,
                age INT,
                grade FLOAT
            )
        """)
        print("Database and table created successfully")
    except Error as e:
        print(f"Error: {e}")
    finally:
        cursor.close()

def insert_student(connection):
    cursor = connection.cursor()
    try:
        cursor.execute("USE student_db")
        insert_query = """
            INSERT INTO students (first_name, last_name, age, grade)
            VALUES (%s, %s, %s, %s)
        """
        student_data = ("Alice", "Smith", 18, 95.5)
        cursor.execute(insert_query, student_data)
        connection.commit()
        print("Student record inserted successfully")
    except Error as e:
        print(f"Error: {e}")
    finally:
        cursor.close()

def update_student_grade(connection):
    cursor = connection.cursor()
    try:
        cursor.execute("USE student_db")
        update_query = """
            UPDATE students
            SET grade = %s
            WHERE first_name = %s
        """
        cursor.execute(update_query, (97.0, "Alice"))
        connection.commit()
        print("Student grade updated successfully")
    except Error as e:
        print(f"Error: {e}")
    finally:
        cursor.close()

def delete_student(connection):
    cursor = connection.cursor()
    try:
        cursor.execute("USE student_db")
        delete_query = "DELETE FROM students WHERE last_name = %s"
        cursor.execute(delete_query, ("Smith",))
        connection.commit()
        print("Student record deleted successfully")
    except Error as e:
        print(f"Error: {e}")
    finally:
        cursor.close()

def fetch_students(connection):
    cursor = connection.cursor()
    try:
        cursor.execute("USE student_db")
        select_query = "SELECT * FROM students"
        cursor.execute(select_query)
        records = cursor.fetchall()
        print("All student records:")
        for row in records:
            print(row)
    except Error as e:
        print(f"Error: {e}")
    finally:
        cursor.close()

def main():
    connection = create_connection()
    if connection:
        create_database_and_table(connection)
        insert_student(connection)
        update_student_grade(connection)
        delete_student(connection)
        fetch_students(connection)
        connection.close()

if __name__ == "__main__":
    main()
