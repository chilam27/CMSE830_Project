# Import libraries
import streamlit as st
import altair as alt
import pandas as pd
import numpy as np
from bokeh.plotting import figure
from bokeh.palettes import Spectral4

st.set_page_config(page_title="Housing Market", 
                   page_icon="📈",
                   layout="wide")

st.markdown("# Housing Market")

st.write(
    """This is the Boston house market data collected from [Redfin](https://www.redfin.com/), a real estate company that offers services to help people buy, sell, and rent homes. The data is a combination of 4 separate datasets and it includes information such as homes sold, active listings, median sale price, and median Sale PPSF (price per square foot). By understanding the past and current state of the housing market as a whole, we can make better decision regarding buying and selling houses."""
)

st.sidebar.header("Year of Period End Filter")
    
# import dataset
redfin_df = pd.read_csv('StreamlitApp/redfin_df.csv')

# set filter
cat_list = np.sort(redfin_df.Year_of_Period_End.unique())
val = [None]* len(cat_list)
for i, cat in enumerate(cat_list):
    val[i] = st.sidebar.checkbox(str(cat), value=True)

# filter data based on selection
redfin_filter_df = redfin_df[redfin_df.Year_of_Period_End.isin(cat_list[val])].reset_index(drop=True)
if redfin_filter_df.shape[0]>0:
    st.dataframe(redfin_filter_df)
else:
    st.write("Empty Dataframe")

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
