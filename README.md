# GreenHouseTempMonitor
<h1>Made by Kevin Ayad - ka223hr<br></h1>
This is an IOT project to measure and monitor temperature and humidity in greenhouses to help farmers take better care of their crops and produce higher-quality fruits, veggies, and herbs.
<br>An individual with a beginner to intermediate understanding of IOT shall be able to set up this project in under 2 hours.
<h1>Objective</h1>
This project will help farmers understand the temperature and humidity of their greenhouses to take better care of their plants, this information will let them know how to water and treat the plants differently based on the temperature and humidity.<br> Furthermore this project could be further improved by adding a feature that triggers a watering system to the plants upon user request, possibly after receiving a notification of increased temperature in real-time.<br>
<h1>needed material</h1>
<ol>
  <li>DHT11 temprature sensor, cost 55sek, https://www.amazon.se/AZDelivery-temperatursensor-fuktighetssensor-kompatibel-Raspberry/dp/B07TYPT2NJ/ref=asc_df_B07TSF9G8L/?tag=shpngadsglede-21&linkCode=df0&hvadid=476437577955&hvpos=&hvnetw=g&hvrand=15908554601659101393&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=1012583&hvtargid=pla-1620771794554&th=1</li>
  <li>raspberry pi pico w, cost 165 sek, https://www.amazon.se/Waveshare-Pico-Microcontroller-Pre-soldered-Header/dp/B0BN5YT8W6/ref=sr_1_1?keywords=raspberry+pi+pico+w&qid=1692647693&sprefix=raspberry+pi+p%2Caps%2C172&sr=8-1</li>
  <li>Jumper cables, resistors and a breadboard, cost 161 sek, https://www.amazon.se/Electronic-Assortment-Breadboard-Transistors-JIANNI/dp/B0BW3R38PW/ref=sr_1_1?crid=1H2ZR0AYBZUNL&keywords=jumper+cables+and+resistors&qid=1692647765&sprefix=jumper+cables+and+resist%2Caps%2C135&sr=8-1</li>
</ol>

<h1>Computer setup</h1>
I used Thonny ide and micropython to develop and upload the code onto the raspberry pi pico w<br>
![Screenshot 2023-08-21 at 21 59 10](https://github.com/Kevinayad/GreenHouseTempMonitor/assets/49120270/e55065d2-f2d3-407e-af29-54da6efa1064)
I simply connect the raspberry pi to my computer then save the main.py file that includes the code into the raspberry pi then flash it and run it.

<h1>electronics connection</h1>
The electronics are connected using a breadboard and then communicating with the dht11 sensor through pin 16 of the pico w, in addition connecting the DHT11 to ground and 3.3 v power through a resistor from the pico w.
the following picture shows how they are connected in reality.
![tempImagemoc76F](https://github.com/Kevinayad/GreenHouseTempMonitor/assets/49120270/2be5088a-348a-4997-b5be-83666ec3caa1)

<h1>Platform</h1>
I chose to use a local web server over widi since it allows me to connect quickly to the device using the built in wifi on pico w by using my home network by just using an ip address in the browser on any device, plus for the future it is scalable by just having a vpn of that network on lets say a phone so we can connect remotly to the device over the internet with no need to update the code.

<h1><\h1>







