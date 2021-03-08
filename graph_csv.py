import pandas as pd
from settings import Dataframe
from settings import Plot

# Remove excess datapoints and tidy up the dataframe, the first parameter is
# the file name and the second parameter is the nth number of lines to save
dc_df = Dataframe('discharge_2cells_clean.csv', 400)

df = dc_df.clean() # initial set up of pandas dataframe
dc_df.add_time_column(df, 'h') # add a column with hours elapsed

# Choose which columns to be graphed
graph_6cells = Plot('Cell Voltages: Discharge on Cell 3 & Cell 5',
                 'Time (hours)', ['Cell 1', 'Cell 2', 'Cell 3',
                                  'Cell 4', 'Cell 5', 'Cell 6'])

# Apply plot setting and show plot
graph_6cells.set_options(df, show_plot = True) 

