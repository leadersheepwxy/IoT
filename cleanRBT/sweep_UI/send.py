import socket
import RPi.GPIO as GPIO


# 樹梅派IP、PORT
bind_ip = '172.20.10.13'  # 用CMD下'ifconfig'查
bind_port = 8888

# socket.AF_INET:於伺服器與伺服器之間進行串接，socket.SOCK_STREAM:使用TCP(資料流)的方式提供可靠、雙向、串流的通信頻道
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((bind_ip, bind_port))

# 伺服器端最多可接受多少socket串接
server.listen(5)
print('Listening in %s:%d' % (bind_ip, bind_port))

try:
    while True:
        # client存串接對象、addr存連線資訊
        client, addr = server.accept()
        print("Acepted connection from: %s:%d" % (addr[0], addr[1]))
        data = client.recv(1024)  # 接收資料，回傳值為接收到的資料。接收最多字數值1024
        print(data)
        # 紅燈開
        if data == b'on':
            #LED.TurnOnLED(4)
            print('開啟')


        # 燈全關
        elif data == b'off':
            #LED.TurnOnLED(4)
            print('關閉')

except KeyboardInterrupt:
    client_socket.close()
    GPIO.cleaup()

