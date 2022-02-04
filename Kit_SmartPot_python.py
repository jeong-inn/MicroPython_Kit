import time
from machine import Pin, ADC
from ETboard.lib.OLED_U8G2 import *
from ETboard.lib.pin_define import *

oled = oled_u8g2()
moisture = ADC(Pin(A3))
pin1 = Pin(D3)
pin2 = Pin(D4)

def setup() :
    moisture.atten(ADC.ATTN_11DB)
    pin1.init(Pin.OUT)
    pin2.init(Pin.OUT)
    
def loop() :
    result = moisture.read()
    moistureValue = 4095 - result
    
    print("토양 수분 센서값 : ", moistureValue)
    print("-----------------")
    time.sleep(0.1)
    '''
    if(moistureValue < 300) :
        pin1.value(HIGH)
        pin2.value(LOW)
    else :
        pin1.value(LOW)
        pin2.value(LOW)       
    
    #text[32] = moistureValue
    
    oled.setLine(1, "* Smart POT *")
    oled.setLine(2, moistureValue)
    '''
    oled.setLine(3, "---------")
    oled.display()
    
if __name__ == "__main__" :
    setup()
    while True :
        loop()