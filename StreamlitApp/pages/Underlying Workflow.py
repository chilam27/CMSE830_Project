# Import libraries
import streamlit as st
import pandas as pd
import altair as alt
import streamlit.components.v1 as components

st.set_page_config(page_title="Underlying Methodology", 
                   page_icon="🔬",
                   layout="wide")

st.markdown("# 🔬 Underlying Methodology")

## Project Outline
st.write("""
## Project Outline

The following are the outline steps that I will be performing: <u>text</u>

- Data collection: use BeautifulSoup to scrape property data from Trulia, a popular real estate website. Gather all listed variables that can be used for data analysis; download Census data through its API, a provider of data on the National, State, and Local levels that help define who we are as a nation and the makeup of the people that live in this country; download housing market data that is available on Redfin, a real estate company that offers services for buying, selling, renting, and financing homes.
- Data cleaning: read in data and prepare it for data analysis; steps include: tidy up the categorical features, deal with null value, etc.
- Exploratory data analysis (EDA): examine the cleaned data and its trends through Streamlit.
- Model building: determine which model (Linear, Lasso, XGBoost) work best (that return the smallest error) and tune the model with different parameters using GridSearchCV.
- Deploy Application: save all relevant files to a [GitHub repository](https://github.com/chilam27/CMSE830_Project?tab=readme-ov-file) and deploy the application onto Streamlit Community Cloud."

## Underlying Workflow Notebook
""")

# display notebook as html
path_to_html = "StreamlitApp/CMSE830_project.html"

with open(path_to_html,'r') as f: 
    html_data = f.read()

# Show in webpage
st.components.v1.html(html_data, scrolling=True, height=800)
