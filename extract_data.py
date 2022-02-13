# -*- coding: utf-8 -*-
"""
Created on Sat Feb 12 19:27:37 2022

@author: AlexBlack
"""

import pandas as pd

from config.directories import rootDir
from functions.functions import append

url = 'http://api.open-notify.org/iss-now.json'

df = pd.read_json(url)

df['latitude'] = df.loc['latitude','iss_position']
df['longitude'] = df.loc['longitude','iss_position']
df.reset_index(inplace=True)

df = df.drop(['iss_position','index','message'], axis=1).loc[0]

append(rootDir+'\output','ISS_positions.xlsx',df)
