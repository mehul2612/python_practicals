import seaborn as sns
from matplotlib import pyplot as plt
import pandas as pd
# print(sns.get_dataset_names())
df=sns.load_dataset('fmri')
print(df.head())
sns.lineplot(x='timepoint',y='signal',data='fmri')
print(sns.show())

