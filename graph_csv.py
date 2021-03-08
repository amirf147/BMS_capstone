# import your desired settings from the settings module
import pandas as pd
from settings import sixcells as sixc
from settings import discharge_data as dc_df

df = dc_df.clean() # initial set up of pandas dataframe

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

df = add_time_column(df, 'h')

# Apply plot setting and show plot
sixc.set_options(df, show_plot = True)

