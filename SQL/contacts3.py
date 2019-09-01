import sqlite3

conn = sqlite3.connect("contacts.sqlite")

name = input("Please enter a name to search for: ")



for row in conn.execute("SELECT * FROM contacts WHERE name LIKE ?", (name,)):
	print(row)
	print("=" * 40)

conn.close()



#
# person_search = input("Please enter a person's name: ")
#
# person_sql = "SELECT * FROM contacts WHERE name = ?"
#
#
# cursor = conn.cursor()
# cursor.execute(person_sql, (person_search, ""))
# print(cursor.fetchall())
