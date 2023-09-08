import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv('C:/Users/keera/Files/DBMS/mtcars.csv')

# Extract 'mpg' and 'wt' columns
mpg = data['mpg']
weight = data['wt']

# Create a scatter plot
plt.scatter(weight, mpg, color='blue')
plt.title('Scatter Plot of MPG vs Weight')
plt.xlabel('Weight')
plt.ylabel('MPG')
plt.grid(True)

# Calculate the correlation coefficient
correlation = mpg.corr(weight)

# Display the correlation coefficient
print("Correlation coefficient between MPG and Weight:", correlation)

# Infer the relationship based on the correlation coefficient
if correlation < 0:
    print("As weight of the car increases, the mpg decreases")
elif correlation > 0:
    print("As weight of the car increases, the mpg increases")
else:
    print("There is no relation between weight of the car and mpg")

# Show the scatter plot
plt.show()
