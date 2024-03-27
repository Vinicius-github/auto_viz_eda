#Load packages
from autoviz.AutoViz_Class import AutoViz_Class
import pandas as pd
%matplotlib inline


#Load dataset
url ="https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
dataset = pd.read_csv(url)

AV = AutoViz_Class()
target = 'Survived'
dft = AV.AutoViz(filename='',
                 sep=',',
                 depVar=target,
                 dfte=dataset,
                 header=0,
                 verbose=1)