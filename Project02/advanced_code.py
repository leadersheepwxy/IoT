import RPi.GPIO as GPIO
import time
import sys
import random

global gGPIOnum

# 設定腳位輸出頻率
def Setup(GPIOnum, frequency):
    global gGPIOnum
    GPIO.setmode(GPIO.BCM)
    gGPIOnum = GPIOnum
    GPIO.setup(gGPIOnum, GPIO.OUT)
    gGPIOnum = GPIO.PWM(gGPIOnum, frequency)
    gGPIOnum.start(0)

# 開燈
def TurnOnLED(GPIOnum):
    GPIO.output(GPIOnum, True)

# 關燈
def TurnOffLED(GPIOnum):
    GPIO.output(GPIOnum, False)

# 設定燈號PWM
def LedPWM(GPIOnum):
    Setup(GPIOnum, 100)
    for dc in range(0, 101, 5):
        gGPIOnum.ChangeDutyCycle(dc)  # 變更PWM的週期，每
        time.sleep(0.1)
    for dc in range(100, -1, -5):
        gGPIOnum.ChangeDutyCycle(dc)
        time.sleep(0.1)


if __name__ == "__main__":
    # 字典將數字出拳可顯示在螢幕為拳種
    dic = {'0': 'Stone', '2': 'Scissors', '5': 'Paper'}
    while True:
        # 玩家出拳
        ans = input('Paper~Scissors~Stone~：')
        # 電腦隨機出拳，並顯示出甚麼拳

        if ans == '0' or ans == '2' or ans == '5':
            computer = random.choice(['0', '2', '5'])
            print('computer throws ', dic[computer])
            # 玩家出石頭
            if ans == '0':
                # 電腦出剪刀 -> 顯示獲勝，並漸亮漸暗綠燈兩次
                if (computer == '2'):
                    print('you WIN!!!')
                    LedPWM(2)
                    LedPWM(2)
                # 電腦出布 -> 顯示敗北，並漸亮漸暗紅燈兩次
                elif (computer == '5'):
                    print('you LOSE...')
                    LedPWM(4)
                    LedPWM(4)
                # 電腦出石頭 -> 顯示平手，並漸亮漸暗黃燈兩次
                else:
                    print('TIE!')
                    LedPWM(3)
                    LedPWM(3)

            # 玩家出剪刀
            elif ans == '2':
                # 電腦出布 -> 顯示獲勝，並漸亮漸暗綠燈兩次
                if (computer == '5'):
                    print('you WIN!!!')
                    LedPWM(2)
                    LedPWM(2)
                # 電腦出石頭 -> 顯示敗北，並漸亮漸暗紅燈兩次
                elif (computer == '0'):
                    print('you LOSE...')
                    LedPWM(4)
                    LedPWM(4)
                # 電腦出剪刀 -> 顯示平手，並漸亮漸暗黃燈兩次
                else:
                    print('TIE!')
                    LedPWM(3)
                    LedPWM(3)

            # 玩家出布
            elif ans == '5':
                # 電腦出石頭 -> 顯示獲勝，並漸亮漸暗綠燈兩次
                if (computer == '0'):
                    print('you WIN!!!')
                    LedPWM(2)
                    LedPWM(2)
                # 電腦出剪刀 -> 顯示敗北，並漸亮漸暗紅燈兩次
                elif (computer == '2'):
                    print('you LOSE...')
                    LedPWM(4)
                    LedPWM(4)
                # 電腦出布 -> 顯示平手，並漸亮漸暗黃燈兩次
                else:
                    print('TIE!')
                    LedPWM(3)
                    LedPWM(3)
        # 輸入非0/2/5 -> 顯示出拳錯誤，並隨機閃爍某一燈五次
        else:
            print('Wrong!')
            rand = random.randint(2, 4)
            Setup(rand, 100)
            for i in range(0, 5):
                TurnOnLED(rand)
                time.sleep(0.3)
                TurnOffLED(rand)
                time.sleep(0.3)
