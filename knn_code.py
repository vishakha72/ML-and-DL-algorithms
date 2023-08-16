import numpy as np
import pandas as pd
import math

from google.colab import drive
drive.mount('/content/drive')

df = pd.read_csv('/content/drive/MyDrive/colab/Data.csv')

df['Salary'].fillna(int(df['Salary'].mean()), inplace = True)
print(df)

df['Age'].fillna(int(df['Age'].mean()), inplace = True)
print(df)

df.describe()

xq= df.sample()
xq_final = pd.DataFrame(xq[['Age','Salary']])
xq_final


def cal_distance(x):
  a = x.to_numpy()
  b = xq_final.to_numpy()
  distance = math.sqrt(sum([(a-b) ** 2 for a, b in zip(a,b[0])] ))
  return distance
  
  df['distance'] = df[['Age','Salary']].apply(cal_distance, axis = 1)
  
  df_sort = df.sort_values('distance', ascending = True)
  
  df_after = df_sort.head(3)
  
  df_after.reset_index()
  
  df_after.iloc[0]
  
  count = [0 for i in range(0,len(df['Purchased'].unique()))]
for xi in range(0, len(df_after)):
  if df_after.iloc[xi]['Purchased'] == 'No':
    count[0] = count[0] + 1
  elif df_after.iloc[xi]['Purchased'] == 'Yes':
    count[1] = count[1] + 1
    
 def max_num_in_list_label(list):
    maxpos = list.index(max(list)) +1
 
 if max_num_in_list_label(count) in df:
  print("Success")
else:
  print("not success")
