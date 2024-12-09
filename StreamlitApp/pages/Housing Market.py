# Import libraries
import streamlit as st
import altair as alt
import pandas as pd
import numpy as np
import seaborn as sns
import plotly.express as px
from bokeh.plotting import figure, show
from bokeh.palettes import Spectral4

st.set_page_config(page_title="Housing Market", 
                   page_icon="📈",
                   layout="wide")

st.markdown("# 📈 Housing Market")

st.write("""
Before assessing the specifications of a property, it would save us a lot of time and effort to first analyze the current real estate market. This approach allows us to make better decisions regarding buying or selling a property and at which price point.
""")

st.sidebar.header("Year of Period End Filter")
    
# import dataset
redfin_df = pd.read_csv('redfin_df.csv')

# set filter
cat_list = np.sort(redfin_df.Year_of_Period_End.unique())
val = [None]* len(cat_list)
for i, cat in enumerate(cat_list):
    val[i] = st.sidebar.checkbox(str(cat), value=True)

# filter data based on selection
redfin_filter_df = redfin_df[redfin_df.Year_of_Period_End.isin(cat_list[val])].reset_index(drop = True)
with st.expander("View Redfin processed dataset"):
  if redfin_filter_df.shape[0]>0:
      st.dataframe(redfin_filter_df, height = 250)
      st.write("""
      ### Redfin Dataset Variables
      - *Day of Year sold*: int; the number of days in a year
      
      - *Year of Period End*: int; the year of when the record end
      - *Period Begin*: date; the date of which the record begins
      - *Period End*: date; the date of which the record ends
      - *Active Listings YOY*: float; the year-over-year number of active listings on Redfin's website based on a specific time frame
      - *Active Listings*: int; the number of active listings on Redfin's website based on a specific time frame
      - *Adjusted Average Homes Sold*: int; the number of homes sold based on a specific time frame
      - *Adjusted Average Homes Sold YOY*: float; the year-over-year number of homes sold based on a specific time frame
      - *Median Sale PPSF (price per square foot)*: int; the median sale PPSF of listings on Redfin's website based on a specific time frame
      - *Median Sale PPSF (price per square foot) YOY*: float; the year-over-year median sale PPSF of listings on Redfin's website based on a specific time frame
      - *Median Sale Price*: int; the median sale price of listings on Redfin's website based on a specific time frame
      - *Median Sale Price YOY*: float; the year-over-year median sale price of listings on Redfin's website based on a specific time frame
      """)
  else:
      st.write("Empty Dataframe")


st.divider()

st.write("""
These four plots provide a comprehensive view of the real estate market in Boston. We can observe general trends in active listings and sale prices throughout the years from 2021 to 2024.

Regarding active listings on Redfin, it's common to see a higher number of listings available during the summer, with a decline starting in the fall season. This trend is also reflected in the other three plots.
""")

# set column
col = st.columns(2)

# multiple line plot: active listing
## subset dataset
redfin_2021_df = redfin_filter_df[redfin_filter_df['Year_of_Period_End'] == 2021]
redfin_2022_df = redfin_filter_df[redfin_filter_df['Year_of_Period_End'] == 2022]
redfin_2023_df = redfin_filter_df[redfin_filter_df['Year_of_Period_End'] == 2023]
redfin_2024_df = redfin_filter_df[redfin_filter_df['Year_of_Period_End'] == 2024]

p = figure(title = "Active Listing Throughout The Year", 
           width = 700,
           height = 400,
           x_axis_label = "Day in a Year", 
           y_axis_label = "Active Listings",
           tooltips = "<strong>Day of year:</strong> @x <br> <strong>Active Listing:</strong> @y")

for df, name, color in zip([redfin_2021_df, redfin_2022_df, redfin_2023_df, redfin_2024_df], ["2021", "2022", "2023", "2024"], Spectral4):
    p.line(df['Day_of_Year'], df['Active_Listings'], line_width=2, color=color, alpha=0.8, legend_label=name)

p.legend.location = "top_right"
p.legend.click_policy="hide"

col[0].bokeh_chart(p, use_container_width = True)

# multiple line plot: home sold
## subset dataset
redfin_2021_df = redfin_filter_df[redfin_filter_df['Year_of_Period_End'] == 2021]
redfin_2022_df = redfin_filter_df[redfin_filter_df['Year_of_Period_End'] == 2022]
redfin_2023_df = redfin_filter_df[redfin_filter_df['Year_of_Period_End'] == 2023]
redfin_2024_df = redfin_filter_df[redfin_filter_df['Year_of_Period_End'] == 2024]

p = figure(title = "Home Sold Throughout The Year", 
           width = 700,
           height = 400,
           x_axis_label = "Day in a Year", 
           y_axis_label = "Home Sold",
           tooltips = "<strong>Day of year:</strong> @x <br> <strong>Home Sold:</strong> @y")

for df, name, color in zip([redfin_2021_df, redfin_2022_df, redfin_2023_df, redfin_2024_df], ["2021", "2022", "2023", "2024"], Spectral4):
    p.line(df['Day_of_Year'], df['Adjusted_Average_Homes_Sold'], line_width=2, color=color, alpha=0.8, legend_label=name)

p.legend.location = "top_right"
p.legend.click_policy="hide"

col[1].bokeh_chart(p, use_container_width = True)

# multiple line plot: median sale price
## subset dataset
redfin_2021_df = redfin_filter_df[redfin_filter_df['Year_of_Period_End'] == 2021]
redfin_2022_df = redfin_filter_df[redfin_filter_df['Year_of_Period_End'] == 2022]
redfin_2023_df = redfin_filter_df[redfin_filter_df['Year_of_Period_End'] == 2023]
redfin_2024_df = redfin_filter_df[redfin_filter_df['Year_of_Period_End'] == 2024]

p = figure(title = "Median Sale Price Throughout The Year", 
           width = 700,
           height = 400,
           x_axis_label = "Day in a Year", 
           y_axis_label = "Median Sale Price",
           tooltips = "<strong>Day of year:</strong> @x <br> <strong>Median Sale Price:</strong> @y")

for df, name, color in zip([redfin_2021_df, redfin_2022_df, redfin_2023_df, redfin_2024_df], ["2021", "2022", "2023", "2024"], Spectral4):
    p.line(df['Day_of_Year'], df['Median_Sale_Price'], line_width=2, color=color, alpha=0.8, legend_label=name)

p.legend.location = "top_right"
p.legend.click_policy="hide"

col[0].bokeh_chart(p, use_container_width = True)

# multiple line plot: median sale price per square foot
## subset dataset
redfin_2021_df = redfin_filter_df[redfin_filter_df['Year_of_Period_End'] == 2021]
redfin_2022_df = redfin_filter_df[redfin_filter_df['Year_of_Period_End'] == 2022]
redfin_2023_df = redfin_filter_df[redfin_filter_df['Year_of_Period_End'] == 2023]
redfin_2024_df = redfin_filter_df[redfin_filter_df['Year_of_Period_End'] == 2024]

p = figure(title = "Median Sale PPSF Throughout The Year", 
           width = 700,
           height = 400,
           x_axis_label = "Day in a Year", 
           y_axis_label = "Median Sale PPSF",
           tooltips = "<strong>Day of year:</strong> @x <br> <strong>Median Sale PPSF:</strong> @y")

for df, name, color in zip([redfin_2021_df, redfin_2022_df, redfin_2023_df, redfin_2024_df], ["2021", "2022", "2023", "2024"], Spectral4):
    p.line(df['Day_of_Year'], df['Median_Sale_ppsf'], line_width=2, color=color, alpha=0.8, legend_label=name)

p.legend.location = "top_right"
p.legend.click_policy="hide"

col[1].bokeh_chart(p, use_container_width = True)

# rerun.
st.button("Re-run")
