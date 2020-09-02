import mysql.connector
import socket
import select

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1"
)

print(mydb)