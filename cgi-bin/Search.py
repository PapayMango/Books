import cgi
import cgitb
import sys
import pyodbc

cgitb.enable()

form = cgi.FieldStorage()

book = form.getfirst('title')
if book is None:
    book = "None"

print("Content-Type: text/html")
print()

print("<link href='../httpd/css/books.css' rel='stylesheet'>")
print("<title>Result</title>")
print('<p>book title</p>')

print('<p>' + book + '</p>')

print('<a href="../httpd/books.html">Back</a>')


conn_str = (
    r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
    r'DBQ=C:\xampp\htdocs\python\db\Books.accdb;'
    )
conn = pyodbc.connect(conn_str)
cursor = conn.cursor()

for table_info in cursor.tables(tableType='TABLE'):
    print(table_info.table_name)

sql = 'select * from books'
cursor.execute(sql)

for row in cursor.fetchall():
    print("<form action='Edit.py' method='get' name='form" + str(row[0]) +"'><div class='book_info' onclick='send(form" + str(row[0]) +")'><input type='hidden' value='" + str(row[0]) +"' name='id'>" + str(row) + "</div></form>")
    
print('''<script>
function send(form){
form.submit()
console.log(id)
console.log("a")
}
</script>''')

