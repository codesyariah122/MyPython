import mysql.connector
from getpass import getpass

def connection():

	host = 'localhost'
	user = input('Username : ')
	passwd = getpass('Password : ')

	if user != "" and passwd != "":

		cnx = mysql.connector.connect(
				host = host,
				user = user,
				password = passwd
			)

		if cnx.is_connected():
			print("Connection Success")
	else:
		print("Login harus diisi")
		
	cnx.close()