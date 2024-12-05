# CMSE 830 midterm and final project

<p align="center">
  <img width="800" height="300" src="https://github.com/chilam27/CMSE830_Project/blob/main/StreamlitApp/image/house.png">
</p>

## Objective
My goal for this project is analyze and predict Boston housing prices based on a regression model though a number of features that the source provides. The data I collected are from Trulia, the Census, and Redfin. By the end of the project, I am hoping to be able to answer these questions:

- What is the current stage of the housing market?
- What are the features that have high effect on to the rent of a property?
- How good is our prediction for the rent of the property?

## Project Outline
The following are the outline steps that I will be performing:

- Data collection: use BeautifulSoup to scrape property data from Trulia, a popular real estate website. Gather all listed variables that can be used for data analysis; download Census data through its API, a provider of data on the National, State, and Local levels that help define who we are as a nation and the makeup of the people that live in this country; download housing market data that is available on Redfin, a real estate company that offers services for buying, selling, renting, and financing homes.
- Data cleaning: read in data and prepare it for data analysis; steps include: tidy up the categorical features, deal with null value, etc.
- Exploratory data analysis (EDA): examine the cleaned data and its trends through Streamlit.
- Model building: determine which model (Linear, Lasso, XGBoost) work best (that return the smallest error) and tune the model with different parameters using GridSearchCV.
- Deploy Application: save all relevant files to a [GitHub repository](https://github.com/chilam27/CMSE830_Project?tab=readme-ov-file) and deploy the application onto Streamlit Community Cloud.

## Streamlit Application: [Boston Housing Market](https://daochilam-cmse830-bostonhousemarket.streamlit.app/)
