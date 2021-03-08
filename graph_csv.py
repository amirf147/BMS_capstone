# import your desired plot setting by specifing class name to import from
# plot_settings module

import pandas as pd
import matplotlib.pyplot as plt
from plot_settings import discharge as setting

def csv_to_df(file_name, row_interval):
    '''file name should end with .csv and row interval determines nth rows to be
    used in final dataframe'''
    
    df = pd.read_csv(file_name)
    df = df.drop([' Data  ',' ADC     ',' StartCells',' OpenWire',
              ' Discharge',' StartAux   ',' StartStatus',' BRD#01 ADDR ',
              ' CELL07',' CELL08',' CELL09',' CELL10',' CELL11',' CELL12',
              ' GPIO1',' GPIO2',' GPIO3',' GPIO4',' GPIO5',' VREF2',' VREGA ',
              ' VREGD ', ' ITMP  '], axis = 1)
    df = df.rename(columns = {'Elapsed Time   ': 'Elapsed Time',
                          ' CELL01': 'Cell 1', ' CELL02': 'Cell 2',
                          ' CELL03': 'Cell 3', ' CELL04': 'Cell 4',
                          ' CELL05': 'Cell 5', ' CELL06': 'Cell 6',
                          ' SOC   ': 'SoC'})

    df = df.iloc[1::row_interval] #only keep the first and every interval after
    df = df.reset_index()
    df = df.drop(['index'], axis = 1)
    return df

def add_time_column(data_frame, hms):
    '''call with dataframe object and specify if want time in hours minutes or
    seconds by passing 'h', 'm' or 's' to hms parameter'''

    times_list = [] #holder for the conversion of elapsed time to time in hours
    A, B, C = 0, 0, 0 #Time conversion coefficients
    
    if hms == 'h':
        A, B, C = 1, 1 / 60, 1 / 3600
    elif hms == 'm':
        A, B, C = 60 , 1, 1 / 60
    elif hms == 's':
        A, B, C = 3600, 60, 1
    else:
        return 'Error: hms should be string "h" or "m" or "s"'
    
    for row_number in range(len(df)):
        times_list.append(df.loc[row_number, 'Elapsed Time'])
        hours = int(times_list[row_number][3])
        minutes = int(times_list[row_number][5:7])
        seconds = int(times_list[row_number][8:10])
        times_list[row_number] = (hours * A) + (minutes * B) + (seconds * C)

    hours_column = pd.Series(times_list)
    df.insert(loc = 0, column = 'Time (hours)', value = hours_column)
    return df

# Edit the following function calls to set your desired data set and options
df = csv_to_df('discharge_2cells_clean.csv', 400)
df = add_time_column(df, 'h')

# Apply plot setting and show plot
setting.set_options(df)
plt.show()
