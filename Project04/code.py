import RPi.GPIO as GPIO
import Adafruit_DHT
import time
import LED

GPIO.setmode(GPIO.BCM)

# 設定接腳
GPIO_TRIGGER = 7
GPIO_ECHO = 12
GPIO_TEMP = 14

GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)
sensor = Adafruit_DHT.DHT11


# 控制閃燈
def Sparkle(light):
    for i in range(0, 5):
        LED.TurnOnLED(light)
        time.sleep(0.2)
        LED.TurnOffLED(light)
        time.sleep(0.2)


# 觸發超聲波感測器
def send_trigger_pulse():
    GPIO.output(GPIO_TRIGGER, True)
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)


# 用溫濕度計算並返回速度
def get_speed():
    humidity, temperature = Adafruit_DHT.read_retry(sensor, GPIO_TEMP)
    speed = 33100 + temperature * 60
    return speed


# 紀錄開始時間、停止時間算距離
def distance(speed):
    send_trigger_pulse()
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()

    TimeElapsed = StopTime - StartTime
    distance = (TimeElapsed * speed) / 2
    return distance


if __name__ == '__main__':
    try:
        while True:
            LED.Setup(2, "OUT")
            LED.Setup(3, "OUT")
            LED.Setup(4, "OUT")

            # get speed 計算distance並顯示出來
            speed = get_speed()
            dist = distance(speed)
            print("--測距: %.1f cm" % dist)

            # 設定警示燈號與文字
            # 距離小於5公分，紅燈閃五次
            if (dist < 5):
                print('嘿欸!停!!距離少於5公分，注意碰撞!')
                Sparkle(4)

            # 距離5~10公分，黃燈閃五次
            elif (5 <= dist < 10):
                print('距離少於10公分，請注意安全距離!')
                Sparkle(3)

            # 距離10~15公分，綠燈閃五次
            elif (10 <= dist < 15):
                print('OK!距離適當!')
                Sparkle(2)

            # 大於15公分僅顯示警語
            else:
                print('勾來勾來!!')

            time.sleep(1)

    except KeyboardInterrupt:
        print("Measurement stopped by user")
        GPIO.cleanup()
