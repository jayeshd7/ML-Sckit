# -*- coding: utf-8 -*-
"""
Created on Mon Apr 16 12:22:30 2018

@author: jdalal
"""

import numpy as np
import pandas as pd

my_dates_index = pd.date_range('20180101',periods=6)

sample_numpy_data = np.array(np.arange(24).reshape(6,4))
sample_numpy_data

sample_df = pd.DataFrame(sample_numpy_data,my_dates_index,columns=list('ABCD'))
sample_df

df_from_dictionary = pd.DataFrame({
        'float':1.0,
        'time':pd.Timestamp('20180825'),
        'series':pd.Series(1,index=list(range(4)),dtype='float32'),
        'array':np.array([3]*4, dtype='int32'),
        'categories':pd.Categorical(["test","train","taxes","tools"]),
        'dull':'boring data'
        
        })
df_from_dictionary
df_from_dictionary.dtypes

sample_df.tail(2)

sample_df.describe()
pd.set_option('display.precision',2)

sample_df.sort_index(axis=1,ascending = True)
sample_df.sort_values(by='B',ascending = False)

sample_df['C']
sample_df[1:4]
sample_df['2018-01-02 ','2018-01-05' ]
x = sample_df.loc[:,['A','B']]
Y = sample_df.loc['2018-01-01':'2018-01-03',['A','B']]
sample_df.loc['2018-01-03',['D','B']][0]*4

sample_numpy_data[3]
z = sample_df.iloc[3]
sample_df.iloc[1:3,2:4]
sample_df.iloc[[0,1,3],[0,2]]
sample_df.iloc[:,1:3]
sample_df[sample_df>=11]

sample_df_2 = sample_df.copy()
sample_df_2['Fruits'] = ['apple','orange','banana','watermelon','chiku','pinaple']

sample_df_2[sample_df_2['Fruits'].isin['banana',]]








