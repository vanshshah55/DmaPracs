import numpy as np
import pandas as pd

file_path=r"D:\Vansh College\sampledata.xlsx"

df=pd.read_excel(file_path)


column_list=(list(df.columns[2:5]))
print(column_list)

for i in column_list:
  print(f"********************************************************************")
  print(f"***************",i,"************************************************")
  print(f"********************************************************************")
  data_column_name=i
  data=df[data_column_name]
  summary_statistics = data.describe()
  print(summary_statistics)
  print(f"mean = ",data.mean())
  print(f"median = ",data.median())
  print(f"mode = ",data.mode().iloc[0])
  print(f"standard deviaition = ",data.std())
  print(f"25 percentile = ",data.quantile(0.25))
  print(f"50 percentile = ",data.quantile(0.50))
  print(f"75 percentile = ",data.quantile(0.75))