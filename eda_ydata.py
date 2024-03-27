#%%
#Load packages
from ydata_profiling import ProfileReport
import pandas as pd

#Load dataset
url ="https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
dataset = pd.read_csv(url)

# use ProfileReport
pr_df = ProfileReport(dataset)
# show pr_df
pr_df
# %%
