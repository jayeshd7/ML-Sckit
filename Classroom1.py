# -*- coding: utf-8 -*-
#classroom1 assigment
import pandas as pd

#import data s

x_panads = pd.get_dummies(dataset,columns =['country'],prefix = 'countr')
dataset = pd.read_csv('')
x = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 3].values

from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values = 'Nan',strategy="mean",axis = 0)
imputer = imputer.fit(x[:,1:3])
x[:,1:3] = imputer.transform(x[:,1:3])


#Encoding tegorial data
#Encoding the independeent variable

from sklearn.preprocessing import LabelEncoder,OneHotEncoder
labelencoder_x = LabelEncoder()
x[:,0] = labelencoder_x.fit_transform(x[:,0])
onehotencoder_x = OneHotEncoder()

labelencoder_y  = LabelEncoder()
y = labelencoder_y.fit_transform(y)




