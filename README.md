# CMSE830_Project
CMSE 830 midterm and final project

My goal for this project is analyze and predict Boston housing prices based on a regression model though a number of features that the source provides. The data I collected are from Trulia and Redfin. By the end of the project, I am hoping to be able to answer these questions:

- What is the current stage of the housing market?
- What are the features that have high effect on to the rent of a property?
- How good is our prediction for the rent of the property?

The following are the outline steps that I will be performing:

- Data collection: use BeautifulSoup to scrape property data from Trulia, a popular real estate website. Gather all listed variables that can be used for data analysis; download - housing market data that is available on Redfin, a real estate company that offers services for buying, selling, renting, and financing homes.
- Data cleaning: read in data and prepare it for data analysis; steps include: tidy up the categorical features, deal with null value, etc.
- Exploratory data analysis (EDA): examine the cleaned data and its trends through Streamlit.
- Model building: determine which model (Linear, Lasso, Random Forest) work best (that return the smallest error) and tune the model with different parameters using GridSearchCV.

http://localhost:8501/
