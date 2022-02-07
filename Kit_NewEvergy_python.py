import time
from machine import Pin, ADC
from ETboard.lib.OLED_U8G2 import *
from ETboard.lib.pin_define import *

oled = oled_u8g2()
solar = ADC(Pin(A3))
windturbine = ADC(Pin(A5))

text1 = [0] * 31
text2 = [0] * 31

def setup() :
    #solar.init(Pin.IN)
    #windturbine.init(Pin.IN)
    solar.atten(ADC.ATTN_11DB)
    windturbine.atten(ADC.ATTN_11DB) 
    
def loop() :
    display_oled()
    time.sleep(1)

def setup_oled() :
    SDA.init(Pin.IN)
    SCL.init(Pin.IN)
    
def display_oled() :
    solar_voltage_value = solar.read()
    windturbine_voltage_value = windturbine.read()

    print("태양광 센서 : ", solar_voltage_value)
    print("풍력 센서 : ", windturbine_voltage_value)
    print("-------------------");

    text1 = "s : %d V" %(solar_voltage_value)
    text2 = "w : %d V" %(windturbine_voltage_value)
    
    oled.clear()
    oled.setLine(1, "* ECO Energy *")
    oled.setLine(2, text1)
    oled.setLine(3, text2)
    oled.display()

if __name__ == "__main__" :
    setup()
    while True :
        loop()
