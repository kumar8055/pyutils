Pre-requisites: Install PostgreSQL library using below command
```python
pip install psycopg2
```
## Steps for inserting one row into a PostgreSQL table
To insert a row into a PostgreSQL table in Python, you use the following steps:

First, connect to the PostgreSQL database server by calling the `connect()` function of the psycopg module.
```python
conn = psycopg2.connect(dsn)
```
The `connect()` function returns a new instance of the connection class.

Next, create a new cursor object by calling the `cursor()` method of the connection object.
```python
cur = conn.cursor()
```
Then, execute the INSERT statement with the input values by calling the `execute()` method of the cursor object.
```python
cur.execute(sql, (value1,value2))
```
You pass the INSERT statement to the first parameter and a list of values to the second parameter of the `execute()` method.

In case the primary key of the table is a `serial or identity` column, you can get the generated ID back after inserting the row.

To do this, you use the RETURNING id clause in the `INSERT` statement. After calling the execute() method, you call the  `fetchone()` method of the cursor object to get the id value like this:
```python
id = cur.fetchone()[0]
```
After that, call the `commit()` method of the connection object to permanently save the changes to the database.
```python
conn.commit()
```
If you forget to call the `commit()` method, psycopg2 will not make any changes to the table.

Finally, close the connection to the PostgreSQL database server by calling the `close()` method of the cursor and connection objects.
```python
cur.close()
conn.close()
```
