logs = ["error disk full","info started","error file missing","warning memory low"]



counts = {
    "error": 0,
    "info": 0,
    "warning": 0
}

for log in logs:
    log_upper = log.upper()

    for log_type in counts:
        if log_type in log:
            counts[log_type] += 1

print(counts)

#most freuqent
most_frequent = max(counts, key=counts.get)
print(most_frequent)