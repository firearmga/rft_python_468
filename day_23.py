import numpy as np
import pandas as pd

n = 100
np.random.seed(42)

employee_id = np.arange(101, 101 + n)

names = np.array([
    "Aarav", "Priya", "Rahul", "Sneha", "Vikram",
    "Ananya", "Rohan", "Neha", "Arjun", "Kavya",
    "Aditya", "Pooja", "Karan", "Simran", "Manish"
])

employee_name = np.random.choice(names, n)
departments = np.array([
    "IT", "HR", "Finance", "Marketing", "Sales"
])

department = np.random.choice(departments, n)
performance_score = np.random.randint(50, 101, n)
attendance = np.random.randint(50, 101, n)

df = pd.DataFrame({
    "Employee_ID": employee_id,
    "Employee_Name": employee_name,
    "Department": department,
    "Performance_Score": performance_score,
    "Attendance_Percentage": attendance
})

# Save as CSV
# df.to_csv("employee_performance.csv", index=False)

#read CSV
#df = pd.read_csv("employee_performace.csv")
# print(df.head(10))

#department wise average performance
department_avg = df.groupby("Department")["Performance_Score"].mean()
print(department_avg)

#Top 10 performers
top_10_performers = df.sort_values(by="Performance_Score",ascending=False).head(10)
print(top_10_performers[["Employee_Name", "Performance_Score"]])

#employees with attendance below 75%
low_attendance = df[df["Attendance_Percentage"]<75]
print(low_attendance["Employee_Name"])


#charts and everything
import matplotlib.pyplot as plt

#Performance comparison chart
department_avg.plot(kind="bar")

plt.title("Department-wise Average Performance")
plt.xlabel("Department")
plt.ylabel("Average Performance Score")


#attendance trend
plt.figure(figsize=(10, 5))

plt.plot(
    df["Employee_ID"],
    df["Attendance_Percentage"],
    marker="o"
)

plt.axhline(
    y=75,
    color="red",
    linestyle="--",
    label="75% Minimum"
)

plt.title("Employee Attendance Trend")
plt.xlabel("Employee ID")
plt.ylabel("Attendance Percentage")

plt.legend()
# plt.tight_layout()
# plt.show()


#Department Distribution
department_count = df["Department"].value_counts()

print(department_count)
plt.figure(figsize=(7, 7))

plt.pie(
    department_count,
    labels=department_count.index,
    autopct="%1.1f%%"
)

plt.title("Department Distribution")

plt.show()







