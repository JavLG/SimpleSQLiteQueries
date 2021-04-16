import sqlite3

def readSqliteTable(dbName):
	try:
		sqliteConnection = sqlite3.connect(dbName)
		cursor = sqliteConnection.cursor()
		print("Connected to SQLite")
		while(True):
			print("Please run your query on file (Type -1 to exit): ", dbName, end="\nMy Query: ")
			sqlite_select_query = input()
			if(sqlite_select_query == "-1"):
				return False
			cursor.execute(sqlite_select_query)
			records = cursor.fetchall()
			for row in records:
				print(row)

		cursor.close()
	except sqlite3.Error as error:
		print("Failed to read data from sqlite table", error)
	finally:
		if sqliteConnection:
			sqliteConnection.close()
			print("The SQLite connection is closed")


'''
JavLG Friday 16/04/2021: Simple sqlite queries to DB.
'''
#DB Name should be on script root directory.			
			

if __name__=="__main__":
	dbName = input("Please input DB name:  ")
	readSqliteTable(dbName)
