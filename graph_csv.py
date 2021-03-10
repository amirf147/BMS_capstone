# plots the data into figures, when one figure is closed the next one opens

from settings import Dataframe
from settings import Plot

# Remove excess datapoints and tidy up the dataframe, the first parameter is
# the file name and the second parameter is the nth number of lines to save
dc_df = Dataframe('discharge_2cells_clean.csv', 400)
cardf = Dataframe('5cell_fullspeed_clean.csv', 1)
burstdf = Dataframe('continuous_steering_busts_clean.csv', 1)

# initial set up of pandas dataframe + remove unwanted columns
df = dc_df.clean()
df2 = cardf.clean()
df3 = burstdf.clean()

# add column with time elapsed either hrs, min, or sec
dc_df.add_time_column(df, 'h')
cardf.add_time_column(df2, 's')
burstdf.add_time_column(df3, 's')

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
#Apply plot setting and show plot
graph_6cells.set_options(df, show_plot = True)
cardata_plot.set_options(df2, show_plot = True) 
burst_plot.set_options(df3, show_plot = True)
