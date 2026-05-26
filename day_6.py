import pandas as pd

data = pd.read_csv("data_day_6.csv")

data["total_sales"] = data["quantity"]*data["price"]

sales_per_product = data.groupby("product")["total_sales"].sum()
print(sales_per_product)

total_revenue = sum(data["total_sales"])
print("Total Revenue: ",total_revenue)

top_product = sales_per_product.idxmax() 
print("Top Selling Product: " ,top_product)

