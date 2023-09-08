import pandas as pd

# Read the CSV file into a DataFrame
df_cocoa = pd.read_csv('C:/Users/keera/Files/DBMS/flavors_of_cocoa.csv')

# Question 1: Check for null values in the DataFrame
null_columns = df_cocoa.columns[df_cocoa.isnull().any()]
print("Variables with null values:", null_columns)

# Question 2: Find the country with the maximum locations of cocoa manufacturing companies
country_with_max_locations = df_cocoa['Company Location'].value_counts().idxmax()
print("Country with maximum locations of cocoa manufacturing companies:", country_with_max_locations)

# Question 3: Check the data types of the features
print("Data types of features:")
print(df_cocoa.dtypes)

# Question 4: Find the maximum rating of chocolates
max_rating = df_cocoa['Rating'].max()
print("Maximum rating of chocolates:", max_rating)
