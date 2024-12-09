# Import libraries
import streamlit as st
import altair as alt
import pandas as pd
import numpy as np
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import pickle 

st.set_page_config(page_title="Price Prediction", 
                   page_icon="🧮",
                   layout="wide")

st.markdown("# 🧮 House Price Prediction")

st.sidebar.header("Model Performance:")

st.write(
    """In this section, we can estimate the property value based on the input values. These inputs include the median house sale comparison, the neighborhood of the property, the number of bedrooms, and the number of bathrooms.

Additionally, you can select which model to use for your prediction from the following options: Linear Regression, Lasso Regression, XGBoost Regressor, Gradient Boosting Regressor, and the tuned version of the XGBoost Regressor. According to our testing, the tuned version of the XGBoost Regressor provides the most accurate property value predictions. However, feel free to use any model you prefer."""
)

st.divider()

st.sidebar.markdown(
"""
### Linear Regression Performance:
- MSE: 14064995476.09
- R-squared: 0.6601

### Lasso Regression Performance:
- MSE: 14064997599.79
- R-squared: 0.6601

### XGBoost Regression Performance:
- MSE: 7620075221.18
- R-squared: 0.8159

### Gradient Boosting Regression Performance:
- MSE: 20519846932.07
- R-squared: 0.5042

### Tunned XGBoost Regression Performance:
- MSE: 7873099317.26
- R-squared: 0.8098
""")

pickle_in = open('StreamlitApp/linear.pkl', 'rb') 
linear = pickle.load(pickle_in) 

pickle_in = open('StreamlitApp/lasso.pkl', 'rb') 
lasso = pickle.load(pickle_in) 

pickle_in = open('StreamlitApp/xgboost.pkl', 'rb') 
xgboost = pickle.load(pickle_in) 

# pickle_in = open('StreamlitApp/gradient.pkl', 'rb') 
# gradient = pickle.load(pickle_in) 

# pickle_in = open('StreamlitApp/tunned_xgboost.pkl', 'rb') 
# tunned_xgboost = pickle.load(pickle_in) 

trulia_df = pd.read_csv('StreamlitApp/final_df.csv')

def prediction(CompareMedianSalePrice, Area, Bath, Bed, ModelChoice):
    if CompareMedianSalePrice[0] == "Yes":
        CompareMedianSalePrice = 1
    elif CompareMedianSalePrice[0] == "No":
        CompareMedianSalePrice = 0 

    if ModelChoice[0] == "Linear Regression":
        prediction = linear.predict([[CompareMedianSalePrice, Area, Bath, Bed]])
    elif ModelChoice[0] == "Lasso Regression":
        prediction = lasso.predict([[CompareMedianSalePrice, Area, Bath, Bed]])
    elif ModelChoice[0] == "XGBoost Regressor":
        prediction = xgboost.predict([[CompareMedianSalePrice, Area, Bath, Bed]])
    # elif ModelChoice[0] == "Gradient Boosting Regressor":
    #     prediction = gradient.predict([[CompareMedianSalePrice, Area, Bath, Bed]])
    # else:
    #     prediction = tunned_xgboost.predict([[CompareMedianSalePrice, Area, Bath, Bed]])
    
    return prediction 

def main(): 
    col1, col2 = st.columns(2)
    with col1:
      Bed = st.slider("Select the number of bedrooms", min_value = 1, max_value = 10, step = 1)
      Area = st.selectbox("In which neighborhood is the property located?", trulia_df['Area'].unique().tolist())
    with col2:
      Bath = st.slider("Select the number of bathrooms", min_value = 0.0, max_value = 5.0, step = 0.5)
      CompareMedianSalePrice = st.radio("Is the house price higher than the median house sale ($665,000)?", ["Yes", "No"])
    ModelChoice = st.pills("Select your preferred predictive model", ["Linear Regression", "Lasso Regression", "XGBoost Regressor", "Gradient Boosting Regressor", "Tunned XGBoost Regressor"])
    result = "" 
    
    if st.button("Predict"): 
        result = prediction(CompareMedianSalePrice, Bath, Bed, Area, ModelChoice) 
        st.success('The predicted sale price is ${}'.format(round(result[0],2))) 
     
if __name__=='__main__': 
    main() 
