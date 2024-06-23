# Predicting Customer Churn- Churn Calculator
In today's competitive market, customer retention is crucial for businesses, especially in industries like telecommunications where service providers strive to maintain a loyal customer base. Predicting customer churn, or the likelihood of customers leaving a service, is a significant area of interest. To address this challenge, we developed an interactive dashboard using Streamlit, a powerful tool for building data-driven web applications in Python.

## Project Overview
The goal of our project was to create an interactive dashboard that allows users to explore and analyze customer data, predict churn using machine learning models, and gain insights through visualizations and statistics. The dashboard is designed to be intuitive, enabling users to interact with data columns, select analysis types, and visualize trends dynamically.

### Key Features:
Data Exploration: Explore categorical and numerical features of customer data.
Machine Learning Prediction: Predict customer churn using pre-trained models.
Visualizations: Generate interactive charts (bar charts, pie charts, histograms) to visualize data distributions and trends.
Dataset Statistics: Display summary statistics such as attrition rates and average monthly income.
Authentication: Placeholder for adding authentication controls.

#### Tools Used
Streamlit
Streamlit is a Python library that simplifies the creation of web applications for data science and machine learning projects. It allows developers to build interactive dashboards with minimal code, integrating data visualizations seamlessly.

Plotly
Plotly is utilized within Streamlit to create interactive plots such as bar charts, pie charts, and histograms. These visualizations enhance user interaction and facilitate deeper insights into the dataset.

Pandas and NumPy
Pandas and NumPy are fundamental libraries for data manipulation and analysis in Python. They were used extensively for data loading, preprocessing, and statistical computations within the dashboard.

#### Implementation Details
Data Preprocessing
The project began with loading and preprocessing the dataset (Churn_Train_Data.csv). Numerical features such as tenure, monthly charges, and total charges were standardized using StandardScaler, while categorical features were encoded using an encoder trained on the dataset.

Machine Learning Model
A logistic regression model was trained to predict customer churn based on selected features. The model was serialized using joblib and integrated into the Streamlit dashboard for real-time predictions.

Dashboard Sections
1. Exploratory Data Analysis (EDA)
The dashboard provides insights into the dataset through exploratory data analysis. It calculates and displays statistics such as attrition rates, average monthly income, and dataset size. Users can interactively explore categorical and numerical distributions.

2. Predictive Analytics
Users can input customer information through interactive form fields. The dashboard preprocesses this input, feeds it into the trained machine learning model, and predicts the likelihood of churn along with the probability percentage.

3. Visualization
Visualizations are a key feature of the dashboard. Users can choose between different chart types (bar charts, pie charts) and customize parameters (e.g., number of bins for histograms) to visualize patterns and correlations within the data.

4. Authentication
Although currently a placeholder, the dashboard includes a section for authentication controls. This feature can be further developed to secure access and manage user permissions as required.

#### Usage and Future Enhancements
Usage
To use the dashboard, simply run the Python script. Navigate through the sections to explore data insights, predict churn probabilities, and visualize trends interactively. Adjust parameters and selections to gain deeper understanding and actionable insights.

Future Enhancements
Model Improvement: Experiment with different machine learning algorithms or ensemble methods to improve prediction accuracy.
Real-time Data Integration: Connect the dashboard to live data sources for dynamic updates and real-time predictions.
Enhanced User Interface: Improve aesthetics and usability with additional widgets, tooltips, and interactive elements.
Deployment: Deploy the dashboard to a cloud platform for broader accessibility and scalability.
Conclusion
In conclusion, our project demonstrates the power of Streamlit in creating interactive data-driven applications for predictive analytics. By leveraging machine learning models and visualizations, businesses can proactively manage customer churn and optimize retention strategies. The dashboard not only provides valuable insights but also enhances decision-making capabilities through intuitive exploration of telecom customer data.

For developers and data scientists, Streamlit offers a robust framework to showcase analytical capabilities effectively. With its ease of use and flexibility, Streamlit empowers teams to build and deploy sophisticated web applications for diverse use cases in industries ranging from telecommunications to finance and beyond.

This article encapsulates the essence of our project, emphasizing the importance of predictive analytics in customer churn management within the telecommunications sector. It aligns with the guidelines provided and highlights the technical implementation, features, and potential for future enhancements.
Author - Georginah Njeri 