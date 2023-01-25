import psycopg2
conn = psycopg2.connect(
    host="cohort4-team5.ckokfd9swhyk.us-west-2.rds.amazonaws.com",
    #host="localhost:5432",
    database="sample",
    user="postgres",
    password="password")

cursor = conn.cursor()



cursor.execute('SELECT * FROM information_schema.tables')

rows = cursor.fetchall()
for table in rows:
    print(table)
conn.close()