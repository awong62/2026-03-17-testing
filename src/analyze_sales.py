import pandas as pd
import matplotlib.pyplot as plt

# 1. Loading Data
# Hardcoded file path expects a specific file to exist locally.
df = pd.read_csv("data/raw/monthly_sales.csv")

# 2. Cleaning Data
# Drops missing values and negative revenues.
df = df.dropna(subset=['Revenue'])
df = df[df['Revenue'] > 0]

# 3. Calculating Metric
average_revenue = df['Revenue'].mean()

# 4. Outputting Results
# Prints directly to the console.
print(f"The average monthly revenue is: ${average_revenue:.2f}")

# 5. Plotting
# Generates a plot and saves it directly to the hard drive.
plt.plot(df['Month'], df['Revenue'])
plt.title("Monthly Revenue")
plt.savefig("results/revenue_plot.png")