import pandas as pd

df = pd.read_csv("data_day_8.csv")
print(df)

# average salary per department

avg_salary = df.groupby('dept')['salary'].mean()

#highest paid employee per department
highest_paid_emp = df.groupby("dept")["salary"].idxmax()

#emloyees in each dept
emp_count = df.groupby("dept")["name"].count()

#sort dept by avg salary in descending order
avg_dept =n= avg_salary.sort_values(ascending=False)

print(df)
print("\n" , avg_salary)
print("\n" , "Highest paid employee per department:","\n" , df["name"].loc[highest_paid_emp])
print("\n" , "Employee count per department:","\n" , emp_count)
print("\n" , "Average salary per department (sorted):","\n" , avg_dept)