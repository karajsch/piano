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


### API Request Section ###
my_headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'Accept': 'application/json'
}

my_params = {
    'aid': 'o1sRRZSLlw',
    'api_token': 'zziNT81wShznajW2BD5eLA4VCkmNJ88Guye7Sw4D'
}

response = requests.post(
    'https://sandbox.tinypass.com/api/v3/publisher/user/search', headers=my_headers, params=my_params)

# Print for testing
print(response.text)
