# pi-dht22-sh1106
Raspberry Pi with DHT22 sensor and SPI display sh1106 OLED 128x64 to show and record environment temperature, humidity, and CPU temp.

## Pre-requisites
- Python3 scripts
- Requires https://github.com/rm-hull/luma.core Luma Core library as well as Adafruit_DHT library (pip3 install Adafruit_DHT)
- Follow pi GPIO pinouts according to https://luma-oled.readthedocs.io/en/latest/hardware.html#spi for sh1106 SPI tiny display.

## Notes
- Resolution of DHT22 sensor is low, so query every few seconds. test.py queries every 5 seconds.
- (optional) Run init.py to create sqlite database if you want to use save_readings.py.
- (optional, can be used for charts and graphs) Use a cron with save_readings.py to to store periodic data. For example my crontab is every 5 minutes: 

`*/5 * * * * cd /home/pi/code/dht22_sensor && /usr/bin/python3 /home/pi/code/dht22_sensor/save_readings.py >> /var/log/dht22.log 2>&1`



