students = ["AMIT", "RIYA", "JOHN"]
subjects = ["Math", "Science", "English"]
marks_data = {
    "Math": [85, 92, 78],
    "Science": [89, 95, 82],
    "English": [78, 88, 85]
}

import numpy as np
import matplotlib.pyplot as plt

x = np.arrange(len(students))
y = 0.25

fig,ax = plt.subplots(figsize = (9,6))

#creating a Bar graph
b1 = ax.bar(x-y, marks_data["Math"], y , color='royalblue', label='Math')
b2 = ax.bar(x, marks_data["Science"], y , color='crimson', label='Science')
b3 = ax.bar(x+y, marks_data["English"], y , color='forestgreen', label='English')

ax.set_xticks(x)
ax.set_xticklabels(students, rotation=30)

# Adding labels and title
ax.set_xlabel('STUDENTS', weight = 'bold')
ax.set_ylabel('MARKS' , weight = 'bold')
ax.set_title('STUDENTS MARKS', weight = 'bold', fontsize = 14)
ax.set_ylim(0, 120)
ax.grid(axis = 'y', linestyle = "--", alpha = 0.7)
ax.set_axisbelow(True)
ax.legend(loc = "upper right", frameon = True, edgecolor = "#000000")

#printing the graph
plt.show()