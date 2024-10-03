import pandas as pd
import random

df = pd.read_csv(r'Sample-Superstore.csv') 

genders = ['Male', 'Female', 'Non-binary']
age_range = range(18, 70)

customer_info = {}

for customer in df['Customer Name'].unique():
    customer_info[customer] = {
        'Age': random.choice(age_range),
        'Gender': random.choice(genders)
    }

df['Age'] = df['Customer Name'].map(lambda name: customer_info[name]['Age'])
df['Gender'] = df['Customer Name'].map(lambda name: customer_info[name]['Gender'])

df.to_csv(r'Updated_Superstore.csv', index=False)

print(df.head())