import RPi.GPIO as GPIO
import time

#設定腳位(輸入輸出)
def Setup(GPIOnum, OUT_IN):
    GPIO.setmode(GPIO.BCM)
    if OUT_IN == "OUT":
        GPIO.setup(GPIOnum, GPIO.OUT)
    else:
        GPIO.setup(GPIOnum, GPIO.IN)

#開燈
def TurnOnLED(GPIOnum):
    GPIO.output(GPIOnum, True)

#關燈
def TurnOffLED(GPIOnum):
    GPIO.output(GPIOnum, False)

if __name__ == "__main__":
    try:
        Setup(2, "OUT")
        Setup(3, "OUT")
        Setup(4, "OUT")
        while True:
            # 紅燈亮2秒，顯示'紅燈停'字樣
            print('Red for STOP!')
            TurnOnLED(4)
            time.sleep(2)
            TurnOffLED(4)

            # 黃燈閃5次0.2秒，顯示'叮叮叮'字樣
            for i in range(0, 5):
                print('Ding~')
                TurnOnLED(3)
                time.sleep(0.2)
                TurnOffLED(3)
                time.sleep(0.2)

            # 綠燈亮1秒，顯示'綠燈行'字樣
            print('Green for GO!')
            TurnOnLED(2)
            time.sleep(1)
            TurnOffLED(2)
            

    except KeyboardInterrupt:
        GPIO.cleanup()
