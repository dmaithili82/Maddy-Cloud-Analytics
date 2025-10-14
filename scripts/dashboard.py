import pandas as pd
import matplotlib.pyplot as plt
import os

# Load the data
data_path = os.path.join("data", "Sample_sales.csv")
df = pd.read_csv(data_path)

# Summarize sales by product
summary = df.groupby("Product")["Sales"].sum().reset_index()

# Display summary in terminal
print("\n=== Sales Summary by Product ===")
print(summary)

# Plot the summary
plt.figure(figsize=(8, 5))
plt.bar(summary["Product"], summary["Sales"], color="skyblue")
plt.title("Total Sales by Product")
plt.xlabel("Product")
plt.ylabel("Sales ($)")
plt.tight_layout()

# Save output
output_path = os.path.join("output", "sales_chart.png")
plt.savefig(output_path)
print(f"\nChart saved to: {output_path}")
