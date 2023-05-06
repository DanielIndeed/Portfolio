#!/usr/bin/env python
# coding: utf-8

# In[28]:


#Reading data

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split 
from sklearn.ensemble import RandomForestClassifier

np.set_printoptions(suppress=True)

train_data = pd.read_csv(r'C:/Users/boscu/AI_models/RF_sound_meter/Dataset/Dataset.csv', delimiter=',') # Read in data

labels = np.array(train_data['Earplugs']) # Labels are the values we want to predict
criteria = np.array(train_data['Criteria'])

train_data = train_data.drop('Earplugs', axis = 1) # Remove the labels from the features and axis 1 refers to the columns
train_data = train_data.drop('Criteria', axis = 1)

train_data_list = list(train_data.columns) # Saving factor names for later use
train_data = np.array(train_data) # Convert to numpy array


# In[29]:


#Training data

# Split the data into training and testing sets
train_train_data, test_train_data, train_labels, test_labels = train_test_split(
    train_data, 
    labels, 
    test_size = 0.25, 
    random_state = 1001,
)

# Instantiate model with 1000 decision trees
rf = RandomForestClassifier(
    n_estimators = 780, 
    random_state = 42,
    max_depth = 13
) 

rf.fit(train_train_data, train_labels) # Train the model on training data


# In[30]:

import joblib

joblib_file = 'C:/Users/boscu/AI_models/RF_sound_meter/Classifier/joblib_rf.pkl'
joblib.dump(rf, joblib_file)

ML_model = joblib.load(joblib_file)

# In[31]:

predictions = ML_model.predict(test_train_data)