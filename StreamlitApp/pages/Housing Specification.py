# Import libraries
import streamlit as st
import altair as alt
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.figure_factory as ff
import geopandas as gpd
from shapely import wkt

st.set_page_config(page_title="House Specification", 
                   page_icon="📝",
                   layout="wide")

st.markdown("# 📝 House Specification")

st.write(
    """This is the Boston housing data scrapped from [Trulia](https://www.trulia.com/). We used the `BeautifulSoup` package to scrape the information from the website for educational purposes only. The data contains variables such as sale, address, area, bed, bath, school, crime, commute, shop_eat, description, feature, URL. Below is the Trulia dataset that has been cleaned and processed."""
)

st.sidebar.header("Processed Dataset Summary")

st.sidebar.markdown(
    """### Size
- Rows: 2659
- Columns: 13

### Trulia Variables
- *Sale*: int; sale price of the house
- *Area*: object; the area that the house is located at
- *Bed*: float; number of bedrooms in a house
- *Bath*: float; number of bathrooms in a house
- *Crime_Rate*: int; crime rate from 1-5
- *Car_Commute_Percentage*: float; proportion of people in the area commute by car
- *Elemenatary_School*: int; number of elementary schools nearby  
- *Middle_School*: int; number of middle schools nearby  
- *High_School*: int; number of high schools nearby
- *Total_School*: int; number of schools nearby
- *Restaurant*: int; number of restaurants nearby
- *Grocery*: int; number of grocery stores nearby
- *Nightlife*: int; number of nightlife activities nearby

### Census Variables
- *Median Household Income*: float; median household income by neighborhood
- *Median Age*: float; median age by neighborhood
- *Total Population*: int; total population by neighborhood
- *Occupied*: int; number of occupancy by neighborhood
- *Vacant*: int; number of vacancy by neighborhood
- *Work Commute Short*: float; number of people commute < 15 minutes to work
- *Work Commute Average*: float; number of people commute 15-45 minutes to work
- *Work Commute Long*: float; number of people commute > 45 minutes to work
""")


# import dataset
trulia_df = pd.read_csv('StreamlitApp/final_df.csv')
census_cleanned = pd.read_csv('StreamlitApp/census_df.csv')
sale_stats = pd.read_csv('StreamlitApp/sale_stats.csv')

# display dataset
st.dataframe(trulia_df)

st.write(
    """This is the Census dataset that we requested through its API. We selected a few variables that we think it might help with us understand the real estate market as well as aiding us in predicting the housing prices. Some of the useful variables include median household income, median age, total population, occupied, vacant, and work commute duration."""
)

st.dataframe(census_cleanned)

st.divider()

# "Sale" distribution plot
fig = px.histogram(trulia_df, x="Sale")
fig.update_layout(title='Sale Distribtuion', width=1100, height=500)
st.plotly_chart(fig)

# Sale statistics expander
with st.expander("Sale variable basic summary statistics"):
    st.dataframe(sale_stats, width=1200)

st.divider()

# correlation heatmap
trulia_num_df = trulia_df.select_dtypes(include = np.number)
corr_matrix = trulia_num_df.corr()

# create the heatmap
fig = px.imshow(corr_matrix,
                x=corr_matrix.columns,
                y=corr_matrix.columns,
                color_continuous_scale='RdBu_r',
                zmin=-1, zmax=1)

## customize the appearance
fig.update_layout(title='Correlation Matrix', width=1200, height=500)

st.plotly_chart(fig)

st.divider()

tab1, tab2= st.tabs(["📦 Box Plot", "🗺️ Map Plot"])

with tab1:
    # box plot
    fig = px.box(trulia_df, x="Area", y="Sale", color = "Area")
    fig.update_layout(title='Sale Box Plot Grouped by Neighborhood', width=1100, height=800, showlegend=False)
    st.plotly_chart(fig)

with tab2:
    # map plot
    census_cleanned['Geometry'] = census_cleanned['Geometry'].apply(wkt.loads)
    median_sale_area = trulia_df[['Area', 'Sale']].groupby(['Area'], as_index = False).median()
    geo_df = pd.merge(census_cleanned, median_sale_area, 'right', on = 'Area').set_index('Area')
    geo_df = gpd.GeoDataFrame(geo_df, geometry = 'Geometry')
    
    fig = px.choropleth_mapbox(geo_df,
                               geojson = geo_df.geometry,
                               locations = geo_df.index,
                               color = geo_df['Sale'],
                               color_continuous_scale = 'Viridis',
                               opacity = 0.75,
                               center = {"lat": 42.32, "lon": -71.0889},
                               mapbox_style = "carto-positron",
                               # width = 1000,
                               height = 1000,
                               zoom = 11,
                               title = 'Sale Map Plot Grouped by Neighborhood',
                               hover_data = ['Sale', 'Total Population', 'Median Household Income', 'Median Age']
                              )
    fig.update_layout(xaxis=dict(autorange=True), yaxis=dict(autorange=True))
    st.plotly_chart(fig)

st.divider()

# "Sale" vs "Bath" scatter plot plot
fig = px.scatter(trulia_df, x="Bath", y="Sale", trendline="ols", trendline_color_override = "white")
fig.update_layout(title='Sale vs. Bath Scatter Plot', width=1100, height=500)
st.plotly_chart(fig)

st.divider()

# "Sale" vs "Bed" scatter plot plot
fig = px.scatter(trulia_df, x="Bed", y="Sale", trendline="ols", trendline_color_override = "white")
fig.update_layout(title='Sale vs. Bed Scatter Plot', width=1100, height=500)
st.plotly_chart(fig)
