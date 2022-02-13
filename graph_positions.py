# -*- coding: utf-8 -*-
"""
Created on Sat Feb 12 20:08:59 2022

@author: AlexBlack
"""

import plotly.express as px
import plotly.io as pio
pio.renderers.default='browser'

from functions.functions import xls_upload
from config.directories import rootDir


df = xls_upload('{}\output\{}'.format(rootDir,input('filename: ')))

fig = px.scatter_geo(df, lat='latitude', lon='longitude')
fig.show()
