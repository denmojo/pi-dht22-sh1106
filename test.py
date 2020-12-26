import os
import platform
import time
import Adafruit_DHT

from luma.core.interface.serial import spi
from luma.core.render import canvas
from luma.oled.device import sh1106
from time import sleep

DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4
serial = spi(device=0, port=0)
device = sh1106(serial)

def get_cpu_temp():
    result = 0.0
    if os.path.isfile('/sys/class/thermal/thermal_zone0/temp'):
        with open('/sys/class/thermal/thermal_zone0/temp') as f:
            line = f.readline().strip()
        if line.isdigit():
            result = float(line) / 1000

    return result


while True:
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
    if temperature is not None:
        temp = "Temp:     {0:0.1f}*F".format(((temperature * 1.8) + 32))
    else: 
        temp = "Temp: Read Err"
    if humidity is not None:
        hum = "Humidity: {0:0.1f}%".format(humidity)
    else:
        hum = "Humidity: Error"
    currTime = "Time:   " + time.strftime('%H:%M:%S', time.localtime(time.time()))
    cpuTemp = "CPU:      {0:0.1f}*C".format(get_cpu_temp()) 
    print(currTime + " " + temp + " " + hum + " " + cpuTemp)

    with canvas(device) as draw:
        draw.rectangle(device.bounding_box, outline="white", fill="black")
        draw.text((15, 10), currTime, fill="white")
        draw.text((15, 20), temp, fill="white")
        draw.text((15, 30), hum, fill="white")
        draw.text((15, 40), cpuTemp, fill="white")
    sleep(10)
