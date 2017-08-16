import sqlite3

if __name__ == "__main__":
	#Connecting to a SQLite Database called database.db
	conn = sqlite3.connect('database.db')
	#Fetching all columns from our table named INFORMATION
	cursor = conn.execute("SELECT id, firstname, lastname, home from INFORMATION")
	#Printing header for the output
	print 'Id\tFirst Name\tLast Name\tHome'
	#Printing each individual row fetched from the database
	for item in cursor:
		print item[0],'\t',item[1],'\t',item[2],'\t',item[3]