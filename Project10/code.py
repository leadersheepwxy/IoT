import RPi.GPIO as GPIO
import time

# 設定伺服馬達腳位
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
pwm = GPIO.PWM(17, 50)
pwm.start(0)
GPIO.output(17, True)

# 設定超音波感測器腳位
GPIO_TRIGGER = 7
GPIO_ECHO = 12
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)

# 超音波感測器發射
def send_trigger_pulse():
    GPIO.output(GPIO_TRIGGER, True)
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)


def get_speed():
    speed = 33100 + 26 * 60
    return speed


def distance(speed):
    send_trigger_pulse()

    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()

    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()

    TimeElapsed = StopTime - StartTime
    distance = (TimeElapsed * speed) / 2

    return distance

# 伺服馬達角度
def SetAngle(angle):
    dutyCycle = 1 / 20 * angle + 3
    pwm.ChangeDutyCycle(dutyCycle)


if __name__ == '__main__':
    try:
        while True:
            speed = get_speed()
            dist = distance(speed)
            print("Measured Distance= %.1f cm" % dist)
            # 距離小於5cm，開閘門三秒後，再次關閉
            if dist < 5:
                SetAngle(0)
                time.sleep(3)
                SetAngle(90)
            else:
                SetAngle(90)
            time.sleep(1)

    except KeyboardInterrupt:
        print('Measurement stopped by user')
        GPIO.cleanup()
