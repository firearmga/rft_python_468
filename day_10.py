logs = ["ERROR DISK FULL","INFO STARTED",'ERROR FILE MISSING','WARNING MEMORY LOW']

counts = {
    "ERROR": 0,
    "INFO": 0,
    "WARNING": 0
}

for log in logs:
    log_type = log.split()[0].upper() #splits the string, keeps the first word, converts it into uppercase

    for log_type in counts:
            counts[log_type] += 1

print("log counts",counts)

most_freq = max(counts,key=counts.get)

print("Most Frequent:", most_freq)