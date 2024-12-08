# Import libraries
import streamlit as st
import pandas as pd
import altair as alt
import streamlit.components.v1 as components

st.set_page_config(page_title="Underlying Methodology", 
                   page_icon="🔬",
                   layout="wide")

st.markdown("# 🔬 Underlying Methodology")

# display notebook as html
path_to_html = "StreamlitApp/CMSE830_project.html"

with open(path_to_html,'r') as f: 
    html_data = f.read()

# Show in webpage
with st.expander("Workflow Notebook (HTML)"):
    st.components.v1.html(html_data, scrolling=True, height=800)
