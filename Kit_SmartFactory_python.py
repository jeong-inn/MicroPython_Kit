import time
from machine import Pin, time_pulse_us
from ETboard.lib.pin_define import *
from ETboard.lib.OLED_U8G2 import *

oled = oled_u8g2()
RESET = Pin(D7)
TRIG = Pin(D9)                               
ECHO = Pin(D8)

count = 0
pre_time = 0
temp_buffer = [0] * 255

def oled_show(count) :
    global temp_buffer
    temp_buffer = "count : %d" %(count)
    oled.setLine(1, "* Smart Factory *")
    oled.setLine(2, temp_buffer) #oled에 count 표시 x
    oled.setLine(3, "--------------")
    oled.display()
    
def setup():
    RESET.init(Pin.IN)
    TRIG.init(Pin.OUT)                         
    ECHO.init(Pin.IN)                         

def loop():
    global pre_time, count
    TRIG.value(LOW)
    ECHO.value(LOW)
    time.sleep_ms(2)
    TRIG.value(HIGH)
    time.sleep_ms(10)
    TRIG.value(LOW)
    
    duration = time_pulse_us(ECHO, HIGH)
    distance = ((34 * duration) / 1000) / 2
    
    print(f'{distance : .1f}', "cm")
    time.sleep(0.1)
    
    if( distance < 10 ) :
        now_time = int(round(time.time() * 1000))
        if(now_time - pre_time > 500) :
            count += 1
            print("count : ", count)
            oled_show(count)
            time.sleep(1)
            
            pre_time = now_time;
            
    if(RESET.value() == LOW) :
        print("reset count")
        count = 0
        oled_show(count)
        print 
    
if __name__ == "__main__":
    setup()
    while True:
        loop()