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

fig = px.line_geo(df, lat='latitude', lon='longitude') #try ,line = dict(width = 2, color = 'blue')
fig.update_geos(
    #projection_type="orthographic",
    #visible=False, resolution=110, #scope="asia",
    showcountries=True, countrycolor="Black",
    showsubunits=True, subunitcolor="Blue"
)
fig.show()
