from machine import*
import network
import urequests as requests
import dht
from time import*
#connect to network
sta =network.WLAN(network.STA_IF)
sta.active(True)
sta.connect('ASUS_20_2G','@7237736%')


#sign up
response=requests.post(url="http://iot.yclass.ir/sign_up.php",json={'username':'poorya','password':'09901776367'})
print(response.text)


sensor=dht.DHT11(Pin(16))
while True:
  sensor.measure()
  response=requests.post(url="http://iot.yclass.ir/send_humidity.php",json={'username':'poorya','password':'09901776367','value':sensor.humidity()})
  print(response.text)
  response=requests.post(url="http://iot.yclass.ir/send_temperature.php",json={'username':'poorya','password':'09901776367','value':sensor.temperature()})
  
  sleep(2)
