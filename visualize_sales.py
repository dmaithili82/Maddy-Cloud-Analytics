import pandas as pd
import matplotlib.pyplot as plt
import os

# Load data
data_path = os.path.join("data", "sample_sales.csv")
df = pd.read_csv(data_path)

# Ensure output folder exists
os.makedirs("output", exist_ok=True)

# 🔹 Total Sales by Product
summary_product = df.groupby("Product")["Sales"].sum().reset_index()
plt.figure(figsize=(8,5))
plt.bar(summary_product["Product"], summary_product["Sales"], color="teal")
plt.title("Total Sales by Product")
plt.xlabel("Product")
plt.ylabel("Sales ($)")
plt.tight_layout()
plt.savefig(os.path.join("output", "sales_by_product.png"))
plt.close()

# 🔹 Total Sales by Region
summary_region = df.groupby("Region")["Sales"].sum().reset_index()
plt.figure(figsize=(8,5))
plt.bar(summary_region["Region"], summary_region["Sales"], color="orange")
plt.title("Total Sales by Region")
plt.xlabel("Region")
plt.ylabel("Sales ($)")
plt.tight_layout()
plt.savefig(os.path.join("output", "sales_by_region.png"))
plt.close()

# 🔹 Daily Sales Trend
plt.figure(figsize=(8,5))
plt.plot(df["Date"], df["Sales"], marker="o", color="purple")
plt.title("Daily Sales Trend")
plt.xlabel("Date")
plt.ylabel("Sales ($)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(os.path.join("output", "sales_trend.png"))
plt.close()

print("✅ Charts created successfully! Check the 'output' folder.")
