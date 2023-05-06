#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import serial
import time
ser = serial.Serial(port = "COM8", baudrate = 9600 , bytesize = 8 )
file2 = open(r"C:\Users\boscu\e_nnovate\Data\Arduino stop.txt",'r+')
f = open(r"C:\Users\boscu\e_nnovate\Data\Arduino text.txt",'a')
word1="recommended"
word2="required"
content=file2.read()
try:
    while 1:
        ok1=0
        ok2=0
        if word1 in content:
            file2.truncate(0)
            file2.close()
            ok1 = 1
        elif word2 in content:
            file2.truncate(0)
            file2.close()
            ok2 = 1
        else:
            f.write(ser.readline().decode("utf-8"))
            ser.flushInput()
            ser.flushOutput()
            f.close()
            f = open(r"C:\Users\boscu\e_nnovate\Data\Arduino text.txt",'a')
        file2 = open(r"C:\Users\boscu\e_nnovate\Data\Arduino stop.txt",'r+')
        content=file2.read()
        if ok1==1:
            time.sleep(7200)
        elif ok2==1:
            time.sleep(3600)
except KeyboardInterrupt:
    print("done")


# In[ ]:




