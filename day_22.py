import numpy as np
import seaborn as sns
import pandas as pd

#dataset crafted with the  help of numpy
np.random.seed(42)
dates = pd.date_range(start="2026-01-01", periods=100, freq="D")
categories = ["Electronics", "Clothing", "Home & Kitchen", "Books"]
sex= ["Male", "Female"]

data = {
    "Date": np.random.choice(dates, size = 500),
    "CustomerID": range(1001, 1001 + 500),
    "Sex" : np.random.choice(sex, size = 500, p = [0.45, 0.55]),
    "Category": np.random.choice(categories, size=500, p=[0.4, 0.3, 0.2, 0.1]),
    "Transaction_Amount": np.random.normal(loc=800, scale=300, size=500)
}

df = pd.DataFrame(data)
# print(df.head(5))

#cleaning missing or duplicate values
df.drop_duplicates(inplace=True)
df.dropna(subset=["CustomerID"])
df["Transaction_Amount"] = df["Transaction_Amount"].fillna(0)

print(df.info())
print(df.isnull().count())

#calculating total sales and average revenue(ARPU)
t_sales = df["Transaction_Amount"].sum()
ARPU = t_sales/500

print(f"Total Sales : Rs{t_sales:,.2f}")
print(f"Avg Revenue per customer : Rs{ARPU:,.2f}")

#top 5 customers
top_5 = (df.groupby("CustomerID")["Transaction_Amount"].sum().nlargest(5))
print(top_5)


#visualization
import matplotlib.pyplot as plt

fig, axes = plt.subplots(2, 2, figsize=(20, 14))
fig.suptitle("Sales And Customer Insights Dashboard", fontweight='bold', fontsize = 24, color = "lavender", y =0.98)

#line chart(sales trend)
sales_trend = df.groupby("Date")["Transaction_Amount"].sum().sort_index()

axes[0, 0].plot(
    sales_trend.index,
    sales_trend.values,
    color="blue",
    linewidth=2
)

axes[0, 0].set_title("Daily Sales Trend")
axes[0, 0].set_xlabel("Date")
axes[0, 0].set_ylabel("Sales (Rs)")
axes[0, 0].tick_params(axis="x", rotation=45)

#Bar Chart(Top Products)
top_categories = (
    df.groupby("Category")["Transaction_Amount"]
    .sum()
    .sort_values(ascending=False)
)

axes[0, 1].bar(
    top_categories.index,
    top_categories.values,
    color="orange"
)

axes[0, 1].set_title("Top Categories by Sales")
axes[0, 1].set_xlabel("Category")
axes[0, 1].set_ylabel("Total Sales (Rs)")
axes[0, 1].tick_params(axis="x", rotation=45)

#pie chart 
# Pie Chart (Category Distribution Share)
category_share = df["Category"].value_counts()

axes[1, 0].pie(
    category_share.values,
    labels=category_share.index,
    autopct="%1.1f%%",
    startangle=90
)

axes[1, 0].set_title("Category Distribution Share")
plt.tight_layout()
plt.show()
