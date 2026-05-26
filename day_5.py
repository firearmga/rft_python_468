import pandas as pd

#reading file
data = pd.read_csv('data.csv')
dict_data = data.to_dict()

print(data)

#store data as a list of dictionaries
print(dict_data)


#calcuilating average marks
print(sum(data["marks"]))
