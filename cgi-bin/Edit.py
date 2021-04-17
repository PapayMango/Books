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

print("<link href='../httpd/css/books.css' rel='stylesheet'>")
print("<title>Edit</title>")

print(str(id))
for row in cursor.fetchall():
    create_book_info(row)

# print(codecs)
# html = codecs.open("./httpd/books.html",'r','utf-8').read()

# print(html)
print('<a href="../httpd/books.html">Back</a>')
print('<script></script>')

def create_book_info(array):
    print('<div class="book_info">')
    print("<h2>"+str(array[1])+"</h2>")
    print("<div>"+str(array[2])+"</div>")
    print("<img src='../httpd/images/trash.png' border='0' width='30' height='30'>")
    print('/<div>')



