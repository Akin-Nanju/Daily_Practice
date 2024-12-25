import psycopg2
conn = None
try:
    conn = psycopg2.connect(
        dbname = 'practice',
        user = 'postgres',
        password = '9849647940',
        host = 'localhost',
        port = '5433'
    )
    conn.autocommit = True
    print('Connection Succesful')
finally:
    if conn:
        conn.close()