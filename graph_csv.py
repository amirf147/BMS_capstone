# plots the data into figures, when one figure is closed the next one opens

from settings import Dataframe
from settings import Plot

# Remove excess datapoints and tidy up the dataframe, the first parameter is
# the file name and the second parameter is the nth number of lines to save
# default is 1 meaning all data points are saved
dc_df = Dataframe('discharge_2cells_clean.csv', 400)
cardf = Dataframe('5cell_fullspeed_clean.csv')
burstdf = Dataframe('continuous_steering_busts_clean.csv')
chargedf = Dataframe('charging_clean.csv')
data4x2_1df = Dataframe('4x2_fullspeed+steering_clean.csv')

# initial set up of pandas dataframe + remove unwanted columns
df = dc_df.clean()
df2 = cardf.clean()
df3 = burstdf.clean()
df4 = chargedf.clean()
df5 = data4x2_1df.clean()


# add column with time elapsed either hrs, min, or sec
dc_df.add_time_column(df, 'h')
cardf.add_time_column(df2, 's')
burstdf.add_time_column(df3, 's')
chargedf.add_time_column(df4, 'm')
data4x2_1df.add_time_column(df5, 'm')

# Choose which columns to be graphed

graph_6cells = Plot('Cell Voltages: Discharge on Cell 3 & Cell 5',
                    'Time (hours)', ['Cell 1', 'Cell 2', 'Cell 3',
                                     'Cell 4', 'Cell 5', 'Cell 6'])

cardata_plot = Plot('Cell Voltages: Car operating at full speed',
                    'Time (seconds)', ['Cell 2', 'Cell 3',
                                       'Cell 4', 'Cell 5', 'Cell 6'])

burst_plot = Plot('Cell Voltages: Bursts of continuous steering',
                  'Time (seconds)', ['Cell 2', 'Cell 3',
                                     'Cell 4', 'Cell 5', 'Cell 6'])

charge_plot = Plot('Cell Voltages: Charging',
                   'Time (minutes)', ['Cell 1', 'Cell 2', 'Cell 3',
                                      'Cell 4', 'Cell 5', 'Cell 6'])

data4x2_1_plot = Plot('Cell Voltages: Fullspeed+steering+stops run with 8 cells (4x2)',
                   'Time (minutes)', ['Cell 1', 'Cell 2', 'Cell 3',
                                      'Cell 4'])
#Apply plot setting and show plot
graph_6cells.set_options(df, show_plot = True)
cardata_plot.set_options(df2, show_plot = True) 
burst_plot.set_options(df3, show_plot = True)
charge_plot.set_options(df4, show_plot = True)
data4x2_1_plot.set_options(df5, show_plot = True)
