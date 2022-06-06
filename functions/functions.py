
import openpyxl
import pandas as pd
from datetime import datetime

# Import CSV file
def csv_upload(path,index=False,dtype=None,encoding=None):
    '''import csv file and drop all empty rows'''
    df = pd.read_csv(path, index_col = index, dtype=dtype, encoding=encoding)
    df = pd.DataFrame(df).dropna(how='all')
    df = df.dropna(how='all', axis=1)
    print('Upload Successful: {} {} rows & {} columns'.format(path,df.shape[0],df.shape[1]))
    return df


# Import from xsl file
def xls_upload(path,sheet=0,index=False,dtype=None,usecols=None):
    '''import excel file and drop all empty rows'''
    df = pd.read_excel (path, sheet_name = sheet, index_col=index, dtype=dtype,usecols=usecols)
    df = pd.DataFrame(df).dropna(how='all')
    if sheet==0:
        print('Upload Successful: {} {} rows & {} columns'.format(path,df.shape[0],df.shape[1]))
    else:
        print('Upload Successful: '+sheet+' {} rows & {} columns'.format(df.shape[0],df.shape[1]))
    return df


# write to log file
def log(text):
    with open('RunLog.txt','a+') as file:
        file.write(str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))+": "+text+'\n')
        
        
# append a row to excel workbook saved in outputs root
def append(path,filename,row,sheetName='Sheet1'):
    file = '{path}\{filename}'.format(path=path,filename=filename)
    wb = openpyxl.load_workbook(file)
    sheet = wb[sheetName]
    new_row = row
    sheet.append(new_row.tolist())
    wb.save(file)
    

# convert seconds to larger time periods
def expand_seconds(seconds):
    '''converts number of seconds entered into days, hour & minutes'''
    
    SecsInMinute = 60
    SecsInHour = 60*60
    SecsInDay = 60*60*24

        
    days = seconds / SecsInDay
    d = days
    d_int = int(d)

    
    hours = seconds / SecsInHour
    h = hours - d_int * 24
    h_int = int(h)

    
    minutes = seconds / SecsInMinute
    m = minutes - (d_int * 24 * 60) - (h_int * 60) 
    m_int = int(m)
    
    
    s = seconds - (d_int * SecsInDay) - (h_int * SecsInHour) - (m_int * SecsInMinute)
    
    
    dbool = d_int >= 1
    hbool = h_int >= 1 
    mbool = m_int >= 1
    sbool = s > 0
    
    print('{}d {}h {}m {}s'.format(d_int, h_int, m_int, s))
    result = '{} days '.format(d_int)*dbool + '{} hours '.format(h_int)*hbool + '{} minutes '.format(m_int)*mbool + '{} seconds '.format(s)*sbool
    return result
