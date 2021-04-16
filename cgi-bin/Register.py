import cgi
import cgitb
import sys
import pyodbc

cgitb.enable()

form = cgi.FieldStorage()

title = str(form.getfirst('title'))
location = str(form.getfirst('location'))

print("Content-Type: text/html")
print()

print('<p>book title</p>')

print(title)
print(location)

print('<a href="../httpd/books.html">Back</a>')

conn_str = (
    r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
    r'DBQ=C:\xampp\htdocs\python\db\Books.accdb;'
    )
conn = pyodbc.connect(conn_str)
cursor = conn.cursor()

# sql = "INSERT INTO books(Title,Location) VALUES(" + str(title) +","+ str(location) + ")"
sql = "INSERT INTO books (Title,Location) VALUES('" + title + "','" +  location + "');"
cursor.execute(sql)
cursor.commit()

cursor.close()
conn.close()