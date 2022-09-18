import RPi.GPIO as GPIO
import time
import sys
import random

global gGPIOnum

#設定腳位輸出頻率
def Setup(GPIOnum, frequency):
    global gGPIOnum
    GPIO.setmode(GPIO.BCM)
    gGPIOnum = GPIOnum
    GPIO.setup(gGPIOnum, GPIO.OUT)
    gGPIOnum = GPIO.PWM(gGPIOnum, frequency)
    gGPIOnum.start(0)

#開燈
def TurnOnLED(GPIOnum):
    GPIO.output(GPIOnum, True)

#關燈
def TurnOffLED(GPIOnum):
    GPIO.output(GPIOnum, False)


if __name__ == "__main__":
    while True:
        #玩家出拳
        ans = input('Paper~Scissors~Stone~：')
        #出石頭(顯示stone!)，紅燈漸亮到漸暗
        if ans == '0':
            print('stone!')
            Setup(4, 100)
            #設定燈泡亮度調節:漸亮漸暗
            for dc in range(0, 101, 5):
                gGPIOnum.ChangeDutyCycle(dc)
                time.sleep(0.1)
            for dc in range(100, -1, -5):
                gGPIOnum.ChangeDutyCycle(dc)
                time.sleep(0.1)

        # 出剪刀(顯示scissors!)，黃燈漸亮到漸暗
        elif ans == '2':
            print('scissors!')
            Setup(3, 100)
            # 設定燈泡亮度調節:漸亮漸暗
            for dc in range(0, 101, 5):
                gGPIOnum.ChangeDutyCycle(dc)
                time.sleep(0.1)
            for dc in range(100, -1, -5):
                gGPIOnum.ChangeDutyCycle(dc)
                time.sleep(0.1)
                
        # 出布(顯示paper!)，綠燈漸亮到漸暗
        elif ans == '5':
            print('paper!')
            Setup(2, 100)
            # 設定燈泡亮度調節:漸亮漸暗
            for dc in range(0, 101, 5):
                gGPIOnum.ChangeDutyCycle(dc)
                time.sleep(0.1)
            for dc in range(100, -1, -5):
                gGPIOnum.ChangeDutyCycle(dc)
                time.sleep(0.1)

        # 輸入非0/2/5 -> 出拳錯誤，隨機閃爍其中一個燈五次
        else:
            print('Wrong!')
            #隨機閃一燈五次
            rand = random.randint(2, 4)
            Setup(rand, 100)
            for i in range(0, 5):
                TurnOnLED(rand)
                time.sleep(0.3)
                TurnOffLED(rand)
                time.sleep(0.3)
