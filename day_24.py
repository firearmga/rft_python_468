import kagglehub
import os
import pandas as pd

# Download latest version
path = kagglehub.dataset_download("valakhorasani/bank-transaction-dataset-for-fraud-detection")

files = os.listdir(path)

Trnx_data = [f for f in files if f.endswith('.csv')][0]
file_full_path = os.path.join(path, Trnx_data)

df = pd.read_csv(file_full_path)

df.to_csv("Trnx_data.csv", index = False)
#detect duplicate trnx
df.drop_duplicates(inplace = True)

#high value transaction, let us say the threshould is $500
query = df.query('TransactionAmount > 500')
print(" The Total Trnx above Threshould are : ", query["TransactionAmount"].count())
print(query["TransactionAmount"])

#suspecious acount with frequent transaction above 10 transactions
freq = df.groupby("AccountID")["TransactionID"].count().reset_index()
query_2 = freq.query("TransactionID > 10")
print("\n\nThe Total suspecious Trnx are : ", query_2['TransactionID'].count())
print(query_2)

import matplotlib.pyplot as plt
import seaborn as sns

# Visualization

fig , axes = plt.subplot_mosaic([['l_top', 'r_top'],
                                  ['bottom', 'bottom']],
                                  figsize = (18,12))
plt.suptitle("FRAUD DETECTION ANALYSIS", fontweight = "bold", fontsize = 24, y = 0.98, color = "royalblue")

#BAR GRAPH - TRANSACTION CATEGORY CHART
# category = df.groupby("TransactionType").value_counts().reset_index()
sns.countplot(data = df, x = "TransactionType" , ax = axes['l_top'], palette = "crest", hue = "TransactionType")
axes['l_top'].set_title("Transaction Category Chart")
axes['l_top'].grid(axis = 'y', alpha = 0.7, linestyle = "--")

#Line Chart - Daily Transaction Trend
df["TransactionDate"] = pd.to_datetime(df["TransactionDate"])
daily = df.groupby(df['TransactionDate'].dt.to_period('M'))['TransactionID'].count().reset_index(name='Count')
sns.lineplot(daily, marker = '*',  ax= axes['bottom'], linewidth = 5)
axes['bottom'].set_title("Daily Transaction Trend")
axes['bottom'].grid(True)

fig.delaxes(axes['r_top'])

#top 10 transactions

top_10 = df['TransactionAmount'].nlargest(10).reset_index()
print(top_10)

# as we have already created dictionary of suspecious transactions named query_2.
df2 = pd.DataFrame(query_2)

df2.to_csv("SuspeciousTransactions.csv", index = False)