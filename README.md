# CMSE 830 midterm and final project

<p align="center">
  <img width="800" height="300" src="https://github.com/chilam27/CMSE830_Project/blob/main/StreamlitApp/image/house.png">
</p>

## Objective

Welcome! Our goal for this application is to analyze and predict Boston housing prices using regression models on various features provided by the sources. The data we collected are from Trulia, the Census, and Redfin. We aim to help you answer these questions:

- What is the current state of the housing market?
- What features have a significant impact on property rent?
- What is the value of my property?

## Project Outline

The following are the outline steps that I will be performing:

- Data collection: use BeautifulSoup to scrape property data from Trulia, a popular real estate website. Gather all listed variables that can be used for data analysis; download Census data through its API, a provider of data on the National, State, and Local levels that help define who we are as a nation and the makeup of the people that live in this country; download housing market data that is available on Redfin, a real estate company that offers services for buying, selling, renting, and financing homes.
- Data cleaning: read in data and prepare it for data analysis; steps include: tidy up the categorical features, deal with null value, etc.
- Exploratory data analysis (EDA): examine the cleaned data and its trends through Streamlit.
- Model building: determine which model (Linear Regression, Lasso Regression, XGBoost Regressor, Gradient Boosting Regressor) work best (that return the smallest error) and tune the model with different parameters using RandomizedSearchCV.
- Deploy Application: save all relevant files to this GitHub repository and deploy the application onto Streamlit Community Cloud.

## Dataset

### Trulia dataset

The Boston housing data scraped from [Trulia](https://www.trulia.com/). We used the BeautifulSoup package to extract information from the website for educational purposes only. The dataset includes variables such as sale, address, area, bed, bath, school, crime, commute, shop_eat, description, feature, and URL.

- 'sale': the sale of the property listed on the website
- 'address': the address of the property
- 'area': neighborhood the property located
- 'bed': number of beds provided
- 'bath': number of bathrooms provided
- 'school': number of school around the area
- 'crime': crime rate of the area
- 'commute': percentage of people commute by car
- 'shop_eat': number of shops and restaurants in the area
- 'description': description of the property
- 'feature': item that property provides (heating, laundry, etc.)
- 'URL': link to the property

### Census dataset

This is the Census dataset that we requested through its API. We selected a few variables that we think might help us understand the real estate market as well as aiding us in predicting the housing prices. Some of the useful variables include median household income, median age, total population, occupied, vacant, and work commute duration.

- 'State': the state of where the record is located
- 'County': the county of where the record is located
- 'Tract': the tract of where the record is located
- 'Location Name': the longer name of where the record is located
- 'Total Population': the total population of where the record is located
- 'Median Household Income': the median household income of where the record is located
- 'Median Age': the median age of where the record is located
- 'Occupied': the occupation count of where the record is located
- 'Vacant': the vacancy count of where the record is located
- 'Work Commute < 10 minutes': the number of people who commute less than 10 minutes to work of where the record is located
- 'Work Commute 10-14 minutes': the number of people who commute between 10-14 minutes to work of where the record is located
- 'Work Commute 15-19 minutes': the number of people who commute between 15-19 minutes to work of where the record is located
- 'Work Commute 20-24 minutes': the number of people who commute between 20-24 minutes to work of where the record is located
- 'Work Commute 25-29 minutes': the number of people who commute between 25-29 minutes to work of where the record is located
- 'Work Commute 30-34 minutes': the amount of people who commute between 30-34 minutes to work of where the record is located
- 'Work Commute 35-44 minutes': the number of people who commute between 35-44 minutes to work of where the record is located
- 'Work Commute 45-59 minutes': the number of people who commute between 45-59 minutes to work of where the record is located
- 'Work Commute > 60 minutes': the number of people who commute more than 60 minutes to work of where the record is located
- 'Geometry': a geometry data type representing an area that is enclosed by a linear ring

### Redfin dataset:

The Boston housing market data collected from [Redfin](https://www.redfin.com/), a real estate company that helps people buy, sell, and rent homes. The data is a combination of four separate datasets and includes information such as homes sold, active listings, median sale price, and median sale price per square foot (PPSF). By understanding the past and current state of the housing market, we can make better decisions regarding buying and selling properties.

- homes sold: the number of homes sold based on a specific time frame
- active listings: the number of active listings on Redfin's website based on a specific time frame
- median sale price: the median sale price of listings on Redfin's website based on a specific time frame
- median sale PPSF (price per square foot): the median sale PPSF of listings on Redfin's website based on a specific time frame

## Streamlit Application: [Boston Housing Market](https://daochilam-cmse830-bostonhousemarket.streamlit.app/)
