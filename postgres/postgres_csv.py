#!/usr/bin/python

import psycopg2
import csv

conn = psycopg2.connect(host="localhost", port = 5342, database="db_name", user="user", password="password")

def custom_insert(sql_query,src_file):
    ##Prepare a SQL statement
    sql = sql_query
    try:
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        with open(src_file,'r') as csv_file:
            csv_data = csv.reader(csv_file)
            ## iterate csv rows and insert into table
            for row in csv_data:
                cur.execute(sql,datarow)
            # commit the changes to the database
            conn.commit()
            # close communication with the database
            cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print("Exception occured",error)
    finally:
        if conn is not None:
            conn.close()

def csv_insert():
    ## Prepare a SQL Query, (%s,%s) -- number of values you are passing as strings
    ## ex: INSERT INTO test_employee(emp_id,emp_name) VALUES(1,'Mike')
    sql = "INSERT INTO test_employee(emp_id,emp_name) VALUES(%s,%s)"
    csv_file = "/apps/disk7/elastic_monitoring/final_scripts/misc/postgresconnect/emp_list.csv"
    ## Call custom insert function to load postgres table
    custom_insert(sql,csv_file)


if __name__ =="__main__":
    csv_insert()
