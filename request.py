import requests
import pandas as pd
"""Setting the headers to send and accept json responses
"""
header = {'Content-Type': 'application/json', \
                  'Accept': 'application/json'}

"""Reading test batch
"""
df = pd.read_csv('TitanikData/titanic.csv', encoding="utf-8-sig")
df = df.head()

"""Converting Pandas Dataframe to json
"""
data = df.to_json(orient='records')

url = 'http://127.0.0.1:5000' # change to your url
r = requests.post(url,data)
print(r)

