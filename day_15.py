import pandas as pd
import matplotlib.pyplot as plt

# 1. Create a sample dataset
# (Monthly trend, Category comparisons, and Ages for distribution)
data = {
    'Months': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
    'Revenue': [1200, 1350, 1100, 1600, 1650, 2100],
    
    'Categories': ['Electronics', 'Apparel', 'Home', 'Beauty'],
    'Category_Sales': [4500, 2200, 3100, 1800],
    
    # 50 normal ages (18-60), plus two extreme outliers (95 and 99)
    'Customer_Ages': [
        25, 34, 28, 45, 52, 23, 31, 38, 41, 29, 22, 55, 48, 33, 27, 36, 40, 50, 26, 32,
        21, 58, 44, 30, 24, 37, 42, 49, 53, 28, 35, 39, 46, 51, 20, 59, 43, 31, 25, 38,
        95, 99  # <-- OUTLIERS
    ]
}

# --- BONUS: USE SUBPLOTS ---
# Create a dashboard layout: 1 row, 3 columns
fig, axes = plt.subplots(1, 3, figsize=(15, 5))
fig.suptitle("Mini EDA Dashboard: Sales & Customer Insights", fontsize=16, fontweight='bold')

# --- TASK 1: LINE CHART (TREND) ---
axes[0].plot(data['Months'], data['Revenue'], marker='o', color='steelblue', linewidth=2)
axes[0].set_title("Revenue Trend (H1)")
axes[0].set_ylabel("Revenue ($)")
axes[0].grid(True, linestyle='--', alpha=0.5)

# --- TASK 2: BAR CHART (COMPARISON) ---
axes[1].bar(data['Categories'], data['Category_Sales'], color='darkorange')
axes[1].set_title("Sales Comparison by Category")
axes[1].set_ylabel("Total Sales ($)")

# --- TASK 3: HISTOGRAM (DISTRIBUTION) & BONUS: DETECT OUTLIERS ---
axes[2].hist(data['Customer_Ages'], bins=15, color='seagreen', edgecolor='black')
axes[2].set_title("Customer Age Distribution")
axes[2].set_xlabel("Age")
axes[2].set_ylabel("Frequency")

# Visually highlighting the outliers in the histogram
axes[2].annotate('Outliers Detected\n(Ages 90+)', xy=(95, 1), xytext=(70, 3),
            arrowprops=dict(facecolor='red', arrowstyle='->', lw=2), color='red')

# Adjust layout to prevent overlapping text
plt.tight_layout()
plt.show()