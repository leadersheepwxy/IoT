import random
import time
import mysql.connector
from mysql.connector import Error

count=0
t = 25
h = 50
data_list = []

while True:
    #生成隨機溫度(限制與前一次溫度差距正負3度)
    t = random.randint((t-3), (t+3))
#     print('T:', t)

    #生成隨機濕度(限制與前一次濕度差距正負5%)
    h = random.randint((h-5), (h+5))
#     print('H:', h)
    #當前時間
    localtime = time.localtime()
    datetime = time.strftime("%Y-%m-%d %I:%M:%S %p", localtime)
#     print('------------------------------------------------')
#     print('Datetime:', datetime)
    
    data_list.append([str(t), str(h), str(datetime)])
#     print(data_list)
    
    time.sleep(1)
    
    count +=1
    print('count:',count)
    
    if count==60:
        #每六十秒將該分鐘產出之資料存入LOG檔一次
        path = 'data_log.txt'
        f = open(path, 'w')
        f.writelines(str(data_list))
        f.close()
        
        #讀取LOG檔
        f = open(path, 'r')
        data = f.read()[2:-2]
        f.close()
        print('read:', data)
        
        try:
            # 連接 MySQL 資料庫
            connection = mysql.connector.connect(
                host='192.168.0.129',          # 主機名稱
                database='temhum', # 資料庫名稱
                user='pi',        # 帳號
                password='108029041')  # 密碼

            sql = "INSERT INTO th (tem, hum, time) VALUES (%s, %s, %s);"

            #存txt檔案切出每一筆資料的各項數據，並寫入資料庫
            for i in range (0,60):
#                 dataset = data.split("], [")
                print('--------------------------------------------------------')
                print('新增數據第',i+1,'組:')
                t_data = data.split("], [")[i].split(",")[0][1:-1]
                h_data = data.split("], [")[i].split(",")[1][2:-1]
                datetime_data = data.split("], [")[i].split(",")[2][2:-1]
                print('t:',t_data)
                print('h:',h_data)
                print('datetime:',datetime_data)
                
                new_data = (t_data, h_data, datetime_data)
                cursor = connection.cursor()
                cursor.execute(sql, new_data)
                # 確認資料有存入資料庫
                connection.commit()
                print("- 新增資料完成: T={0}, H={1}, TIME={2}".format(t_data, h_data, datetime_data))
        
        except Error as e:
            print("資料庫連接失敗：", e)

        finally:
            if (connection.is_connected()):
                cursor.close()
                connection.close()


        data_list = []
        count = 0
    
    

