import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder
import scipy.stats as stats
data=pd.read_csv('C:\\Users\\User\\source\\repos\\MyDataScient\\possum.csv')
print(data.isnull().values.any())
data=data.dropna()