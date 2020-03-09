import pymysql

connection = pymysql.connect(host='127.0.0.1',
							 user='root',
							 password='root',
							 db='pyproject',
							 cursorclass = pymysql.cursors.DictCursor)

try:
	with connection.cursor() as cursor:

		# SQL
		sql = "SELECT * FROM log"

		# Выполнить команду запроса (Execute Query).
		cursor.execute(sql)
		print("cursor.description: ", cursor.description)
		print()
		for row in cursor:
			print(row)
finally:
	# Закрыть соединение (Close connection).
	connection.close()
