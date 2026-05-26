import pandas as pd

data = pd.read_csv("data_day_7.csv")

# average marks per student
data["average_marks_per_student"] = (data["math"]+data["science"]+data["english"])/3

print(data["average_marks_per_student"])

# finding topper
topper = data.loc[data["average_marks_per_student"].idxmax()]
print(topper)

#counting students above average
class_average = data["average_marks_per_student"].mean()
print(data.loc[data["average_marks_per_student"]>class_average])

# adding grade column
def assign_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 75:
        return "B"
    elif avg >= 60:
        return "C"
    else:
        return "D"

data["grade"] = data["average_marks_per_student"].apply(assign_grade)

print("\nData With Grades:")
print(data)


# subject average
subject_average_math = data["math"].mean()
subject_average_science = data["science"].mean()
subject_average_english = data["english"].mean()
print(subject_average_math,subject_average_science,subject_average_english)