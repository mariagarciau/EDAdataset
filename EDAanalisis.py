import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("USA_Housing.csv")
data.head()

data.isnull().sum()
#data.info()
#data.describe()

data.hist()
data.hist("Area Population")