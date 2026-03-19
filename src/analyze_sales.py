import pandas as pd
import matplotlib.pyplot as plt

def get_script_name():
    return(__name__)

# 1. Loading Data
def load_data(filename):
    """This function loads data. Example: load_data("data/raw/monthly_sales.csv")"""
    df = pd.read_csv(filename)
    return df

# 2. Cleaning Data
# Drops missing values and negative revenues.
def clean_data(df):
    cleaned_df = df.dropna(subset=['Revenue']).copy()
    cleaned_df = cleaned_df[cleaned_df['Revenue'] > 0]
    return cleaned_df

# 3. Calculating Metric
def calculate_average_revenue(df):
    if df.empty:
        raise ValueError("Cannot calculate average on an empty DataFrame.")
    average_revenue = df['Revenue'].mean()
    return average_revenue

# 4. Plotting
def create_revenue_plot(df):
    fig, ax = plt.subplots()
    ax.plot(df['Month'], df['Revenue'])
    ax.set_title("Monthly Revenue")
    return fig

#plt.plot(df['Month'], df['Revenue'])
#plt.title("Monthly Revenue")
#plt.savefig("results/revenue_plot.png")

if __name__ == "__main__":
    filename = "data/raw/monthly_sales.csv"
    df = load_data(filename)
    cleaned_df = clean_data(df)

    average_revenue = calculate_average_revenue(cleaned_df)
    print(f"The average monthly revenue is: ${average_revenue:.2f}")

    revenue_fig = create_revenue_plot(cleaned_df)
    revenue_fig.savefig("results/revenue_plot.png")    
