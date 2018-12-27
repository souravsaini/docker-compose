from peewee import *

db = MySQLDatabase(
	'flaskappdb',
	host='db',
	port=3306,
	user='root',
	password='root'
)
db.connect()