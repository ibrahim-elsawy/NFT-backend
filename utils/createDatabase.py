import sqlite3

DBNAME="./NFT.db"
T1="users"
T2="images"


if __name__ == '__main__': 
	conn = sqlite3.connect(DBNAME) 
	c = conn.cursor() 
	c.execute(f"CREATE TABLE {T1} (i INTEGER PRIMARY KEY AUTOINCREMENT, id TEXT, email TEXT, username TEXT )") 
	c.execute(f"CREATE TABLE {T2} (i INTEGER PRIMARY KEY AUTOINCREMENT, user_id TEXT, image_url TEXT, like INTGER, year INTEGER, month INTEGER, day INTEGER, hour INTEGER, min INTEGER, FOREIGN KEY (user_id) REFERENCES users (id))") 
	c.execute(f"CREATE INDEX users_id ON {T1} (id);")
	c.execute(f"CREATE INDEX like_number ON {T2} (like);")
	conn.commit() 
	conn.close()
	
