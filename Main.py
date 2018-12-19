#init connection
#import DBHelper.py to use connection function
conn = get_db_connection()
cursor = conn.cursor()

#Script for Select
cursor.execute('SELECT * FROM customers LIMIT 100')
for row in cursor:
    print(row)

#Script for Delete
cursor.execute('DELETE FROM customers where id = 189')

#Script for Update
cursor.execute('UPDATE customers SET first_name="qyara" where id = 16')

#Script for Insert
cursor.execute("INSERT INTO customers values(199,'azda','firmansyah','zzzz@aaa.com')")

conn.close()
