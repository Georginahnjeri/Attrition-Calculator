import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go

# Load your dataset
data_path = 'Data/Churn_Train_Data.csv'
data = pd.read_csv(data_path)

st.set_page_config(
    page_title='Dashboard',
    page_icon='',
    layout='wide'
)

def dashboard_page():
    st.title("Dashboard")

    # Check if data and selections are available from session state
    if "selected_cat_cols" not in st.session_state or "selected_num_cols" not in st.session_state:
        st.error("Please select categorical and numerical columns on the Data Page first!")
        return

    selected_cat_cols = st.session_state.get("selected_cat_cols")
    selected_num_cols = st.session_state.get("selected_num_cols")

    # Sidebar for additional information
    st.sidebar.title('Additional Information')

    # EDA Section
    st.header("Exploratory Data Analysis (EDA)")
    st.write("Performing EDA on the dataset.")

    # Stats about the dataset
    st.header("Dataset Statistics")

    if 'Churn' in data.columns:
        st.subheader("Churn Rate")
        churn_rate = data['Churn'].value_counts(normalize=True)['Yes']
        st.write(f"Churn Rate: {churn_rate:.2%}")
    else:
        st.warning("Churn column not found in the dataset.")

    if 'MonthlyCharges' in data.columns:
        st.subheader("Average Monthly Charges")
        average_monthly_charges = data['MonthlyCharges'].mean()
        st.write(f"Average Monthly Charges: ${average_monthly_charges:.2f}")
    else:
        st.warning("MonthlyCharges column not found in the dataset.")

    st.subheader("Data Size")
    st.write(f"Number of Rows: {data.shape[0]}")
    st.write(f"Number of Columns: {data.shape[1]}")

    # Authentication Section (placeholder)
    st.header("Authentication")
    st.write("Authentication information and controls go here.")

    # Use st.container to structure the dashboard
    dashboard_container = st.container()

    # Categorical Columns Analysis
    with dashboard_container:
        st.write("Categorical Columns Analysis:")
        # Add a dropdown to choose chart type (optional)
        chart_type = st.selectbox("Select Chart Type", ["Bar Chart", "Pie Chart"])

        for col in selected_cat_cols:
            if col in data.columns:
                if chart_type == "Bar Chart":
                    # Create a bar chart with different colors for each bar
                    color_sequence = ["#0000FF", "#007FFF", "#00BFFF", "#1E90FF", "#4169E1", "#6495ED"]
                    colors = color_sequence[:len(data[col].value_counts())]
                    fig = go.Figure(data=[go.Bar(x=data[col].value_counts().index, y=data[col].value_counts(), marker_color=colors)])
                    st.plotly_chart(fig)
                elif chart_type == "Pie Chart":
                    # Create a pie chart
                    labels = data[col].value_counts().index
                    values = data[col].value_counts().values
                    fig = go.Figure(data=[go.Pie(labels=labels, values=values)])
                    st.plotly_chart(fig)
            else:
                st.warning(f"Column '{col}' not found in the dataset.")

    # Numerical Columns Analysis
    with dashboard_container:
        st.write("Numerical Columns Analysis:")
        # Add options to customize histogram parameters (optional)
        num_bins = st.slider("Number of Bins", 5, 20, 10)

        for col in selected_num_cols:
            if col in data.columns:
                # Create a histogram with different colors for each bar
                color_sequence = ["#0000FF", "#007FFF", "#00BFFF", "#1E90FF", "#4169E1", "#6495ED"]
                # Normalize the data for color assignment
                normalized_data = (data[col] - data[col].min()) / (data[col].max() - data[col].min())
                color_indices = np.round(normalized_data * (len(color_sequence) - 1)).astype(int)
                colors = [color_sequence[i] for i in color_indices]
                fig = go.Figure(data=[go.Histogram(x=data[col], nbinsx=num_bins, marker_color=colors)])
                st.plotly_chart(fig)
            else:
                st.warning(f"Column '{col}' not found in the dataset.")

if __name__ == "__main__":
    dashboard_page()


