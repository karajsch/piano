# Importing pandas
import pandas as pd

# Importing 2 files
#files = ["FileA.csv", "FileB.csv"]

data1 = pd.read_csv('FileA.csv')
data2 = pd.read_csv('FileB.csv')

# Using concat method to combine both files
file_c = pd.merge(data1, data2, 
    on='user_id', how='inner')
    
#([pd.read_csv(f) for f in files])

# This will export the new file as a CSV
file_c.to_csv("FileC.csv", index=False, encoding='utf-8-sig')
data = pd.read_csv("FileC.csv")
print(data)
