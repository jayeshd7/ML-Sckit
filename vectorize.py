# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 17:14:40 2018

@author: jdalal
"""


import pandas as pd
import numpy as np

my_dictionary = {'a':45,'b':-19.5,'c':4444}
my_second_series = pd.Series(my_dictionary)
my_second_series
np.exp(my_second_series)
series  =  my_second_series[1:]+my_second_series[:-1]

def multiply_by_ten(inputelement):
    return inputelement * 10.0
my_second_series.map(multiply_by_ten)