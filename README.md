# pi-dht22-sh1106
Raspberry Pi with DHT22 sensor and SPI display sh1106 OLED 128x64 to show and record environment temperature, humidity, and CPU temp.

## Pre-requisites
- Python3 
- Enable SPI via `raspi-config`
- Requires Luma Core and Luma OLED libraries (`pip3 install luma.core` && `pip3 install luma.oled`) as well as Adafruit_DHT library (`pip3 install Adafruit_DHT`)
- Follow pi GPIO pinouts according to https://luma-oled.readthedocs.io/en/latest/hardware.html#spi for sh1106 SPI tiny display.

## Notes
- Resolution of DHT22 sensor is low, so query every few seconds. `test.py` queries every 10 seconds.
- Use a 10k ohm resistor between 3.3v VCC pin and DAT pin
- (optional) Run `init.py` to create sqlite database if you want to use `save_readings.py`.
- (optional, can be used for charts and graphs) Use a cron with `save_readings.py` to to store periodic data. For example my crontab is every 5 minutes: 

`*/5 * * * * cd /home/pi/code/pi-dht22-sh1106 && /usr/bin/python3 /home/pi/code/pi-dht22-sh1106/save_readings.py >> /var/log/dht22.log 2>&1`

- (optional) If you want to have the display start automatically, copy `sh1106.service` to `/etc/systemd/system` 
  - Do: `systemctl daemon-reload` then `systemctl enable sh1106`
  - Make sure any running `test.py` is killed.
  - Do: `systemctl start sh1106`
  - The service will now run automatically on startup. To stop, simply do `systemctl sh1106 stop` however this does not currently blank the screen display.

![DHT Pins Diagram](/images/DHT_pins1.png)
![sh1106 screen](/images/IMG_8982.JPG)
![DHT22 on breadboard](/images/IMG_9003.JPG)

