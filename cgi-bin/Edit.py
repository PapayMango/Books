import cgi
import cgitb
import sys
import pyodbc
import codecs

cgitb.enable()

form = cgi.FieldStorage()

id = form.getfirst('id')

conn_str = (
    r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
    r'DBQ=C:\xampp\htdocs\python\db\Books.accdb;'
    )
conn = pyodbc.connect(conn_str)
cursor = conn.cursor()

sql = "select * from books where id = " + str(id)
cursor.execute(sql)

print("Content-Type: text/html")
print()


print(str(id))
for row in cursor.fetchall():
    print('row')

print(codecs)
html = codecs.open("./httpd/books.html",'r','utf-8').read()

print(html)
print('<a href="../httpd/books.html">Back</a>')