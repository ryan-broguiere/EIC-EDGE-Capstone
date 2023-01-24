import psycopg2
import mysql.connector

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

# connectsql = mysql.connector.connect(user='postgres', database='capstone')
# cursor = connectsql.cursor()

# cursor.execute(
#     "CREATE TABLE address ("
#         "ID SERIAL PRIMARY KEY,"
#         "Address VARCHAR(50),"
#         "City VARCHAR(25),"
#         "State VARCHAR(25),"
#         "ZipCode VARCHAR(5)"
#     ");"

#     "CREATE TABLE customer ("
#         "ID SERIAL PRIMARY KEY,"
#         "FirstName VARCHAR(25),"
#         "LastName VARCHAR(25),"
#         "AddressID INT REFERENCES address(ID),"
#         "Email VARCHAR(50)"
#     ");"

#     "CREATE TABLE account ("
#         "ID SERIAL PRIMARY KEY,"
#         "AccountNumber VARCHAR(10),"
#         "CustomerID INT REFERENCES customer(ID),"
#         "CurrentBalance FLOAT"
#     ");")

#now that you have a cursor, you can insert into your DB, retrieve, etc..


rows = cursor.fetchall()
for table in rows:
    print(table)
conn.close()

