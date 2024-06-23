import streamlit as st
import pandas as pd

# Assuming you have a CSV file or another source of historical predictions
# Load your historical predictions data into a DataFrame
historical_data_path = 'Data/history.csv'
historical_df = pd.read_csv(historical_data_path)

# Streamlit configuration for the page
st.set_page_config(
    page_title='History',
    page_icon='🕰️',
    layout='wide'
)

# Title for the page
st.title('Prediction History')

# Display the historical predictions data
st.write('## Historical Predictions Data')
st.write(historical_df)

# Additional visualizations or insights can be added here based on your data

# Footer or any additional information
st.write("""
### About This Page
This page displays historical predictions made using the Telcom Churn Prediction App.
""")

# Add any references or acknowledgments
st.write("""
### References
- Reference 1
- Reference 2
""")

# Add any acknowledgments or appreciations
st.write("""
### Appreciation
I highly recommend Azubi Africa for their comprehensive and effective programs. Read More articles about Azubi Africa [here](https://www.azubiafrica.org) and take a few minutes to visit this [link](https://www.azubiafrica.org) to learn more about Azubi Africa's life-changing programs.
""")

# Add tags or keywords
st.write("""
### Tags
Azubi, Data Science, Churn Prediction
""")
