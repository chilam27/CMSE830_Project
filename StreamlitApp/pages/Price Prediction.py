# Import libraries
import streamlit as st
import altair as alt
import pandas as pd
import numpy as np
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression, Lasso

import pickle 

st.set_page_config(page_title="Price Prediction", 
                   page_icon="🧮",
                   layout="wide")

st.markdown("# House Price Prediction")

st.sidebar.header("Model Performance")

st.write(
    """Determine which model (Linear, Lasso, XGBoost) work best (that return the smallest error)."""
)

st.sidebar.markdown(
"""
### Linear Regression Performance:
- MSE: 14064995476.091335
- R-squared: 0.6601388179154841

### Lasso Regression Performance:
- MSE: 14064997599.792627
- R-squared: 0.6601387665991767

### XGBoost Regression Performance:
- MSE: 7620075221.183669
- R-squared: 0.815871410933144
""")

###
# loading in the model to predict on the data 
pickle_in = open('StreamlitApp/linear.pkl', 'rb') 
linear = pickle.load(pickle_in) 

pickle_in = open('StreamlitApp/lasso.pkl', 'rb') 
lasso = pickle.load(pickle_in) 

pickle_in = open('StreamlitApp/xgboost.pkl', 'rb') 
xgboost = pickle.load(pickle_in) 
  
@st.cache_data
  
# defining the function which will make the prediction using  
# the data which the user inputs 
def prediction(CompareMedianSalePrice, Bath, Bed, Grocery, Nightlife, Restaurant, CarCommutePercentage, ModelChoice):  
    
    if CompareMedianSalePrice[0] == "Yes":
        CompareMedianSalePrice = 1
    elif CompareMedianSalePrice[0] == "No":
        CompareMedianSalePrice = 0 

    if ModelChoice[0] == "Linear Regression":
        prediction = linear.predict([[CompareMedianSalePrice, Bath[0], Bed[0], Grocery[0], Nightlife[0], Restaurant[0], CarCommutePercentage[0]]])
    elif ModelChoice[0] == "Lasso Regression":
        prediction = lasso.predict([[CompareMedianSalePrice, Bath[0], Bed[0], Grocery[0], Nightlife[0], Restaurant[0], CarCommutePercentage[0]]])
    elif ModelChoice[0] == "XGBoost":
        prediction = xgboost.predict([[CompareMedianSalePrice, Bath[0], Bed[0], Grocery[0], Nightlife[0], Restaurant[0], CarCommutePercentage[0]]])
    
    return prediction 

def main(): 
      
    # the following lines create text boxes in which the user can enter  
    # the data required to make the prediction 
    CompareMedianSalePrice = st.radio("Is the house price higher than the median house sale?", ["Yes", "No"]),
    Bath = st.slider("Select the number of bathrooms", min_value = 0.0, max_value = 5.0, step = 0.5), 
    Bed = st.slider("Select the number of bedrooms", min_value = 1, max_value = 10, step = 1), 
    Grocery = st.slider("Select the number of grocery store closed by", min_value = 0, max_value = 150, step = 1),
    Nightlife = st.slider("Select the number of nightlife activities closed by", min_value = 0, max_value = 425, step = 1),
    Restaurant = st.slider("Select the number of restaurants closed by", min_value = 0, max_value = 1135, step = 1),
    CarCommutePercentage = st.slider("Select the percentage of commuting by car", min_value = 0, max_value = 100, step = 1),
    ModelChoice = st.pills("Select your preferred predictive model", ["Linear Regression", "Lasso Regression", "XGBoost"]),
    result ="" 
      
    # the below line ensures that when the button called 'Predict' is clicked,  
    # the prediction function defined above is called to make the prediction  
    # and store it in the variable result 
    
    if st.button("Predict"): 
        result = prediction(CompareMedianSalePrice, Bath, Bed, Grocery, Nightlife, Restaurant, CarCommutePercentage, ModelChoice) 
        st.success('The predicted sale price is ${}'.format(round(result[0],2))) 
     
if __name__=='__main__': 
    main() 
