import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
data = pd.read_csv('C:/Users/keera/Files/DBMS/diamond.csv')

# Create a boxplot
plt.figure(figsize=(10, 6))
sns.boxplot(x='cut', y='price', data=data, order=["Fair", "Good", "Very Good", "Premium", "Ideal"])
plt.title('Boxplot of Price vs Cut')
plt.xlabel('Cut')
plt.ylabel('Price')
plt.xticks(rotation=45)
plt.grid(True)

# Calculate the median price for each cut category
median_prices = data.groupby('cut')['price'].median()
highest_median_cut = median_prices.idxmax()
highest_median_price = median_prices.max()

# Display the cut with the highest median price
print(f"The category with the highest median price is '{highest_median_cut}' with a median price of ${highest_median_price:.2f}")

# Show the boxplot
plt.tight_layout()
plt.show()
