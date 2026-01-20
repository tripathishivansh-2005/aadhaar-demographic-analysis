import pandas as pd
import matplotlib.pyplot as plt
import os
# Folder path (current folder)
folder_path = "."
# Read and merge all CSV files
files = [f for f in os.listdir(folder_path) if f.endswith(".csv")]
df_list = []
for file in files:
    temp = pd.read_csv(file)
    df_list.append(temp)

df = pd.concat(df_list, ignore_index=True)

print(df.head())
print(df.shape)
df['date'] = pd.to_datetime(df['date'], errors='coerce')

# Remove rows with invalid dates
df = df.dropna(subset=['date'])
monthly = df.groupby(
    pd.Grouper(key='date', freq='M')
)[['demo_age_5_17', 'demo_age_17_']].sum()
heatmap_data = df.groupby([
    pd.Grouper(key='date', freq='M'),
    'state'
])[['demo_age_5_17', 'demo_age_17_']].sum()
