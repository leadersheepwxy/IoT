import Adafruit_DHT
import time
import LED  # 放之前的檔名
import random

# 燈光亮一下
def Bright(light):
    LED.TurnOnLED(light)
    time.sleep(1)
    LED.TurnOffLED(light)
    time.sleep(1)

# 燈光快速閃爍
def Sparkle(light):
    LED.TurnOnLED(light)
    time.sleep(0.2)
    LED.TurnOffLED(light)
    time.sleep(0.2)
    LED.TurnOnLED(light)
    time.sleep(0.2)
    LED.TurnOffLED(light)
    time.sleep(0.2)


sensor = Adafruit_DHT.DHT11
GPIO = 14  # 溫濕度感測器 14腳位

while True:
    LED.Setup(2, "OUT")
    LED.Setup(3, "OUT")
    LED.Setup(4, "OUT")

    # 抓取當前時間
    currentTime = time.strftime("%H:%M:%S")
    # 記錄溫溼度感測器所量測之數值
    humidity, temperature = Adafruit_DHT.read_retry(sensor, GPIO)

    if humidity is not None and temperature is not None:
        print("=======================================")

        # 印出當前時間的溫溼度
        print(currentTime, '-> Temp={0}*C, Humidity={1}%'.format(temperature, humidity))

        # 判別當前溫溼度符合中暑條件
        if ((temperature > 38 and humidity > 30) or (temperature > 31 and humidity > 80)):
            Sparkle(4)
            print("中暑警報!")

        # 判別當前溫溼度符合預防中暑條件
        elif temperature > 34:
            Sparkle(3)
            print("請注意!預防中暑!")

        # 不符合中暑及預警條件
        else:
            Sparkle(2)
            print("目前沒有中暑危險!")

            # 產生隨機數以觸發警示條件
            print("產生隨機數......")
            while True:
                randTEMP = random.randint(25, 50)
                randHUM = random.randint(0, 100)
                print('隨機Temp={0}*C , 隨機Humidity={1}%'.format(randTEMP, randHUM))

                # 若隨機數符合"中暑"條件，則發出警示並跳出迴圈
                if ((randTEMP > 38 and randHUM > 30) or (randTEMP > 31 and randHUM > 80)):
                    Bright(4)
                    print("中暑警報!")
                    break
                # 若隨機數符合"預防中暑"條件，則發出警示並跳出迴圈
                elif randTEMP > 34:
                    Bright(3)
                    print("請注意!預防中暑!")
                    break
                # 若隨機數無法觸發預警則亮綠燈，並再次生成隨機數，直到觸發條件為止。
                else:
                    Bright(2)
                    print("目前沒有中暑危險!")
                    print("再次生成隨機數......")

    else:
        print('Failed to get reading. Try again!')

    time.sleep(5)
