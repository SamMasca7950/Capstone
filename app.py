import streamlit as st
import pandas as pd
from predict import predict

# Title for your app
st.title('#🍷 Wine Quality Prediction App')

with st.expander("### About this app"):
    st.write('')
    st.markdown(
        '''
        This app utilize a machine learning model to predict wine quality based on physiochemial properties.
        Use the sliders to enter the information before clicking on Predict.
         ''')

st.write('### Enter the information from your wine.' )


input_features = {
    'fixed acidity': st.slider('Fixed Acidity', min_value=3.8, max_value=15.9, value=7.0, step=0.1, format="%.2f"),
    'volatile acidity': st.slider('Volatile Acidity', min_value=0.08, max_value=2.0, value=0.5, step=0.01, format="%.2f"),
    'citric acid': st.slider('Citric Acid', min_value=0.0, max_value=1.7, value=0.5, step=0.01, format="%.2f"),
    'residual sugar': st.slider('Residual Sugar', min_value=0.6, max_value=30.0, value=2.0, step=0.1, format="%.2f"),
    'chlorides': st.slider('Chlorides', min_value=0.0, max_value=0.7, value=0.05, step=0.001, format="%.2f"),
    'free sulfur dioxide': st.slider('Free Sulfur Dioxide', min_value=1, max_value=70, value=35, step=1, format="%.2f"),
    'total sulfur dioxide': st.slider('Total Sulfur Dioxide', min_value=5, max_value=200, value=100, step=1, format="%.2f"),
    'density': st.slider('Density', min_value=0.9900, max_value=1.040, value=0.9960, step=0.0001, format="%.4f"),
    'pH': st.slider('pH', min_value=2.5, max_value=4.0, value=3.25, step=0.01, format="%.2f"),
    'sulphates': st.slider('Sulphates', min_value=0.0, max_value=2.0, value=0.5, step=0.01, format="%.2f"),
    'alcohol': st.slider('Alcohol', min_value=8.0, max_value=15.0, value=10.5, step=0.1, format="%.2f")
    
}


if st.button('Predict'):
    input_df = pd.DataFrame([input_features])

 
    prediction = predict(input_df)  

    st.write(f'Prediction: {prediction}')
