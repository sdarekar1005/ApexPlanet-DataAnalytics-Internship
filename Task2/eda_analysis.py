import pandas as pd
import matplotlib.pyplot as plt

# Load Dataset
df = pd.read_csv("Superstore.csv", encoding="latin1")

print("Dataset Shape:", df.shape)

print("\nColumn Names:")
print(df.columns.tolist())

print("\nData Types:")
print(df.dtypes)

print("\nSummary Statistics:")
print(df.describe())

print("\nMissing Values:")
print(df.isnull().sum())

# Sales by Region
region_sales = df.groupby("Region")["Sales"].sum()

plt.figure(figsize=(8,5))
region_sales.plot(kind="bar")
plt.title("Sales by Region")
plt.ylabel("Sales")
plt.tight_layout()
plt.savefig("sales_by_region.png")
plt.close()
print("Sales by Region Chart Created")

# Sales by Category
category_sales = df.groupby("Category")["Sales"].sum()

plt.figure(figsize=(8,5))
category_sales.plot(kind="bar")
plt.title("Sales by Category")
plt.ylabel("Sales")
plt.tight_layout()
plt.savefig("sales_by_category.png")
plt.close()
print("Sales by Category Chart Created")

# Profit by Category
category_profit = df.groupby("Category")["Profit"].sum()

plt.figure(figsize=(8,5))
category_profit.plot(kind="bar")
plt.title("Profit by Category")
plt.ylabel("Profit")
plt.tight_layout()
plt.savefig("profit_by_category.png")
plt.close()
print("Profit by Category Chart Created")

# Top 10 Products by Sales
top_products = df.groupby("Product Name")["Sales"].sum().sort_values(ascending=False).head(10)

plt.figure(figsize=(10,6))
top_products.plot(kind="bar")
plt.title("Top 10 Products by Sales")
plt.ylabel("Sales")
plt.tight_layout()
plt.savefig("top10_products.png")
plt.close()
print("Top 10 Products Chart Created")

# Monthly Sales Trend

df["Order Date"] = pd.to_datetime(df["Order Date"])

monthly_sales = df.groupby(df["Order Date"].dt.to_period("M"))["Sales"].sum()

plt.figure(figsize=(12,6))
monthly_sales.plot()
plt.title("Monthly Sales Trend")
plt.ylabel("Sales")
plt.xlabel("Month")
plt.tight_layout()
plt.savefig("charts/monthly_sales_trend.png")
plt.close()
print("Monthly Sales Trend Chart Created")