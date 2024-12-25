import psycopg2
conn = None
try:
    conn = psycopg2.connect(
    dbname = "practice",
    user = "postgres",
    password = "9849647940",
    host = "localhost",
    port = 5433
    )
    conn.autocommit = True
    print("Connection Succesful")
    cursor = conn.cursor()
    insert = """
    Insert into INFO (id, fname, lname, age) 
    values(1,'Akin','Nanju',20),
    (2,'Bagish','Gautam',10),
    (3,'Prajwal','Shrestha',20),
    (4,'John','Vector',22),
    (5,'Bisham','Shrestha',20)
    """
    cursor.execute(insert)
    print("Data Inserted Successfully")
finally:
    if conn:
        conn.close()
        print("PostgreSQL connection is closed")