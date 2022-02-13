# -*- coding: utf-8 -*-
"""
Created on Sat Feb 12 20:36:15 2022

@author: AlexBlack
"""

import time
# import openpyxl
import pandas as pd
from datetime import datetime
from threading import Thread, Event
from functions.functions import log
from config.directories import rootDir


intervals = int(input('How frequently should data be collected (in seconds): '))
length = int(input('How long should data be collected for (in seconds): '))

log('Program started')

sheetname = str(datetime.now().strftime("%Y-%m-%d"))+" "+str(intervals)+"-"+str(length)

data = pd.DataFrame()
url = 'http://api.open-notify.org/iss-now.json'

stop = Event()

def read_api():
    while not stop.is_set():
        global data 
        df = pd.read_json(url)
        
        df['latitude'] = df.loc['latitude','iss_position']
        df['longitude'] = df.loc['longitude','iss_position']
        df.reset_index(inplace=True)
        df = df.drop(['iss_position','index','message'], axis=1).loc[:0]
        
        data = pd.concat([data,df])
        
        log('Successful data collection')
            
        time.sleep(intervals)

thread = Thread(target=read_api)

thread.start()
thread.join(timeout=length)
stop.set()

file = rootDir+'\output\{}.xlsx'.format(sheetname)
data.to_excel(file,index=False)

log('Program completed')


# wb = openpyxl.load_workbook(file)
# wb.create_sheet(sheetname)
# wb[sheetname].append(data.columns)
# wb.save(rootDir+'\output\test.xlsx')
