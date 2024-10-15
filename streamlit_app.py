# Import libraries
import streamlit as st
import altair as alt
import pandas as pd
import seaborn as sns
from bokeh.plotting import figure
from bokeh.models import ColumnDataSource
from bokeh.embed import components

# Page configuration
st.set_page_config(
    page_title="Boston Housing Market",
    page_icon="🏘️",
    layout="wide",
    initial_sidebar_state="expanded")

alt.themes.enable("dark")

# Load data
trulia_df = pd.read_csv('trulia_df.csv')
redfin_df = pd.read_csv('redfin_df.csv')

# Line plot
st.title("Bokeh Line Plot in Streamlit")

x_column = redfin_df["Period_End"]
y_column = redfin_df["Median_Sale_ppsf"]

grouped = redfin_df.groupby("Year_of_Period_End")

st.write(f"Line plot for {x_column} vs {y_column}")

palette = Category10[10]
color_idx = 0 

for name, group in grouped:
    source = ColumnDataSource(redfin_df)
    
    p.line(x=x_column, y=y_column, source=source, line_width=2, 
           legend_label=str(name), color=palette[color_idx % len(palette)])
    color_idx += 1

p.legend.title = group_column
p.legend.location = "top_left"

script, div = components(p)
st.components.v1.html(f"{script}{div}", height=500)

# Correlation heatmap
corr = trulia_df.corr()
st.write("Correlation Heatmap:")

plt.figure(figsize=(10, 6))
sns.heatmap(corr, annot=True, cmap='coolwarm', center=0)

st.pyplot(plt)

