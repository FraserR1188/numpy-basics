import numpy as np
import pandas as pd

df = pd.read_csv('train.csv')
#print(df.head(10))

#print(df['GrLivArea'][0:10])
#print(np.array(df['GrLivArea'][0:10]))

# Element-wise addition of two arrays

area_above_ground = np.array(df['GrLivArea'][0:10])
basement_area = np.array(df['TotalBsmtSF'][0:10])
porach_area = np.array(df['OpenPorchSF'][0:10])
total_area = area_above_ground + basement_area + porach_area
print(total_area)
