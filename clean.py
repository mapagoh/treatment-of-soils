import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

pd.options.display.max_columns = None
pd.options.display.max_rows = None

data= pd.read_csv("Filtered_ST_data.csv")

data1=data.drop(['p_ex_1'], axis=1)
data1=data.drop(['p_ex_3'], axis=1)
data1=data.drop(['coarse_tot'], axis=1)
data1=data.drop(['wood_lit_c'], axis=1)
data1=data.drop(['litterfall_anpp'], axis=1)
data1=data.drop(['depth_water'], axis=1)

data.isnull()
data.bfill()
fig = plt.figure(figsize = (15,20))
ax = fig.gca()
data1.hist(ax = ax)

print(data1)