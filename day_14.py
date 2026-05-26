dataset = {
    "CATEGORIES" : ["FOOD", "TRAVEL" , "SHOPPING"],
    "EXPENSES" : [500,300,200]
}



import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize = (9,6))

#plotting the pie chart
color = ["#ff9999","#66b3ff","#99ff99"]
bar1 = ax.pie(dataset["EXPENSES"], explode = [0.05,0,0],colors = color, labels = dataset["CATEGORIES"], autopct = "%1.1f%%", shadow = True, startangle = 90)

#setting the aspect ratio to be equal so that the pie chart is circular
ax.axis("equal")
ax.set_title("EXPENSES BY CATEGORY", fontsize = 14, fontweight = "bold")

#display the pie chart
plt.show()

