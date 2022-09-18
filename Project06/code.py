import socket
import RPi.GPIO as GPIO
import LED

LED.Setup(2, 'OUT')
LED.Setup(3, 'OUT')
LED.Setup(4, 'OUT')

# 樹梅派IP、PORT
bind_ip = '192.168.0.202'  # 用CMD下'ifconfig'查
bind_port = 8888

# socket.AF_INET:於伺服器與伺服器之間進行串接，socket.SOCK_STREAM:使用TCP(資料流)的方式提供可靠、雙向、串流的通信頻道
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((bind_ip, bind_port))

# 伺服器端最多可接受多少socket串接
server.listen(5)
print('Listening in %s:%d' % (bind_ip, bind_port))

try:
    # client存串接對象、addr存連線資訊
    client, addr = server.accept()
    print("Acepted connection from: %s:%d" % (addr[0], addr[1]))
    while True:

        data = client.recv(1024)  # 接收資料，回傳值為接收到的資料。接收最多字數值1024
        print(data)
        # 紅燈開
        if data == b'ron':
            LED.TurnOnLED(4)
            print('紅燈開啟')

        # 黃燈開
        elif data == b'yon':
            LED.TurnOnLED(3)
            print('黃燈開啟')

        # 綠燈開
        elif data == b'gon':
            LED.TurnOnLED(2)
            print('綠燈開啟')

        # 燈全開
        elif data == b'allon':
            LED.TurnOnLED(4)
            LED.TurnOnLED(3)
            LED.TurnOnLED(2)
            print('所有燈開啟')

        # 紅燈關
        elif data == b'roff':
            LED.TurnOffLED(4)
            print('紅燈關閉')

        # 黃燈關
        elif data == b'yoff':
            LED.TurnOffLED(3)
            print('黃燈關閉')

        # 綠燈關
        elif data == b'goff':
            LED.TurnOffLED(2)
            print('綠燈關閉')

        # 燈全關
        elif data == b'alloff':
            LED.TurnOffLED(4)
            LED.TurnOffLED(3)
            LED.TurnOffLED(2)
            print('所有燈關閉')

except KeyboardInterrupt:
    client_socket.close()
    GPIO.cleaup()

