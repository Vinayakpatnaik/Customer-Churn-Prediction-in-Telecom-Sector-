import numpy as np
import pickle
import pandas as pd
import streamlit as st 

from PIL import Image


pickle_in = open("model.sav","rb")
classifier=pickle.load(pickle_in)

def predict_churn(Gender,SeniorCitizen,MonthlyCharges,TotalCharges,Partner,Dependents,Tenure,
                  PhoneService,MultipleLines,InternetService,OnlineSecurity,OnlineBackup,DeviceProtection,
                  TechSupport,StreamingTV,StreamingMovies,Contract,PaperlessBilling,PaymentMethod):
    
    '''
    Gender
    SeniorCitizen
    MonthlyCharges
    TotalCharges
    Partner
    Dependents
    Tenure
    PhoneService
    MultipleLines
    InternetService
    OnlineSecurity
    OnlineBackup
    DeviceProtection
    TechSupport
    StreamingTV
    StreamingMovies
    Contract
    PaperlessBilling
    PaymentMethod
    '''

    prediction=classifier.predict([[Gender,SeniorCitizen,MonthlyCharges,TotalCharges,Partner,Dependents,Tenure,
                                    PhoneService,MultipleLines,InternetService,OnlineSecurity,OnlineBackup,DeviceProtection,
                                    TechSupport,StreamingTV,StreamingMovies,Contract,PaperlessBilling,PaymentMethod]])
    print(prediction)
    return prediction



def main():
    st.markdown("<h1 style='text-align: center; color: White;'>Web app for Churn Prediction</h1>", unsafe_allow_html=True)

    html_temp = """
    <div style="background-color:grey;padding:10px">
    <h2 style="color:white;text-align:center;">Customer Churn Prediction in Telecom Sector </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)

    Gender = st.text_input("Gender", "Enter Here", help="0 for Female, 1 for Male")
    SeniorCitizen = st.text_input("Senior Citizen", "Enter Here", help="0 for No, 1 for Yes")
    MonthlyCharges = st.text_input("Monthly Charges", "Enter Here", help="Enter the amount charged monthly.")
    TotalCharges = st.text_input("Total Charges", "Enter Here", help="Enter the total amount charged so far.")
    Partner = st.text_input("Partner", "Enter Here", help="Enter 0 for No, 1 for Yes if you have a partner.")
    Dependents = st.text_input("Dependents", "Enter Here", help="Enter 0 for No, 1 for Yes if you have dependents.")
    Tenure = st.text_input("Tenure", "Enter Here", help="Enter the number of months you've been with the service.")
    PhoneService = st.text_input("Phone Service", "Enter Here", help="Enter 0 for No, 1 for Yes if you have a phone service.")
    MultipleLines = st.text_input("Multiple Lines", "Enter Here", help="Enter 0 for No, 1 for No phone service, 2 for Yes.")
    InternetService = st.text_input("Internet Service", "Enter Here", help="Enter 0 for DSL, 1 for Fiber optic, 2 for No.")
    OnlineSecurity = st.text_input("Online Security", "Enter Here", help="Enter 0 for No, 1 for No internet service, 2 for Yes.")
    OnlineBackup = st.text_input("Online Backup", "Enter Here", help="Enter 0 for No, 1 for No internet service, 2 for Yes.")
    DeviceProtection = st.text_input("Device Protection", "Enter Here", help="Enter 0 for No, 1 for No internet service, 2 for Yes.")
    TechSupport = st.text_input("Tech Support", "Enter Here", help="Enter 0 for No, 1 for No internet service, 2 for Yes.")
    StreamingTV = st.text_input("Streaming TV", "Enter Here", help="Enter 0 for No, 1 for No internet service, 2 for Yes.")
    StreamingMovies = st.text_input("Streaming Movies", "Enter Here", help="Enter 0 for No, 1 for No internet service, 2 for Yes.")
    Contract = st.text_input("Contract", "Enter Here", help="Enter 0 for Month-to-month, 1 for One year, 2 for Two year.")
    PaperlessBilling = st.text_input("Paperless Billing", "Enter Here", help="Enter 0 for No, 1 for Yes for paperless billing.")
    PaymentMethod = st.text_input("Payment Method", "Enter Here", help="Enter 0 for Bank transfer, 1 for Credit card, 2 for Electronic check, 3 for Mailed check.")

    # Initialize result variable
    result = None
    
    if st.button("Predict"):
        result = predict_churn(Gender, SeniorCitizen,MonthlyCharges,TotalCharges,Partner,Dependents,Tenure,
                             PhoneService,MultipleLines,InternetService,OnlineSecurity,OnlineBackup,DeviceProtection,
                             TechSupport,StreamingTV,StreamingMovies,Contract,PaperlessBilling,PaymentMethod)
    
    # Display results only if the prediction has been made
    if result is not None:
        churn_status = "not likely to Churn" if result == 0 else "likely to Churn"
        st.success(f'The output is {result} i.e., Customer is {churn_status}')

if __name__=='__main__':
    main()