import serial
ser = serial.Serial('/dev/ttyAMA0' , 9600)

a=0

while (a < 10):
    name_out = raw_input ("to arduino: \n")
    ser.write(name_out + "\n")
    name_return = ser.readline()
    print("from arduino: " + name_return)
    a = a+1
