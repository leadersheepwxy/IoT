#--coding:utf-8-
import random
import time
import datetime
import mysql.connector
from mysql.connector import Error

import socket
import RPi.GPIO as GPIO




# 樹梅派IP、PORT
bind_ip = '172.20.10.2'  # 用CMD下'ifconfig'查
bind_port = 8888

# socket.AF_INET:於伺服器與伺服器之間進行串接，socket.SOCK_STREAM:使用TCP(資料流)的方式提供可靠、雙向、串流的通信頻道
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((bind_ip, bind_port))

# 伺服器端最多可接受多少socket串接
server.listen(5)
print('Listening in %s:%d' % (bind_ip, bind_port))


roundtime_s=0
roundtime_e=0
roundtime_stop=0

try:
    while True:
        # client存串接對象、addr存連線資訊
        client, addr = server.accept()
        print("Acepted connection from: %s:%d" % (addr[0], addr[1]))
        data = client.recv(1024)  # 接收資料，回傳值為接收到的資料。接收最多字數值1024
#        print(data)
            
        num = str(data).split("'")
#        print(num)
        num_target = int(num[1])
        
        # 開啟
        if data != None:
            print('開啟')
            while True:
                localtime = datetime.datetime.now()
                if roundtime_s == 0:
                    starttime = localtime
                    print("starttime:",starttime)
                roundtime_s += 1

                
                passtime = (localtime - starttime).seconds
                if passtime == num_target:
                    roundtime_e += 1
            #                    print("roundtime_e:",roundtime_e)
                    if roundtime_e == 1:
                        endtime = localtime
                        print("end:",endtime)
                        

                        try:
                            # 連接 MySQL 資料庫
                            connection = mysql.connector.connect(
                                host='172.20.10.13',          # 主機名稱
                                database='rbt', # 資料庫名稱
                                user='pi',        # 帳號
                                password='108029041')  # 密碼
            
                            sql = "INSERT INTO record (s_time, e_time) VALUES (%s, %s);"
                                
                            new_data = (starttime, endtime)
                            cursor = connection.cursor()
                            cursor.execute(sql, new_data)
                            # 確認資料有存入資料庫
                            connection.commit()
                            print("- 新增資料完成: Start_time={0}, End_time={1}".format(starttime, endtime))

                        
                        except Error as e:
                            print("資料庫連接失敗：", e)
            
                        finally:
                            if (connection.is_connected()):
                                cursor.close()
                                connection.close()
                                roundtime_s=0
                                roundtime_e=0
                                break;
                            


except KeyboardInterrupt:
    client_socket.close()
    GPIO.cleaup()
