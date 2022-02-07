import time
from machine import Pin
from ETboard.lib.servo import Servo
from ETboard.lib.pin_define import *

touch_sensor = Pin(D2)
servo = Servo(Pin(D5))

def setup() :
    touch_sensor.init(Pin.IN)

def loop() :
    result = touch_sensor.value()
    
    if(result == HIGH) :
        servo.write_angle(0)
        time.sleep(2)
    
    else :
        servo.write_angle(50)

if __name__ == "__main__" :
    setup()
    while True :
        loop()