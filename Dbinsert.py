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
    cursor = conn.cursor()
    create = """
    Create Table INFO (
        id int primary key not null,
        fname varchar(40),
        lname varchar(40),
        age int)
        """
    cursor.execute(create)
    print("Table created successfully")
finally:
    if conn:
        conn.close()