# importing libraries
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
sns.set_theme(style='darkgrid')

# initializing data frame
data = pd.read_excel('2018data.xlsx', sheet_name=['Data'])
print(data)
data2 = pd.read_excel('college2021data.xlsx', sheet_name=['Data'])
print(data2)
data3 = pd.read_excel('2018data2.xlsx', sheet_name=['Data'])
print(data3)

'''
data_chart = sns.histplot(data=data, x='Age', hue=[
                          'yes', 'no'], multiple='stack')
print(data_chart)
'''
