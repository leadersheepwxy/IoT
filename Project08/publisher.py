import paho.mqtt.client as mqtt
import random
import time
import numpy as np

TopicSeverIP = '192.168.0.202'
TopicServerPort = 1883  # port
TopicName = "Humidity"

mqttc = mqtt.Client('python_pub')
mqttc.connect(TopicSeverIP, TopicServerPort)

sec = 0
hum_list = [0]

while True:
    # 紀錄60秒每秒的隨機生成濕度
    if sec <= 60:
        hum = random.randint(30, 100)
        hum_list.append(hum)
        print(hum_list)
        time.sleep(1)

        # 每60秒計算一次平均濕度並傳給SUB
        if sec == 60:
            H = int(np.mean(hum_list[1:-1]))
            mqttc.publish(TopicName, H)
            sec = 0
            hum_list = [0]
        sec += 1
