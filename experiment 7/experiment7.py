import pandas as pd
data = pd.read_csv('C:/Users/abhis/Documents/DTU ML_LAB/experiment 7/SummerSD.csv')
print(data.head())
data['Country'] = data['Country'].fillna("")
data['Year'] = data['Year'].fillna(method='bfill')
data = data.dropna()
data = data.dropna(axis=1, how='all')

data['City'] = data['City'].str.upper()


data = data.rename(columns={
    'City': 'Host Country',
    'Code': 'country_code'
})

print(data)
