# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 10:20:04 2018

@author: jdalal
"""
import pandas as pd
import numpy as np
my_simple_series =pd.Series(np.random.rand(5),index=['a','b','c','d','e'])
my_simple_series['b']
my_simple_series[:3]
my_dictionary = {'a':45,'b':-19.5,'c':4444}
my_second_series = pd.Series(my_dictionary)
pd.Series(my_dictionary,index=['b','e','d','a'])
my_second_series.get('a')
