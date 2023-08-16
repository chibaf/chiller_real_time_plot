#!/usr/bin/env python3
# -*- coding: utf-8 -*-"
import serial

ser = serial.Serial(
    port='/dev/ttyUSB0',  # ポート名は環境に合わせて変更
    baudrate=9600,
    timeout=1  # タイムアウトの設定
)

# データ送信
request_00M1 = b'\x04\x30\x30\x4D\x31\x05'
ser.write(request_00M1)

# データ受信
line = ser.readline()  
line2 = line.strip().decode("utf-8")
print(line2)
