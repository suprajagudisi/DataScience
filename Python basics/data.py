import pyodbc
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=LAPTOP-DPGHAFFU;'
                      'Database=Weekly gas price in california;'
                      'Trusted_Connection=yes;')
cursor=conn.cursor()
cursor.execute('select * from Gas_price')
rows=cursor.fetchall()
for row in rows:
    print(row)
