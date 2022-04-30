import sqlite3

class Database():
	def __init__(self, dbname) -> None: 
		self.dbname = dbname
	def insert(self, table_name, values:list):
		valuesList = tuple([None] + values,)
		conn = sqlite3.connect(self.dbname)
		c = conn.cursor()
		questionMarkList = str(tuple(map(lambda _ : '?', valuesList))).replace("'", "")
		c.execute(f"INSERT INTO {table_name} VALUES {questionMarkList}", valuesList)
		conn.commit()
		conn.close()
	def getRowsWithFilter(self, table_name, filterColName:str, filterColValue):
		l = []
		conn = sqlite3.connect(self.dbname)
		c = conn.cursor()
		r = c.execute(f"SELECT * FROM {table_name} where {filterColName} = ?", (filterColValue,))
		l = [row for row in r if row[0]!=None ]
		conn.close()
		return l

	def deleteRowsWithFilter(self, table_name, filterColName=True, filterColValue=True):
		l = []
		cond = ""
		conn = sqlite3.connect(self.dbname)
		c = conn.cursor()
		if type(filterColName) == list:
			for i, n in enumerate(filterColName):
				cond = cond + n + " = " + "? " + "AND " if i != len(filterColName)-1 else cond + n + " = " + "? "
			valueTuple = tuple(filterColValue,)
		else:
			cond = cond + filterColName + " = " + "?"
			valueTuple = (filterColValue,)
		r = c.execute(f"DELETE FROM {table_name} WHERE {cond} ", valueTuple)
		conn.commit()
		conn.close()
		return l

	def updateRowsWithFilter(self, table_name, updateColName, newValue, filterColName=True, filterColValue=True):
		conn = sqlite3.connect(self.dbname)
		c = conn.cursor()
		c.execute(f"UPDATE {table_name} SET {updateColName} = ? WHERE {filterColName} = ? ;", (newValue, filterColValue))
		conn.commit()
		conn.close()

	
	def getRowsWithFilterLimit(self, table_name, filterColName:str=True, filterColValue=True, limit:int=6, offset:int=0):
		l = []
		conn = sqlite3.connect(self.dbname)
		c = conn.cursor()
		r = c.execute(f"SELECT * FROM {table_name} where {filterColName} = ? LIMIT {limit} OFFSET {offset}", (filterColValue,))
		l = [row for row in r if row[0]!=None ]
		conn.close()
		return l
	

	def insertInfo(self, table_name, id, text):
		conn = sqlite3.connect(self.dbname)
		c = conn.cursor()

		c.execute(f"INSERT INTO {table_name} VALUES (?, ?, ?)", (None, id, text)) 
		conn.commit()
		conn.close()

	def updateInfo(self, table_name, id, text):
		conn = sqlite3.connect(self.dbname)
		c = conn.cursor()
		c.execute(f"Update {table_name} set info=? where id=?",(text, id))
		conn.commit()
		conn.close()

	def insertQA(self, table_name, id, question, answer):
		conn = sqlite3.connect(self.dbname)
		c = conn.cursor()
		c.execute(f"INSERT INTO {table_name} VALUES (?, ?, ?, ?)", (None, id, question, answer)) 
		conn.commit()
		conn.close()

	def updateQA(self, table_name, id, question, answer):
		conn = sqlite3.connect(self.dbname)
		c = conn.cursor()
		c.execute(f"Update {table_name} set  = {question} where id = {id}")
		conn.commit()
		conn.close()

	def read(self, table_name):
		l = []
		conn = sqlite3.connect(self.dbname)
		c = conn.cursor()
		r = c.execute(f"SELECT * FROM {table_name}")
		l = [list(row) for row in r]
		conn.close()
		return l
		
	def readColumn(self, table_name, column_name):
		l = []
		conn = sqlite3.connect(self.dbname)
		c = conn.cursor()
		r = c.execute(f"SELECT {column_name} FROM {table_name}")
		l = [row[0] for row in r if row[0]!=None ]
		conn.close()
		return l
	def getRowById(self, table_name, id):
		l = []
		conn = sqlite3.connect(self.dbname)
		c = conn.cursor()
		r = c.execute(f"SELECT * FROM {table_name} where id = ?", (id,))
		l = [row for row in r if row[0]!=None ]
		conn.close()
		return l
	
	def cleanData(self, table_name, id):
		l = []
		conn = sqlite3.connect(self.dbname)
		c = conn.cursor()
		r = c.execute(f"DELETE FROM {table_name} WHERE id=?", (id,))
		conn.close()
		return l
	def getNumRows(self, table_name):
		conn = sqlite3.connect(self.dbname)
		c = conn.cursor()
		c.execute(f'SELECT COUNT(*) from {table_name}') 
		result = c.fetchone() 
		return result[0]
	
	def getColumnsNames(self, table_name):
		columns = []
		conn = sqlite3.connect(self.dbname)
		c = conn.cursor()
		data = c.execute(f"SELECT * FROM {table_name}")
		for col in data.description:
			columns.append(col[0])
		return columns
		


