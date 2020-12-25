import sqlite3

conn = sqlite3.connect("dht22_readings.db")
c = conn.cursor()

c.execute("CREATE TABLE IF NOT EXISTS sensor_readings (id INTEGER PRIMARY KEY AUTOINCREMENT, ftemp TEXT, humidity TEXT, created_date TEXT)")

conn.close()

