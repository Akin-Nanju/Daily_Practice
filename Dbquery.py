import psycopg2
conn = None
try:
    conn = psycopg2.connect(
        dbname="practice",
        user="postgres",
        password="9849647940",
        host="localhost",
        port=5433
    )
    conn.autocommit = True
    print("Connection Succesful")
    print()
    cursor = conn.cursor()
    sele = "Select id, fname, lname, age from info WHERE id = 1"
    cursor.execute(sele)
    result = cursor.fetchone()
    print(f"id:{result[0]}, fname:{result[1]},lname:{result[2]}, age:{result[3]}")
    print()
    print("NOW TRYING TO FETCH ALL DATA FROM DATABSE")
    sel = "SELECT * FROM info"
    cursor.execute(sel)
    row = cursor.fetchall()
    for row in row:
        print(f"id:{row[0]}, fname:{row[1]},lname:{row[2]}, age:{row[3]}")
        print()
finally:
    if conn:
        cursor.close()
        conn.close()
        print("Connection Closed")