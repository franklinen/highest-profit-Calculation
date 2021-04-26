#declare environment variables
#import os
#os.chdir(r'C:\Users\MAIN\Desktop\sada')
#os.getcwd()
#import libraries
import json
import pandas as pd

#import file
url = 'https://gist.githubusercontent.com/bobbae/b4eec5b5cb0263e7e3e63a6806d045f2/raw/279b794a834a62dc108fc843a72c94c49361b501/data.csv'
data = pd.read_csv(url)
# Total rows
print(data.shape[0])
#rename columns
data.columns = ['year', 'company', 'rank', 'revenue', 'profit']
# Convert to float, otherwise NaN
data['profit'] = pd.to_numeric(data['profit'], errors='coerce')
# Remove NaN
data = data[data['profit'].notnull()]
# Rows after removing NaN
print(data.shape[0])
# Sort by descending order of profit
data.sort_values(by=['profit'], ascending=False, inplace=True)
# Export top 20 to .json
data[:20].to_json('data2.json', orient='records')
#import the json file and print it
with open('data2.json') as f:
    data2 = json.load(f)
print(data2)




