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

# 變數宣告
distance0 = 0
StopTime1 = 0


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


def get_velocity():
    global StopTime1, distance0, dist_error
    send_trigger_pulse()
    StopTime0 = StopTime1

    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime1 = time.time()

    TimeElapsed = StopTime1 - StartTime
    speed = get_speed()
    distance1 = TimeElapsed * speed * 0.5

    # 界定距離範圍限制
    if distance1 < 2 or distance1 > 400:
        dist_error = True
    else:
        dist_error = False

    # 以兩點距離與耗時，計算速率
    velocity = (distance1 - distance0) / (StopTime1 - StopTime0)
    distance0 = distance1

    return abs(velocity)


if __name__ == '__main__':
    try:
        global dist_error
        dist_error = False
        while True:
            LED.Setup(2, "OUT")
            LED.Setup(3, "OUT")
            LED.Setup(4, "OUT")

            velocity = get_velocity()
            if dist_error:
                print('Range Error: Range 2-400 cm')
            else:
                print('--移動速度 :', str(velocity), 'cm/sec')

            # 設定警示燈號與文字
            # 秒速大於5公分，紅燈閃五次
            if (velocity > 30):
                print('已超速!!!請減速慢行!!')
                Sparkle(4)

            # 秒速20~30公分，黃燈閃五次
            elif (20 <= velocity < 30):
                print('少年郎咖注意欸!')
                Sparkle(3)

            # 秒速10~20公分，綠燈閃五次
            elif (10 <= velocity < 20):
                print('安全駕駛~')
                Sparkle(2)

            # 秒速10公分僅顯示字語
            else:
                print('慢慢來~~')

            time.sleep(1)

    except KeyboardInterrupt:
        print("Measurement stopped by user")
        GPIO.cleanup()

