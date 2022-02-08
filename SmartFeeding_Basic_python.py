# ******************************************************************************************
# FileName     : SmartFeeding_Basic_python
# Description  : 스마트모이 공급 코딩 키트 (기본)
# Author       : 손정인
# CopyRight    : (주)한국공학기술연구원(www.ketri.re.kr)
# Created Date : 2022.02.08 
# Reference    :
# Modified     :
# ******************************************************************************************

#import
import time
from machine import Pin
from ETboard.lib.servo import Servo
from ETboard.lib.pin_define import *

# global variable
touch_sensor = Pin(D2)                                 # 터치 센서 핀 지정
servo = Servo(Pin(D5))                                 # 서보모터 핀 지정

# setup
def setup() :
    touch_sensor.init(Pin.IN)                          # 터치센서 입력값 설정
    servo.write_angle(50)                              # 서보모터를 기본(닫힘) 상태로 초기화

# main loop
def loop() :
    touch_sensor_result = touch_sensor.value()
    
    if(touch_sensor_result == HIGH) :                  # 터치센서가 눌러졌으면
        servo.write_angle(0)                           # 서보모터를 열림 상태로 만듦
        time.sleep(2)                                  # 모이가 내려가길 2초동안 기다림
    
    else :
        servo.write_angle(50)                          # 서보모터를 기본(닫힘) 상태로 초기화

if __name__ == "__main__" :
    setup()
    while True :
        loop()

# ==========================================================================================
#
#  (주)한국공학기술연구원 http://et.ketri.re.kr
#
# ==========================================================================================