#Load packages
import sweetviz
import pandas as pd

#Load dataset
url ="https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
dataset = pd.read_csv(url)

# use analyze 
analyze_df = sweetviz.analyze([dataset, "df"], target_feat = 'Survived')
# then show 
analyze_df.show_html('analyze.html')