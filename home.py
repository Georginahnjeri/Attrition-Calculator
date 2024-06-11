import streamlit as st

# Streamlit app
st.title('Customer Churn Predictor')

# Introduction for the homepage
st.write("""
## Welcome to the Customer Churn Predictor

Every company aims to increase its profit or revenue margin, and customer retention is one key area where industry players focus their resources. In today's world of machine learning, most companies build classification models to perform churn analysis on their customers.

**Classification** in machine learning and statistics is a supervised learning approach where the computer program learns from the data given to it and makes new observations or classifications. The main goal is to identify which class/category the new data will fall into.

For example, we can classify a bank transaction into Fraud or Non-Fraud categories or an email into Spam or Non-Spam.

This app helps you predict whether a customer is likely to churn (leave) or not based on various input features. Use the **Predict** page to enter customer data and see the prediction. You can also view the history of all predictions made using this app on the **History** page.
""")

# Navigation sidebar
pages = st.sidebar.selectbox("Choose a page", ["🔮 Predict", "🕝 History" , "📒 Data" , "🏠 Home" , "📈 Dashboard" ])