import serial
import pyvjoy
import time

joy = pyvjoy.VJoyDevice(1)
encoder = serial.Serial('COM14', 9600)

time.sleep(2) #wait for serial and vjoy to come up


while True:
#angle from arduino    
    raw_enc_position = float(encoder.readline())
#translate encoder degree to usable vjoy range
    translated_joystick_position = int((int(raw_enc_position) / 360) * 32768)
#Send computed value to virtual joystick
    joy.set_axis(pyvjoy.HID_USAGE_X, translated_joystick_position)



#debug
    print(translated_joystick_position)
    
