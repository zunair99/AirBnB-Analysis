#importing necessary libraries
import pandas as pd
import matplotlib as mp
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import seaborn as sb


#importing and reading dataset
airbnb = pd.read_csv('Airbnb\AB_NYC_2019.csv\AB_NYC_2019.csv')
airbnb.describe()
airbnb.dtypes
#cleaning dataset of null values
airbnb.isnull().any() #columns that have null values: name, host_name, last_review, reviews_per_month
airbnb.isnull().sum() #16 null values in name, 21 null values in host_name, 10052 null values in each reviews_per_month and last_review
cleanbnb = airbnb.drop(['name', 'host_name', 'last_review', 'reviews_per_month'], axis = 1) #dropping unnecessary columns with null values
cleanbnb.isnull().any() #confirming that cleaned dataset has no null values
cleanbnb.isna().sum() #confirming no NA values in cleaned dataset

cleanbnb.head()
cleanbnb.tail()
cleanbnb.describe() #48895 instances of airbnb data within this dataset
#mean price is about $153
#mean minumum number of nights is around 7 nights per airbnb
#mean number of reviews per airbnb is about 23

#correlation analysis using matplotlib
correlation = cleanbnb.corr(method = 'pearson')
corr_fig = plt.figure(figsize = (6,6))
sb.heatmap(correlation)
plt.show()


#correlation heatmap shows little correlation among variables

#data visualization using seaborn
cleanbnb.columns
cleanbnb['neighbourhood'].unique()
cleanbnb['neighbourhood'].nunique() #221 unique neighborhoods
cleanbnb['room_type'].unique()
cleanbnb['room_type'].nunique() #3 unique types of rooms

#Occurrences of Different Types of AirBnB Residences
sb.countplot(cleanbnb['room_type'], palette = "Set2")
plt.title("Occurrences of Different Room Types on AirBnB")
plt.show()
#Majority of airbnbs are private rooms or entire houses/apartments

#AirBnB Price vs Availability, Using Room Type as Filtering Hue
sb.scatterplot(x = cleanbnb['availability_365'], y = cleanbnb['price'], hue = cleanbnb['room_type'])
plt.title("Relationship Between AirBnB Price and AirBnB Availability Factoring in Room Type")
plt.show()

#Neighborhood Group Occurrences on AirBnB Residences
sb.countplot(cleanbnb['neighbourhood_group'], palette = "Set2")
plt.title("Ocurrences of Different Neighbourhood Groups")
plt.show()
#Most AirBnB Residences in Brooklyn and Manhattan (significantly higher than other neighborhoods)

#Neighborhood Occurrences on AirBnB Residences
sb.countplot(cleanbnb['neighbourhood'], palette = "Set2")
plt.title("Different Neighbourhoods of AirBnB Residences")
plt.show()

#Neighbourhood Group Map
sb.scatterplot(x = cleanbnb['latitude'], y = cleanbnb['longitude'], hue = cleanbnb['neighbourhood_group'])
plt.title("Map of Neighbourhood Groups")
plt.show()

#Price Map
sb.scatterplot(x = cleanbnb['latitude'], y = cleanbnb['longitude'], hue = cleanbnb['price'])
plt.title("Map of Prices")
plt.show()

#Availability Map
sb.scatterplot(x = cleanbnb['latitude'], y = cleanbnb['longitude'], hue = cleanbnb['availability_365'])
plt.title("Map of Availability")
plt.show()

#Room Type Map
sb.scatterplot(x = cleanbnb['latitude'], y = cleanbnb['longitude'], hue = cleanbnb['room_type'])
plt.title("Map of Room Types")
plt.show()

