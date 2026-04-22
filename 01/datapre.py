import pandas as pd
import numpy as np
data = pd.DataFrame({
    'AREA': ['A', 'B', None, 'C'],
    'INT_SQFT': [100, 200, np.nan, 150],
    'DATE_SALE': ['2020', '2019', '2021', None]
})
print("BEFORE:\n", data, "\n")
data['AREA'] = data['AREA'].fillna('')
data['INT_SQFT'] = data['INT_SQFT'].fillna(data['INT_SQFT'].mean())
data = data.dropna(thresh=2)
data['AREA'] = data['AREA'].str.upper()
data = data.rename(columns={'DATE_SALE': 'SALE_DATE', 'INT_SQFT': 'SQFT_AREA'})
data = data.sort_values(by='SALE_DATE')
print("AFTER:\n", data)