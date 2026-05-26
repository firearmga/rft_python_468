dataset = {
    "DATES" : ["MON","TUE","WED","THU","FRI"],
    "SALES" : [200,250,300,280,350]
}

import matplotlib.pyplot as plt
import pandas as pd

df = pd.DataFrame(dataset)

#creating the line graph plot 
ax = df.plot(x="DATES", y="SALES", kind="line", marker="o", color="royalblue", linewidth=2, figsize=(8, 5))
#finding the highest and lowest sales values and their corresponding indices
hi_idx, hi_val = df["SALES"].idxmax(), df["SALES"].max()
lo_idx, lo_val = df["SALES"].idxmin(), df["SALES"].min()

#highlighting the highest and lowest sales points
ax.scatter(hi_idx, hi_val, color="crimson", s=100, label="Highest Sales", zorder = 5)
ax.scatter(lo_idx, lo_val, color="forestgreen", s=100, label="Lowest Sales", zorder = 5)

#annotating the highest and lowest points with text labels
ax.annotate(f"HIGHEST", (hi_idx, hi_val), textcoords="offset points", xytext=(0,10), ha='center', color="crimson", weight ="bold")
ax.annotate(f"LOWEST", (lo_idx, lo_val), textcoords="offset points", xytext=(0,-15), ha='center', color="forestgreen", weight ="bold")

#customizing the plot with titles, labels, grid, and legend
plt.title("Sales Over the Week", fontweight="bold", fontsize=14)
plt.xlabel("Days")
plt.ylabel("Sales")
plt.ylim(150,400)
plt.grid(True, linestyle="--", alpha=0.5)
plt.xticks(rotation=45)
plt.legend()

#displaying the plot
plt.show()