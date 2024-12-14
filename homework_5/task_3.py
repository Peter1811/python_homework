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

query = 'SELECT supplier_id, MAX(unit_price) FROM products ' \
        'WHERE supplier_id IN (1, 3, 5) ' \
        'GROUP BY supplier_id;' \

cursor.execute(query)

rows = cursor.fetchall()

for row in rows:
    print(row)

cursor.close()
conn.close()
