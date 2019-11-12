# Communication using Bluetooth between Raspberry Pi and Arduino
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) [![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/dwyl/esta/issues) [![Python 2.7](https://img.shields.io/badge/python-2.7-blue.svg)](https://www.python.org/downloads/release/python-270/) [![HitCount](http://hits.dwyl.io/sayederfanarefin/iot-python-raspberry-pi-arduino-bluetooth-communication.svg)](http://hits.dwyl.io/sayederfanarefin/iot-python-raspberry-pi-arduino-bluetooth-communication)

The project is mainly to communicate between arduino and raspberry pi over bluetooth (HC05)

## Components:
1. [Arduino Uno](https://www.amazon.com/Arduino-Development-Microcontroller-ATmega328-ATMEGA16U2/dp/B07V9VGXFS/ref=sr_1_8?keywords=arduino+uno&qid=1573429666&sr=8-8) 1 pcs
2. [Raspberry Pi](https://www.amazon.com/Raspberry-Model-2019-Quad-Bluetooth/dp/B07TC2BK1X/ref=sr_1_3?keywords=raspberry+pi&qid=1573429739&sr=8-3) 1 pcs
3. [Bluetooth module HC05](https://www.amazon.com/HiLetgo-Bluetooth-Transceiver-Integrated-Communication/dp/B07VL725T8/ref=sr_1_2?keywords=bluetooth+module+hc05&qid=1573429855&sr=8-2) 2 pcs

## Arduino part:
I connected the Bluetooth module’s rx to 11, tx to 10 and gn to gnd and vcc to 5v. The en pin was also HIGH (applying 3.3V) Then I powered up the arduino and also the Bluetooth module. Then I uploaded this code to Arduino:


```
#include <SoftwareSerial.h>
 
SoftwareSerial mySerial(10, 11); 
 
void setup()
{
  // Open serial communications and wait for port to open:
  Serial.begin(9600);
  while (!Serial) {
    ; // wait for serial port to connect. Needed for Leonardo only
  }
 
  Serial.println("Ready!");
 
  // set the data rate for the SoftwareSerial port
 
  // for HC-05 use 38400 when poerwing with KEY/STATE set to HIGH on power on
  mySerial.begin(38400);
}
 
void loop() // run over and over
{
  if (mySerial.available()){
    Serial.write(mySerial.read());
  }
  if (Serial.available()){
    mySerial.write(Serial.read());
  }
}
```
 I opened the serial monitor And using the "AT" command I set the name and also the Bluetooth module to Master. I used these commands to do so :
"AT+NAME=ER" (for name)
"AT+ROLE=1" (for Master)
Then I bind this module with the other Bluetooth module using its Mac address. The command was:
"AT+BIND= (mac of the Bluetooth connected with arduino)"
Now, whenever both of the modules are on these two modules will automatically pair. 

## Raspberry Pi part:
Firstly, I connected the Pi to my router and an IP was assigned to the Pi using the router's DHCP. Then I figured out the Pi's assigned address using the router's admin panel, and used "Putty" to connect to Pi over ssh using the IP address.
 Then I connect the Bluetooth module's rx to pi's tx pin and Bluetooth module's tx pin to pi's rx pin. 
Since this module is capable of communicating using the serial, so I connected it with the Pi's serial pins. Then I installed "" package in order to communicate with the Bluetooth. And wrote this script in python:

```
import serial
ser = serial.Serial('/dev/ttyAMA0' , 9600)

a=0

while (a < 10):
    name_out = raw_input ("to arduino: \n")
    ser.write(name_out + "\n")
    name_return = ser.readline()
    print("from arduino: " + name_return)
    a = a+1

```

The Bluetooth module was in slave mode.
Then I browse to that directory using the Linux commands and then ran that script.

Ref: http://blog.miguelgrinberg.com/post/a-cheap-bluetooth-serial-port-for-your-raspberry-pi


Integration of the both parts: 
Now the modules get connected automatically whenever both of them are up. One thing about the HC05 is whenever they are paired the blinking of the led of the Bluetooth module gets slower as in it blinks in every 2sec, and if it is not paired it blinks in every second. And I tried to connect with those individually using my phone's Bluetooth but since they are already paired, both of them refused my Phone's Bluetooth connection prompt.
The I send some data from the serial monitor of the arduino and that data showed up in putty which was connected with the Pi. I did it vise versa and it worked!

![alt text](https://github.com/sayederfanarefin/iot-python-raspberry-pi-arduino-bluetooth-communication/blob/master/IMG_20151025_020431.jpg)


For further help you can contact me via email: erfanjordison@gmail.com
