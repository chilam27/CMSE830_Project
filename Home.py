# Import libraries
import streamlit as st
import altair as alt
import pandas as pd
import numpy as np
import seaborn as sns
import plotly.express as px
from bokeh.plotting import figure, show
from bokeh.palettes import Spectral4

# Page configuration
st.set_page_config(
    page_title="Boston Housing Market",
    page_icon="🏘️",
    layout="wide",
    initial_sidebar_state="expanded")

alt.themes.enable("dark")

st.markdown("# Analyzing and Predicting Boston House Market")

st.write(
    """My goal for this project is analyze and predict Boston housing prices based on a regression model though a number of features that the source provides. The data I collected are from Trulia and Redfin. By the end of the project, I am hoping to be able to answer these questions:

- What is the current stage of the housing market?
- What are the features that have high effect on to the rent of a property?
- How good is our prediction for the rent of the property?

The following are the outline steps that I will be performing:

- Data collection: use BeautifulSoup to scrape property data from Trulia, a popular real estate website. Gather all listed variables that can be used for data analysis; download housing market data that is available on Redfin, a real estate company that offers services for buying, selling, renting, and financing homes.
- Data cleaning: read in data and prepare it for data analysis; steps include: tidy up the categorical features, deal with null value, etc.
- Exploratory data analysis (EDA): examine the cleaned data and its trends through Streamlit.
- Model building: determine which model (Linear, Lasso, Random Forest) work best (that return the smallest error) and tune the model with different parameters using GridSearchCV.
"""
)

# display PDF
# def displayPDF(file):
#     # Opening file from file path
#     with open(file, "rb") as f:
#         base64_pdf = base64.b64encode(f.read()).decode('utf-8')

#     # Embedding PDF in HTML
#     pdf_display = F'<iframe src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf"></iframe>'

#     # Displaying File
#     st.markdown(pdf_display, unsafe_allow_html=True)

# displayPDF()





