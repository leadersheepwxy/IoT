import paho.mqtt.client as mqtt
import LED
import time

LED.Setup(27, "OUT")
LED.Setup(17, "OUT")
LED.Setup(18, "OUT")

# 與A區農場連線
def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe("Temperature")

# A區農場回傳之數據判斷，平均溫度>=35，則亮紅燈一次
def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload))
    if msg.payload >= b'35':
        LED.TurnOnLED(17)
        time.sleep(1)
        LED.TurnOffLED(17)

# 與B區農場連線
def on_connect2(client, userdata, flags, rc):
    print("Connected with result code  " + str(rc))
    client.subscribe("Humidity")

# B區農場回傳之數據判斷，平均濕度<=50，則亮黃燈一次    
def on_message2(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload))
    if msg.payload <= b'50':
        LED.TurnOnLED(18)
        time.sleep(1)
        LED.TurnOffLED(18)

client = mqtt.Client()
client2 = mqtt.Client()

client.connect("192.168.0.207", 1883, 60)  # A區農場Publisher1的IP、port
client2.connect("192.168.0.202", 1883, 60)  # B區農場Publisher2的IP、port

client.on_connect = on_connect
client.on_message = on_message

client2.on_connect = on_connect2
client2.on_message = on_message2

# 因多台client，需以此代替client.loop_forever()
client.loop_start()
client2.loop_start()
time.sleep(20)
client.loop_stop()
client2.loop_stop()
