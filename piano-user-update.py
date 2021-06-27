# Importing pandas
import pandas as pd
import requests

### Data Merge Section ###
# Importing client supplied CSV files
data1 = pd.read_csv('FileA.csv')
data2 = pd.read_csv('FileB.csv')

# Merge data on user_id
mergedData = pd.merge(data1, data2,
                      on='user_id', how='inner')

# Print merged data for testing
print(mergedData)
