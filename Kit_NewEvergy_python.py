# ******************************************************************************************
# FileName     : NewEnergy_Basic_python
# Description  : 빨강 LED 가 켜졌다 꺼졌다 반복
# Author       : 이승찬
# Created Date : 2021.08.19
# Reference    :
# Modified     :
# ******************************************************************************************


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
    solar.atten(ADC.ATTN_11DB)
    windturbine.atten(ADC.ATTN_11DB) 
    
def loop() :
    display_oled()
    time.sleep(1)

def setup_oled() :
    SDA.init(Pin.IN)
    SCL.init(Pin.IN)
    
def display_oled() :
    solar_voltage_value = solar.read()# 태양광 발전량 측정 센서
    windturbine_voltage_value = windturbine.read() # 풍력 발전량 측정 센서

    print("태양광 센서 : ", solar_voltage_value)
    print("풍력 센서 : ", windturbine_voltage_value)
    print("-------------------");

    text1 = "s : %d V" %(solar_voltage_value)
    text2 = "w : %d V" %(windturbine_voltage_value)
    
    oled.clear()
    oled.setLine(1, "* ECO Energy *")# OLED 첫 번째 줄 : 시스템 이름
    oled.setLine(2, text1) # OLED 두 번째 줄 : 태양광 발전량
    oled.setLine(3, text2)# OLED 세 번째 줄 : 풍력 발전량
    oled.display()

if __name__ == "__main__" :
    setup()
    while True :
        loop()

#=========================================================================================
#
# (주)한국공학기술연구원 http://et.ketri.re.kr
#
#=========================================================================================
