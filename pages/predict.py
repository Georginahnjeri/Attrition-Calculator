import streamlit as st
import joblib
import pandas as pd
import datetime
import os
from sklearn.preprocessing import StandardScaler

# Load your CSV data into a DataFrame
data_path = 'Data/Churn_Train_Data.csv'
df = pd.read_csv(data_path)

# Create an instance of StandardScaler
scaler = StandardScaler()

# Fit scaler on numerical columns of your dataset
numeric_cols = ['tenure', 'MonthlyCharges', 'TotalCharges']
scaler.fit(df[numeric_cols])

# Function to preprocess input data
def preprocess_input(data, encoder, scaler):
    # Add Tenure_group based on the tenure
    data['Tenure_group'] = pd.cut(data['tenure'],
                                  bins=[0, 12, 24, 48, 60, 72],
                                  labels=['0-12', '12-24', '24-48', '48-60', '60-72'],
                                  right=False)
    
    # Encode categorical columns
    categorical_cols = data.select_dtypes(include=['object', 'category']).columns
    data[categorical_cols] = encoder.transform(data[categorical_cols])
    
    # Normalize the numeric columns using the fitted scaler
    data[numeric_cols] = scaler.transform(data[numeric_cols])
    
    # Drop Tenure_group to avoid issues during prediction
    data = data.drop(columns=['Tenure_group'])
    
    return data

# Function to load machine learning pipeline
def load_pipeline(model_path):
    pipeline = joblib.load(model_path)
    return pipeline

# Streamlit configuration
st.set_page_config(
    page_title='Predict Page',
    page_icon='🔮',
    layout='wide'
)

st.title('Telcom Churn Prediction 🔮')

# Function to display input form
def display_form():
    # Load encoder and model pipeline
    encoder = joblib.load("./Models/encoder.joblib")
    model_path = "./Models/Logistic_regression_pipeline.joblib"  # Update with your model path
    pipeline = load_pipeline(model_path)
    
    with st.form('input-feature'):
        col1, col2, col3 = st.columns(3)

        with col1:
            st.write('### Personal Information')
            st.selectbox('Gender', options=['Male', 'Female'], key='gender')
            st.number_input('Senior Citizen', min_value=0, max_value=1, key='SeniorCitizen')
            st.selectbox('Partner', options=[0, 1], key='Partner')
            st.selectbox('Dependents', options=[0, 1], key='Dependents')
            st.number_input('Tenure', min_value=0, key='tenure')
            st.selectbox('Phone Service', options=[0, 1], key='PhoneService')
            st.selectbox('Multiple Lines', options=['No', 'Yes'], key='MultipleLines')

        with col2:
            st.write('### Work Information')
            st.selectbox('Internet Service', options=['DSL', 'Fiber optic', 'No'], key='InternetService')
            st.selectbox('Online Security', options=['No', 'Yes', 'No internet service'], key='OnlineSecurity')
            st.selectbox('Online Backup', options=['No', 'Yes', 'No internet service'], key='OnlineBackup')
            st.selectbox('Device Protection', options=['No', 'Yes', 'No internet service'], key='DeviceProtection')
            st.selectbox('Tech Support', options=['No', 'Yes', 'No internet service'], key='TechSupport')
            st.selectbox('Streaming TV', options=['No', 'Yes', 'No internet service'], key='StreamingTV')

        with col3:
            st.write('### Contract Information')
            st.selectbox('Streaming Movies', options=['No', 'Yes', 'No internet service'], key='StreamingMovies')
            st.selectbox('Contract', options=['Month-to-month', 'One year', 'Two year'], key='Contract')
            st.selectbox('Paperless Billing', options=[0, 1], key='PaperlessBilling')
            st.selectbox('Payment Method', options=['Electronic check', 'Mailed check', 'Bank transfer (automatic)', 'Credit card (automatic)'], key='PaymentMethod')
            st.number_input('Monthly Charges ($)', min_value=0.0, max_value=200.0, value=0.0, key='MonthlyCharges')
            st.number_input('Total Charges ($)', min_value=0.0, value=0.0, key='TotalCharges')

        submit_button = st.form_submit_button("Submit")

        if submit_button:
            gender = st.session_state['gender']
            senior_citizen = st.session_state['SeniorCitizen']
            partner = st.session_state['Partner']
            dependents = st.session_state['Dependents']
            tenure = st.session_state['tenure']
            phone_service = st.session_state['PhoneService']
            multiple_lines = st.session_state['MultipleLines']
            internet_service = st.session_state['InternetService']
            online_security = st.session_state['OnlineSecurity']
            online_backup = st.session_state['OnlineBackup']
            device_protection = st.session_state['DeviceProtection']
            tech_support = st.session_state['TechSupport']
            streaming_tv = st.session_state['StreamingTV']
            streaming_movies = st.session_state['StreamingMovies']
            contract = st.session_state['Contract']
            paperless_billing = st.session_state['PaperlessBilling']
            payment_method = st.session_state['PaymentMethod']
            monthly_charges = st.session_state['MonthlyCharges']
            total_charges = st.session_state['TotalCharges']

            # Prepare input data
            input_data = pd.DataFrame({
                'gender': [gender],
                'SeniorCitizen': [senior_citizen],
                'Partner': [partner],
                'Dependents': [dependents],
                'tenure': [tenure],
                'PhoneService': [phone_service],
                'MultipleLines': [multiple_lines],
                'InternetService': [internet_service],
                'OnlineSecurity': [online_security],
                'OnlineBackup': [online_backup],
                'DeviceProtection': [device_protection],
                'TechSupport': [tech_support],
                'StreamingTV': [streaming_tv],
                'StreamingMovies': [streaming_movies],
                'Contract': [contract],
                'PaperlessBilling': [paperless_billing],
                'PaymentMethod': [payment_method],
                'MonthlyCharges': [monthly_charges],
                'TotalCharges': [total_charges]
            })

            # Preprocess input data
            input_data = preprocess_input(input_data, encoder, scaler)

            # Make prediction
            prediction = pipeline.predict(input_data)
            probability = pipeline.predict_proba(input_data)

            # Display prediction result
            st.markdown(f"### Churn Prediction: {prediction[0]}")
            st.markdown(f"#### Probability of Churn: {probability[0][1]*100:.2f}%")

# Main section
if __name__ == "__main__":
    st.title("Churn Prediction App")
    display_form()
