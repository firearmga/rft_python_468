data = [10,None,20,10,"",30,None,40]

# Remove duplicates
unique = []
seen = set()

for item in data:
    if item not in seen:
        seen.add(item)
        unique.append(item)

print(unique) #removing duplicates

cleaned = [x for x in unique if x not in (None, "")] #removing invalid values

print(cleaned)  # returning cleaned list

print(len(data)-len(cleaned)) #counts the values removes

cleaned.sort()
print(cleaned) #returns sorted list

