# -*- coding: utf-8 -*-
"""preprocessing

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1FYnG4mEqOQ02kvSzNbiWCBrNC9F4W1yc
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv('obesitas.csv')
dataset = pd.read_csv('obesitas.csv', sep =';')
x = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values

print(x)
print(y)

from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values=np.nan, strategy="median")
imputer.fit(x[:, 1:2])
x[:, 1:2] = imputer.transform(x[:, 1:2])

print(x)

from sklearn.impute import SimpleImputer
imputer= SimpleImputer(missing_values=np.nan, strategy="most_frequent")
imputer.fit(x[:, 2:4])

x[:, 2:4] = imputer.transform(x[:, 2:4])

print(x)

from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values=np.nan, strategy="most_frequent")
imputer.fit(x[:, 4:7])

x[:, 4:7] = imputer.transform(x[:, 4:7])

print(x)

import numpy as np
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder

x = [
    ['Adit', 21.0, 'Jarang', 'Sering', 'Tidak', 'Ya', 'Tidak'],
    ['Budi', 28.0, 'Jarang', 'Sedang', 'Ya', 'Tidak', 'Ya'],
    ['Cindy', 34.0, 'Jarang', 'Sering', 'Tidak', 'Ya', 'Ya'],
    ['Dika', 20.0, 'Sering', 'Sering', 'Ya', 'Tidak', 'Ya'],
    ['Eka', 28.0, 'Sedang', 'Sedang', 'Tidak', 'Ya', 'Tidak'],
    ['Farah', 32.0, 'Sering', 'Jarang', 'Tidak', 'Tidak', 'Ya'],
    ['Gita', 35.0, 'Jarang', 'Sering', 'Tidak', 'Ya', 'Tidak'],
    ['Hadi', 17.0, 'Sedang', 'Sedang', 'Ya', 'Ya', 'Ya'],
    ['Irwan', 24.0, 'Sering', 'Sering', 'Ya', 'Tidak', 'Ya'],
    ['Joko', 37.0, 'Jarang', 'Sering', 'Tidak', 'Ya', 'Tidak']
]

ct = ColumnTransformer(
    transformers=[
        ('encoder', OneHotEncoder(), [2, 3, 4, 5, 6])
    ],
    remainder='passthrough'
)

x = np.array(ct.fit_transform(x))

print(x)

from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
y = le.fit_transform(y)

print(y)

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=1)

print(x_train)

print(x_test)

print(y_train)

print(y_test)