import time
from machine import Pin, time_pulse_us, ADC
from ETboard.lib.pin_define import *
from ETboard.lib.OLED_U8G2 import *

led1 = Pin(D2)
led2 = Pin(D3)
TRIG = Pin(D9)                               
ECHO = Pin(D8)
#cds = ADC(Pin(A1))
cds = Pin(A3)

def setup():
    TRIG.init(Pin.OUT)                         
    ECHO.init(Pin.IN)                         
    led1.init(Pin.OUT)
    led2.init(Pin.OUT)
    #cds.atten(ADC.ATTN_11DB)
    cds.init(Pin.IN)
def loop():
    TRIG.value(LOW)
    ECHO.value(LOW)
    time.sleep_ms(2)
    TRIG.value(HIGH)
    time.sleep_ms(10)
    TRIG.value(LOW)
    
    duration = time_pulse_us(ECHO, HIGH)
    distance = ((34 * duration) / 1000) / 2
    cdsValue = (cds.value()) / 10
    
    if( distance < 10 ) :
        led1.value(HIGH)
    else :
        led1.value(LOW)
        
    print(" 초음파 센서  : ", distance)
    print("-----------------------")
    
    if( cdsValue < 300 ) :
        led2.value(HIGH)
    else :
        led2.value(LOW)
    
    print(" 조도 센서  : ", cdsValue)
    print("-----------------------")
    
    time.sleep(0.1)                                


if __name__ == "__main__":
    setup()
    while True:
        loop()
        