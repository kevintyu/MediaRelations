# CanDev Hackathon

import numpy as np
import pandas as pd
import os
import glob
import matplotlib.pyplot as plt

cwd = os.getcwd()
mediaRelationsFileName = glob.glob(cwd + '/*2019.xlsx')[0]

mediaRelationsDF = pd.read_excel(mediaRelationsFileName)

# print the dataframe to see whats inside ** WORKS **
# print(mediaRelationsDF)

mediaRelationsDF.head()

topicMediaRelations = pd.read_excel(mediaRelationsFileName, header=None, index_col=False)[10]
%matplotlib inline
topicMediaRelations.value_counts()[:].plot(x = 'topic', y = 'count',kind='bar')
newTopicMediaRelations = topicMediaRelations.reset_index()
newTopicMediaRelations.to_excel("output.xlsx")
