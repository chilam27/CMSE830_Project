# Import libraries
import streamlit as st
import altair as alt
import pandas as pd
import numpy as np
import seaborn as sns
import plotly.express as px
from bokeh.plotting import figure, show
from bokeh.palettes import Spectral4

st.set_page_config(page_title="Price Prediction", 
                   page_icon="🧮",
                   layout="wide")

st.markdown("# House Market")
st.sidebar.header("House Market")
st.write(
    """This is the Boston house market data collected from [Redfin](https://www.redfin.com/). The data includes relevant information such as homes sold, active listings, median sale price, and median Sale PPSF (price per square foot)"""
)

st.sidebar.header("Filter")