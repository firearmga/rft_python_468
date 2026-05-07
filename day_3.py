# DAY 3 dictionary based phonebook

phonebook = {}

#adding contacts
phonebook["AMIT"] = "9876543210"
phonebook["RIYA"] = "9123456780"

print(phonebook)

#search contact
number =  phonebook.get("AMIT")
print(number)

#Delete contact
phonebook.pop("RIYA")
print(phonebook)

#PARTIAL NAME SEACRH
# IDK this for now

#To prevent duplicates
if "KRISH" not in phonebook:
    phonebook["KRISH"] = "XXXXXX8965"
else:
    print("Key already exists!")
