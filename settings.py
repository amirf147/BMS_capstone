import pandas as pd
import matplotlib.pyplot as plt

if __name__ == "__main__":
    print("I prefer to be a module.")

class Csv:

    path = 'datalogs\\raw\\'
    column_names = []
    
    def __init__(self, file_name):
        self.file_name = file_name

    def to_lines(self):
        a_file = open(self.path + self.file_name, "r")
        lines = a_file.readlines()
        a_file.close()
        self.column_names = lines[4] # holds the column names of the table
        lines = lines[6:-4] # remove first six lines and last 4 lines w/ no data
        return lines
    
class Dataframe:

    def __init__(self, file_name, row_interval):
        self.file_name = 'datalogs\\cleaned\\' + file_name
        self.row_interval = row_interval

    def clean(self):
        df = pd.read_csv(self.file_name)
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
        df = df.iloc[1::self.row_interval] #only keep the first and every interval after
        df = df.reset_index()
        df = df.drop(['index'], axis = 1)
        return df
    
class Plot:

    def __init__(self, title, x_values, y_values):
        self.title = title
        self.x_values = x_values
        self.y_values = y_values

    def set_options(self, df, n = 10, show_plot = False):
        df.plot(x = self.x_values, y = self.y_values)
        plt.title(self.title)
        plt.ylabel('Voltage (V)')
        ax = plt.axes()
        ax.xaxis.set_major_locator(plt.MaxNLocator(n))
        plt.minorticks_on()
        #plt.grid(color = 'black', linestyle = '-.', linewidth = 0.7)
        if show_plot:
            plt.show()

test_csv = Csv('test_data.csv')

discharge_data = Dataframe('discharge_2cells_clean.csv', 400)

sixcells = Plot('Cell Voltages: Discharge on Cell 3 & Cell 5',
                 'Time (hours)', ['Cell 1', 'Cell 2', 'Cell 3',
                                  'Cell 4', 'Cell 5', 'Cell 6'])

