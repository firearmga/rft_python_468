data = {
    "NAME" : ["A","B","C","D"],
    "AGE" : [24,31,28,37],
    "SALARY":[51000,42000,54000,48000]
}

import pandas as pd
df = pd.DataFrame(data,index = ["EMP1","EMP2","EMP3","EMP4"])
finetune = df[(df["AGE"]<30) | (df["SALARY"]>50000)]
print(finetune)

with open("DATA.csv","w") as file:
    file.write(str(finetune))