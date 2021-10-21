import psycopg2

conn = psycopg2.connect(host="localhost", port = 5342, database="db_name", user="user", password="password")

def insert_one():
    ### Insert into emp_table
    sql = """INSERT INTO test_employee(emp_id,emp_name) VALUES(%s,%s);""" 
    try:
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.execute(sql,(1,'emp_1'))
        cur.execute(sql,(2,'emp_2'))
        #
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print("Exception occured in insert_one",error)

def insert_many():
    ##Prepare a SQL statement
    sql = "INSERT INTO test_employee(emp_id,emp_name) VALUES(%s,%s)"
    try:
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        employee_list = [
            (3,'Mike'),
            (4,'John'),
            (5,'Sehari'),
            (6,'Hero'),
        ]
        cur.executemany(sql,employee_list)
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print("Exception occured in insert_many",error)

def fetch_data():
    try:
        # Create a cursor object
        cur = conn.cursor()
        # A sample query of all data from the "vendors" table in the "suppliers" database
        cur.execute('''SELECT * from "test_employee"''')
        query_results = cur.fetchall()
        print(query_results)
        # Close the cursor and connection to so the server can allocate
        # bandwidth to other requests
        cur.close()
        conn.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print("Exception occured in fetch_data",error)
    finally:
        if conn is not None:
            conn.close()

if __name__=="__main__":
    insert_one()
    insert_many()
    fetch_data()