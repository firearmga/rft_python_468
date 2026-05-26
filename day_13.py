import seaborn as sns
import matplotlib.pyplot as plt

# Load sample data
df = sns.load_dataset("tips")

fig , ax = plt.subplots(figsize=(10, 6))

# 1. Plot using Seaborn
sns.histplot(data=df, x="total_bill", kde = True, bins=20, color="skyblue", edgecolor="black")
ax.set_title("Distribution of Total Bill", fontsize=16, fontweight="bold", pad=15)

plt.show()

# 2. Calculate skewness using pure Pandas
print("Skewness value:", df["total_bill"].skew())