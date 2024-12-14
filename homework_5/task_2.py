import psycopg2
import dotenv
import os

dotenv.load_dotenv('.env')

host = os.getenv('HOST')
port = os.getenv('PORT')
dbname = os.getenv('DBNAME')
user = os.getenv('USER')
password = os.getenv('PASSWORD')

conn = psycopg2.connect(host=host,
                        port=port,
                        dbname=dbname,
                        user=user,
                        password=password)
cursor = conn.cursor()

query = 'SELECT MIN(unit_price) AS min_price FROM products '\
        'WHERE category_id=1;'

cursor.execute(query)

for row in cursor.fetchall():
    print(row)

cursor.close()
conn.close()
