import time
from machine import Pin
from ETboard.lib.OLED_U8G2 import *
from ETboard.lib.pin_define import *

c_value = 0.001221245421
oled = oled_u8g2()

def setup() :
    pass

def loop() :
    display_oled()
    time.sleep(1)

def setup_oled() :
    SDA.init(Pin.IN)
    SCL.init(Pin.IN)
    
def display_oled() :
    solar_voltage_value = Pin(A3).read()
    print("태양광 센서 : ", solar_voltage_value)

    text1[32] = "S : "
    value1[32]
    str1 = str(solar_voltage_value * c_value)
    
    text1 = text1 + value1
    text1 = text1 + "V"
    list1 = list(str1)
    windturbine_voltage_value = Pin(A5).read()
    print("풍력 센서 : ", windturbine_voltage_value)
    print("-------------------");

    text2[32] = "W : "
    value2[32]
    str2 = Str(windturbine_voltage_value * c_value)
    list2 = list(str2)
    text2 = text2 + value2
    text2 = text2 + "V"

    oled.setLine(1, "* ECO Energy *")
    oled.setLine(2, text1)
    oled.setLine(3, text2)
    oled.display()

if __name__ == "__main__" :
    setup()
    while True :
        loop()
