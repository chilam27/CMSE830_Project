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
    """My goal for this project is analyze and predict Boston housing prices based on a regression model though a number of features that the source provides. The data I collected are from Trulia and Redfin. By the end of the project, I am hoping to be able to answer these questions:

- What is the current state of the housing market?
- What are the features that have high effect on to the rent of a property?
- How good is our prediction for the rent of the property?
"""
)

st.markdown("## Project Outline")

st.write(
    """The following are the outline steps that I will be performing: <u>text</u>

- Data collection: use BeautifulSoup to scrape property data from Trulia, a popular real estate website. Gather all listed variables that can be used for data analysis; download housing market data that is available on Redfin, a real estate company that offers services for buying, selling, renting, and financing homes.
- Data cleaning: read in data and prepare it for data analysis; steps include: tidy up the categorical features, deal with null value, etc.
- Exploratory data analysis (EDA): examine the cleaned data and its trends through Streamlit.
- Model building: determine which model (Linear, Lasso, Random Forest) work best (that return the smallest error) and tune the model with different parameters using GridSearchCV.
- Deploy Application: save all relevant files to a [GitHub repository](https://github.com/chilam27/CMSE830_Project?tab=readme-ov-file) and deploy the application onto Streamlit Community Cloud."
"""
)

st.divider()

# display notebook as html
path_to_html = "./CMSE830_Project.html" 

with open(path_to_html,'r') as f: 
    html_data = f.read()

## Show in webpage
with st.expander("Data Collecting & Processing Notebook (HTML)"):
    st.components.v1.html(html_data, scrolling=True, height=800)
