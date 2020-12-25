import time
import sqlite3
import Adafruit_DHT

DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4



try:
    sqliteConnection = sqlite3.connect('dht22_readings.db')
    cursor = sqliteConnection.cursor()
    print("Successfully connected to SQLite %s" % time.asctime(time.localtime(time.time())))

    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
    tempf = (temperature * 1.8) + 32
        
    count = cursor.execute("INSERT INTO sensor_readings (ftemp, humidity, created_date) values (%s, %s, %s)" % (str(tempf), str(humidity), time.time()))
    sqliteConnection.commit()
    print("Record inserted ", cursor.rowcount)
    cursor.close()

except sqlite3.Error as e:
    print("Failed to insert data into sqlite table", str(e))
finally:
    if (sqliteConnection):
        sqliteConnection.close()
        print("SQLite connection closed")


