def printFileContents(myFile):
	
	print(open(myFile).read().splitlines())
	
def writeFileContents(myFile, somethingToWrite):
	f = open(myFile,'a')
	f.write(somethingToWrite +'\n') # python will convert \n to os.linesep
	f.close() # you can omit in most cases as the destructor will call if

printFileContents("alive.txt")
writeFileContents("writer.txt", "All for one!")


#Consider for Example
#def writeToDatabase():
# import pyodbc
# cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=localhost;DATABASE=testdb;UID=me;PWD=pass')
# cursor = cnxn.cursor()
# cursor.execute("select user_id, user_name from users")
# rows = cursor.fetchall()
# for row in rows:
#     print row.user_id, row.user_name