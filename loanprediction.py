# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 13:59:27 2025

@author: USER
"""

import numpy as np
import pickle
import streamlit as st

#loading the saved model
loaded_model = pickle.load(open(r'C:\Users\USER\OneDrive\Desktop\jupyter\trained_model2.sav', 'rb'))

#create a function for prediction
def loan_prediction(input_data):
    
    
    #converting input data to numpy array because processing is easier than list
    input_data_as_numpy_array= np.array(input_data, dtype=float)
    #reshape the array
    input_data_reshaped= input_data_as_numpy_array.reshape(1, -1)
    
    prediction= loaded_model.predict(input_data_reshaped)
    #print(prediction)
    # Return the result
    if prediction[0] == 0:
        return "Not eligible for a loan"
    else:
        return "Eligible for a loan"
def main():
    st.title("Loan eligibility web App")
    #getting the input data from the user				
    Gender = st.text_input("Gender, (0 for Male, 1 for Female):")
    Married= st.text_input("Marital status, (0 for No, 1 for Yes):")
    Dependents= st.text_input("Number of dependents, (e.g., 0, 1, 2, 3)")
    Education= st.text_input("graduate or non graduate, (0 for Non-Graduate, 1 for Graduate):")
    Self_Employed=st.text_input("self employment status, (0 for No, 1 for Yes):")
    ApplicantIncome= st.text_input("applicants income:")
    CoapplicantIncome= st.text_input("Co_applicans income :")
    LoanAmount =st.text_input("Loan Amount:")
    Loan_Amount_Term =st.text_input("Loan Amount Term:")
    Credit_History = st.text_input("credit history:")
    Property_Area= st.text_input("Area of property, (0 for Rural, 1 for Semi-Urban, 2 for Urban):")
    
    #code for prediction
    predict = ''
    #creating a pattern for prediction
    if st.button("Check eligibility"):
        try:
            input_values = [
                float(Gender), float(Married), float(Dependents), 
                float(Education), float(Self_Employed), float(ApplicantIncome), 
                float(CoapplicantIncome), float(LoanAmount), 
                float(Loan_Amount_Term), float(Credit_History), float(Property_Area)
            ]
            predict = loan_prediction(input_values)
        except ValueError:
            predict = "Please enter valid numeric inputs for all fields."
    
            #predict = loan_prediction([Gender, Married, Dependents, Education, Self_Employed, ApplicantIncome, CoapplicantIncome,LoanAmount, Loan_Amount_Term, Credit_History, Property_Area])
    
    st.success(predict)
    
if __name__ == '__main__':
    main()