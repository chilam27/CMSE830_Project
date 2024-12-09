# Import libraries
import streamlit as st
import pandas as pd
import altair as alt
import streamlit.components.v1 as components


# Page configuration
st.set_page_config(
    page_title="Boston Housing Market",
    page_icon="🏘️",
    layout="wide",
    initial_sidebar_state="expanded")

alt.themes.enable("dark")

st.markdown("# Analyzing and Predicting Boston House Market")

st.image("StreamlitApp/image/house.png", caption= "iStock: Typical Brownstone Row Houses in Back Bay Boston Massachusetts USA stock photo", width = 1100, use_column_width = None, clamp = False, channels = "RGB", output_format = "auto")

st.markdown("## Objective")

st.write(
    """My goal for this project is analyze and predict Boston housing prices based on a regression model though a number of features that the source provides. The data I collected are from Trulia, the Census, and Redfin. By the end of the project, I am hoping to be able to answer these questions:

- What is the current state of the housing market?
- What are the features that have high effect on to the rent of a property?
- How good is our prediction for the rent of the property?

## Project Outline

The following are the outline steps that I will be performing: <u>text</u>

- Data collection: use BeautifulSoup to scrape property data from Trulia, a popular real estate website. Gather all listed variables that can be used for data analysis; download Census data through its API, a provider of data on the National, State, and Local levels that help define who we are as a nation and the makeup of the people that live in this country; download housing market data that is available on Redfin, a real estate company that offers services for buying, selling, renting, and financing homes.
- Data cleaning: read in data and prepare it for data analysis; steps include: tidy up the categorical features, deal with null value, etc.
- Exploratory data analysis (EDA): examine the cleaned data and its trends through Streamlit.
- Model building: determine which model (Linear, Lasso, XGBoost) work best (that return the smallest error) and tune the model with different parameters using GridSearchCV.
- Deploy Application: save all relevant files to a [GitHub repository](https://github.com/chilam27/CMSE830_Project?tab=readme-ov-file) and deploy the application onto Streamlit Community Cloud."

## Dataset
- Trulia dataset: the Boston housing data scraped from [Trulia](https://www.trulia.com/). We used the BeautifulSoup package to extract information from the website for educational purposes only. The dataset includes variables such as sale, address, area, bed, bath, school, crime, commute, shop_eat, description, feature, and URL.
- Census dataset: this is the Census dataset that we requested through its API. We selected a few variables that we think might help us understand the real estate market as well as aiding us in predicting the housing prices. Some of the useful variables include median household income, median age, total population, occupied, vacant, and work commute duration.
- Redfin dataset: the Boston housing market data collected from [Redfin](https://www.redfin.com/), a real estate company that helps people buy, sell, and rent homes. The data is a combination of four separate datasets and includes information such as homes sold, active listings, median sale price, and median sale price per square foot (PPSF). By understanding the past and current state of the housing market, we can make better decisions regarding buying and selling properties.
"""
)





