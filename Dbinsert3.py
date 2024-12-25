import psycopg2
conn = None
try:
    conn = psycopg2.connect(
        dbname = 'practice',
        user = 'postgres',
        password = '9849647940',
        host = 'localhost',
        port = 5433
    )
    conn.autocommit = True
    print('Connection Succesful')
    cursor = conn.cursor()
    insert = """Insert into info(id, fname, lname, age)
    VALUES(%s, %s, %s, %s)
    """
    data = [
        (6,'Alice', 'Johnson', 25),
        (7,'Bob', 'Smith', 30),
        (8,'Charlie', 'Davis', 35),
        (9,'David', 'Martinez', 40),
        (10,'Eva', 'Lee', 45)
    ]
    cursor.executemany(insert, data)
    print("Successfully inserted")
finally:
    if conn:
        conn.close()
    
    