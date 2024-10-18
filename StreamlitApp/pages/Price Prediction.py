# Import libraries
import streamlit as st
import altair as alt
import pandas as pd
import numpy as np
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

st.set_page_config(page_title="Price Prediction", 
                   page_icon="🧮",
                   layout="wide")

st.markdown("# House Price Prediction")

st.sidebar.header("Model Performance")

st.write(
    """This is the Boston house market data collected from [Redfin](https://www.redfin.com/). The data includes relevant information such as homes sold, active listings, median sale price, and median Sale PPSF (price per square foot)"""
)
