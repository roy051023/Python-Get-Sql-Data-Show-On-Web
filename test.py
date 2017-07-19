import MySQLdb
import sys
import json

# Select
def select():
	cursor.execute("SELECT * FROM light")
	result = cursor.fetchall()

	data = json.dumps([{"id": r[0], "time": r[1].strftime('%Y-%m-%d %H:%M:%S'), "value": r[2]} for r in result])

	print (data)

# INSERT INTO
def insetinto():
	try:
	   cursor.execute("INSERT INTO light (value) VALUES (%d)" % (int(sys.argv[2])))
	   db.commit()
	   print (json.dumps({"result": "Success !"}))
	except:
	   db.rollback()
	   print (json.dumps({"result": "Failed !"}))

def threshold():
	cursor.execute("SELECT * FROM light")
	result = cursor.fetchall()

	data = json.dumps([{"id": r[0], "time": r[1].strftime('%Y-%m-%d %H:%M:%S'), "value": r[2], "color":  "#FF0000" if  r[2] >= int(sys.argv[2]) else "#00FF00"} for r in result])

	print (data)

if __name__ == '__main__':
	db = MySQLdb.connect(host="localhost", user="test123", passwd="test123", db="iot")
	cursor = db.cursor()
	if sys.argv[1] == '1':
		select()
	elif sys.argv[1] == '2':
		insetinto()
	elif sys.argv[1] == '3':
		threshold()

	db.close()