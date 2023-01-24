import psycopg2

#pyscopg2 - this is a library that helps me connect to a postgres database
#from Python


# this connects to the Docker container running postgres:
conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="test")

#we use cursor so that we can run some SQL
cursor = conn.cursor()

#this is a sanity check - to verfiy that we are indeed connected to postgres:
cursor.execute('SELECT * FROM information_schema.tables')


#now that you have a cursor, you can insert into your DB, retrieve, etc..


rows = cursor.fetchall()
for table in rows:
    print(table)
conn.close()

