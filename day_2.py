# DAY 2 (STUDENT SCORE ANALYZER)


marks = [78,85,67,85,92,78]

#average
avg = sum(marks)/len(marks)
print(avg)

#highest
print(max(marks))

#lowest
print(min(marks))

#counting how many students scored above average
count = 0
for i in marks:
    if i>avg:
        count+=1 
print(count)

# grade distribution
grade_distribution = {"A":0, "B":0, "C":0, "F":0}

for mark in marks:
    if 90 <= mark <= 100:
        grade_distribution["A"] += 1
    elif 80 <= mark <= 89:
        grade_distribution["B"] += 1
    elif 70 <= mark <= 79:
        grade_distribution["C"] += 1
    else:
        grade_distribution["F"] += 1

print("Grade Distribution:")
for grade, count in grade_distribution.items():
    print(f"{grade}: {count}")
