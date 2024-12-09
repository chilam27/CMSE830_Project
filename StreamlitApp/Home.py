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

st.write("""
## Objective

Welcome! Our goal for this application is to analyze and predict Boston housing prices using regression models on various features provided by the sources. If you're looking to buy or sell a property or assess the Boston market area, this application is designed to streamline your process and help you make data-driven decisions. The data we collected are from Trulia, the Census, and Redfin. We aim to help you answer these questions:

- What is the current state of the housing market?
- What features have a significant impact on property rent?
- What is the value of my property?

## Dataset
- Trulia dataset: the Boston housing data scraped from [Trulia](https://www.trulia.com/). We used the BeautifulSoup package to extract information from the website for educational purposes only. The dataset includes variables such as sale, address, area, bed, bath, school, crime, commute, shop_eat, description, feature, and URL.
- Census dataset: this is the Census dataset that we requested through its API. We selected a few variables that we think might help us understand the real estate market as well as aiding us in predicting the housing prices. Some of the useful variables include median household income, median age, total population, occupied, vacant, and work commute duration.
- Redfin dataset: the Boston housing market data collected from [Redfin](https://www.redfin.com/), a real estate company that helps people buy, sell, and rent homes. The data is a combination of four separate datasets and includes information such as homes sold, active listings, median sale price, and median sale price per square foot (PPSF). By understanding the past and current state of the housing market, we can make better decisions regarding buying and selling properties.
"""
)





