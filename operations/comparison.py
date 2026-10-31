import numpy as np
import pandas as pd

df = pd.read_csv('train.csv')
#print(df.head(10))

#print(df['GrLivArea'][0:10])
#print(np.array(df['GrLivArea'][0:10]))

# Element-wise addition of two arrays

area_above_ground = np.array(df['GrLivArea'][0:10])
basement_area = np.array(df['TotalBsmtSF'][0:10])

greater_than = area_above_ground > basement_area
print(greater_than)

less_than = area_above_ground < basement_area
print(less_than)

equal_to = area_above_ground == basement_area
print(equal_to)