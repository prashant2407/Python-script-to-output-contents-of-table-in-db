import sqlite3

if __name__ == '__main__':
	#Connecting to a SQLite Database called database.db
	conn = sqlite3.connect('database.db')
	#Checking if there is a table already existing with the name Information
	result = conn.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='INFORMATION';")
	if len(result.fetchall()) == 0:
		#If table does not exist, creating the table
		conn.execute('''CREATE TABLE INFORMATION
		         (ID INT PRIMARY KEY     NOT NULL,
		         FIRSTNAME           TEXT    NOT NULL,
		         LASTNAME            TEXT,
		         HOME        TEXT);''')
		#Inserting Data into the Table
		conn.execute("INSERT INTO INFORMATION (ID,FIRSTNAME,LASTNAME,HOME) VALUES (1, 'Rose', 'Tyler', 'Earth')");
		conn.execute("INSERT INTO INFORMATION (ID,FIRSTNAME,LASTNAME,HOME) VALUES (2, 'Zoe', 'Heriot', 'Space Station W3')");
		conn.execute("INSERT INTO INFORMATION (ID,FIRSTNAME,LASTNAME,HOME) VALUES (3, 'Jo', 'Grant', 'Earth')");
		conn.execute("INSERT INTO INFORMATION (ID,FIRSTNAME,LASTNAME,HOME) VALUES (4, 'Leela', null, 'Unspecified')");
		conn.execute("INSERT INTO INFORMATION (ID,FIRSTNAME,LASTNAME,HOME) VALUES (5, 'Romana', null, 'Gallifrey')");
		conn.execute("INSERT INTO INFORMATION (ID,FIRSTNAME,LASTNAME,HOME) VALUES (6, 'Clara', 'Oswald', 'Earth')");
		conn.execute("INSERT INTO INFORMATION (ID,FIRSTNAME,LASTNAME,HOME) VALUES (7, 'Adric', null, 'Alzarius')");
		conn.execute("INSERT INTO INFORMATION (ID,FIRSTNAME,LASTNAME,HOME) VALUES (8, 'Susan', 'Foreman', 'Gallifrey')");
		#Persisting data into the table
		conn.commit()
	#Closing the Connection to the Database
	conn.close()