# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 13:44:41 2025

@author: USER
"""

import numpy as np
import pickle

#loading the saved model
loaded_model = pickle.load(open('C:/Users/USER/OneDrive/Desktop/jupyter/trained_model2.sav', 'rb'))

#predictive system
input_data= (0,1,0,1,1,3000,0.0,66.0,360.0,1.0, 2)

#converting input data to numpy array because processing is easier than list
input_data_as_numpy_array= np.array(input_data)
#reshape the array
input_data_reshaped= np.array(input_data).reshape(1, -1)

prediction= loaded_model.predict(input_data_reshaped)
print(prediction)
if prediction [0] == 0:
    print("Not eligible for a loan" )
else: 
    print(" eligible for a loan")

print("Prediction result:", prediction)