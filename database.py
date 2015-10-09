import sqlite3 as lite
import pandas as pd
con = lite.connect('getting_started.db')
cities = (('New York City','NY'),('Boston','MA'),('Chicago','IL'),('Miami','FL'),('Dallas','TX'),('Seattle','WA'),('Portland','OR'),('San Francisco','CA'),('Los Angeles','CA'),('Washington','DC'),('Houston','TX'),('Las Vegas','NV'),('Atlanta','GA'))
with con:
	cur = con.cursor()
	#only going to redo cities because weather is a lot to type
	cur.execute("DROP TABLE IF EXISTS cities")
	cur.execute("CREATE TABLE cities (name text, state text)")
	#INSERT INTO cities (name, state) VALUES ('NYC','NY');
	cur.executemany("INSERT INTO cities (name, state) VALUES (?,?)", cities)
	cur.execute("SELECT name, state, year, warm_month FROM cities INNER JOIN weather ON name = city")
	rows = cur.fetchall()
	cols=[var[0] for var in cur.description]
	df = pd.DataFrame(rows,columns=cols)

	print "The cities that have the warmest month in July are:"
	cur.execute("SELECT name, state FROM cities INNER JOIN weather ON name = city WHERE warm_month = 'July'")
	#cur.execute("SELECT * FROM weather")
	rows = cur.fetchall()
	for row in rows:
		print row
