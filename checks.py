import numpy as np
import pandas as pd

df=pd.read_csv("schools_targetstudy.csv")
print((df['Phone number']=="-1").sum())
