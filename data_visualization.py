import pandas as pd
import matplotlib.pyplot as plt

# Load Dataset
df = pd.read_csv("sales_data.csv")

print("=" * 50)
print("DATA VISUALIZATION PROJECT")
print("=" * 50)

# Display Dataset
print("\nSales Dataset:\n")
print(df)

# Basic Statistics
print("\nSummary Statistics:\n")
print(df.describe())

# Line Chart
plt.figure(figsize=(8,5))
plt.plot(df["Month"], df["Sales"], marker="o")
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.savefig("line_chart.png")
plt.show()

# Bar Chart
plt.figure(figsize=(8,5))
plt.bar(df["Month"], df["Sales"])
plt.title("Monthly Sales Comparison")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("bar_chart.png")
plt.show()

print("\nCharts generated successfully.")
