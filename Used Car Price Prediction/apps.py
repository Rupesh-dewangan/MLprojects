import streamlit as st
import joblib


st.title('🚗 Car Price Prediction')

st.divider()
st.info('Predicting the price of used car using machine learning model')

import streamlit as st

# Create two columns
st.divider()
col1, col2 = st.columns(2)

fuel_option = ['Petrol', 'Diesal','CNG']
seller_option = ['Individual', 'Dealer']
transmission_option = ['Manual', 'Automatic']


# Add input boxes to the columns

st.divider()
with col1:
    Present_Price = st.number_input("Present_Price",min_value=100000, max_value=1000000,step=1)
    Fuel_Type = st.selectbox("Fuel_Type", fuel_option)
    Transmission = st.selectbox("Transmission",transmission_option)
    Age = st.number_input("Age",min_value=0, max_value=15,step=1)

with col2:
    Kms_Driven = st.number_input("Kms_Driven",min_value=1, max_value=1000000,step=1)
    Seller_Type = st.selectbox("Seller_Type",seller_option)
    Owner = st.number_input("Owner",min_value=0, max_value=10,step=1)

model_input = [[Present_Price/100000, Kms_Driven, fuel_option.index(Fuel_Type), seller_option.index(Seller_Type), transmission_option.index(Transmission), Owner, Age]]
#model_input

if st.button("Predict!"):

    if Present_Price!=0 :
    
        model_load = joblib.load("https://github.com/Rupesh-dewangan/MLprojects/blob/master/Used%20Car%20Price%20Prediction/prediction.joblib")

        #Make Prediction

        prediction = model_load.predict(model_input)
        prediction = f"{float(str(prediction*100000)[1:-1]):.2f}"
        st.write('Expected Price is Rs.' , prediction)
        st.balloons()

    else:
        st.write('Please enter the correct values to predict car price')
