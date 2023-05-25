import psycopg2


db = "dbname='postgres' user='postgres' host='127.0.0.1' password = 'postgresPassword'"
conn = psycopg2.connect(db)
cursor = conn.cursor()

cursor.execute("SELECT * FROM Laptops WHERE Company = 'Apple';")
tuple_resultset = cursor.fetchall()
cursor.close()

for result in tuple_resultset:
    print(result)