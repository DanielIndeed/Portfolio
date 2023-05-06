#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np

from Model_trainer import ML_model

print("Enter your age: ")
val_age = int(input())

Arduino = pd.read_csv(r"C:/Users/boscu/AI_models/RF_sound_meter/Dummy Data/Noise values.txt", names=['Db'])

avg_val_Db = Arduino['Db'].mean()

k = (Arduino.count(numeric_only=True))

if avg_val_Db >= 80:
	absolute_timer_alg=np.double(k*0.1)
else:
	absolute_timer_alg=0
if absolute_timer_alg > 60:
	absolute_timer_alg=0
absolute_timer_alg=np.double(absolute_timer_alg)

input_data = {
    'Age': [val_age],
    'Noise level': [avg_val_Db],
    'Time exposure': [absolute_timer_alg]
}

input_data = pd.DataFrame(input_data)

input_data = np.array(input_data)

predictions = ML_model.predict(input_data)

print(input_data)
print(predictions)

# In[ ]:


from plyer import notification 
from PIL import Image
import serial

file2 = open(r"C:/Users/boscu/e_nnovate/Data/Arduino stop.txt",'r+')
file_rec = open(r"C:/Users/boscu/e_nnovate/Data/Arduino text.txt",'r+')
file_req = open(r"C:/Users/boscu/e_nnovate/Data/Arduino text.txt",'r+')

if predictions == 'Recommended':
    notification.notify(
        title = "Earplugs are required",
        message = "If not available, withdrawal from the environment is also an option.",
        app_icon = r"C:/Users/boscu/e_nnovate/Images/1.ico",
        timeout = 20
    )
    im1 = Image.open(r"C:/Users/boscu/e_nnovate/Images/1.png")
    im1.show()
    file_rec.truncate(0)
    file2.write("recommended")
if predictions == 'Required':
    notification.notify(
        title = "Earplugs are required",
        message = "If not available, withdrawal from the environment is also an option.",
        app_icon = r"C:/Users/boscu/e_nnovate/Images/2.ico",
        timeout = 20
    )
    im2 = Image.open(r"C:/Users/boscu/e_nnovate/Images/2.png")
    im2.show()
    file_req.truncate(0)
    file2.write("required")

