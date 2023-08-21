import dht
from time import sleep
import time
from machine import Pin
import network
import socket
sensor = dht.DHT11(Pin(16))


ssid = 'replace with ssid'
pw = 'replace with password'
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, pw)
html = """
<html>
    <head> <title>Pico Web Server</title> </head>
    <body>
        <h2>the temprature is %s degrees celsuis</h2>
        
    </body>
</html>
"""
max_wait = 10
while max_wait > 0:
    if wlan.status() < 0 or wlan.status() >= 3:
        break
    max_wait -= 1
    print('waiting for connection...')
    time.sleep(1)

if wlan.status() != 3:
    raise RuntimeError('network connection failed')
else:
    print('connected')
    status = wlan.ifconfig()
    print( 'ip = ' + status[0] )
    
    
addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]

s = socket.socket()
s.bind(addr)
s.listen(1)
print('listening on', addr)
 


while True:
  try:
    cl, addr = s.accept()
    print('client connected from', addr)
    request = cl.recv(1024)
    print(request)
        
    sleep(1)
    sensor.measure()
    temp = sensor.temperature()
    hum = sensor.humidity()
    temp_f = temp * (9/5) + 32.0
    print('Temperature: %3.1f C' %temp)
    print('Temperature: %3.1f F' %temp_f)
    print('Humidity: %3.1f %%' %hum)
    response = html % temp
    cl.send('HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n')
    cl.send(response)
    cl.close()
  except OSError as e:
    cl.close()
    print('connection closed')

