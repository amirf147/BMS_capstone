import sys
import pandas as pd
import matplotlib.pyplot as plt

if __name__ == "__main__":
    print("I prefer to be a module.")
    sys.exit()

class Csv:

    rawfiles_path = 'datalogs\\raw\\'
    cleanfiles_path = 'datalogs\\cleaned\\'
    column_names = []
    
    def __init__(self, file_name):
        self.file_name = file_name

    def to_lines(self):

        a_file = open(self.rawfiles_path + self.file_name, "r")
        lines = a_file.readlines()
        a_file.close()
        self.column_names = lines[4] # holds the column names of the table
        lines = lines[6:-4] # remove first 6 and last 4 lines w/ no data
        return lines

    def to_chars(self, lines):
        # Create a list of lists of each character
        divided_lines = [] # holder for list of lists 
        char_list = [] # used to temporarily hold chars in each line
        
        for line_num in range(len(lines)):
            for char in lines[line_num]:   
                char_list.append(char)
    
            divided_lines.append(char_list)
            char_list = []
        return divided_lines

    def fix_decimals(self, divided_lines):
        # Change X,XXXX to X.XXXX in data
        comma_count = 0 # num of commas tracker
        for line in range(len(divided_lines)):
            for char in range(len(divided_lines[line])):
                if divided_lines[line][char] == ',':
                    comma_count += 1
                    if ((comma_count >= 10) and (comma_count % 2 == 0)):
            #this if statement is to do with the fact that the first decimal
            #point comes from the 10th occurence of a comma in the line and
            #then every other instance thereafter until the end of the line
                        divided_lines[line][char] = '.'
                
            comma_count = 0
        # Recreate the list of lines
        line = ''
        lines = []
        for line_num in range(len(divided_lines)):
            for char in range(len(divided_lines[line_num])):
                line += divided_lines[line_num][char]
            lines.append(line)
            line = ''
        return lines

    def write_to_file(self, lines, new_file_suffix = '_clean.csv'):
        f = open(self.cleanfiles_path + self.file_name[:-4] + new_file_suffix,
                 'w+')
        f.write(self.column_names) # add the column names to the first line
        for line in lines:
            f.write(line)
        f.close()
            
class Dataframe:

    def __init__(self, file_name, row_interval = 1):
        self.file_name = 'datalogs\\cleaned\\' + file_name
        self.row_interval = row_interval

    def clean(self):
        df = pd.read_csv(self.file_name)
        df = df.rename(columns = {'Elapsed Time   ': 'Elapsed Time',
                          ' CELL01': 'Cell 1', ' CELL02': 'Cell 2',
                          ' CELL03': 'Cell 3', ' CELL04': 'Cell 4',
                          ' CELL05': 'Cell 5', ' CELL06': 'Cell 6',
                          ' SOC   ': 'SoC'})
        df = df.iloc[1::self.row_interval] #only keep the first and every interval after
        df = df.reset_index()
        df = df.drop(['index'], axis = 1)
        return df
    
    def add_time_column(self, data_frame, hms):
        '''call with dataframe object and specify if want time in hours
        minutes or seconds by passing 'h', 'm' or 's' to hms parameter'''

        times_list = [] #holder for the conversion of elapsed time to time in hours
        A, B, C = 0, 0, 0 #Time conversion coefficients
    
        if hms == 'h':
            A, B, C = 1, 1 / 60, 1 / 3600
            column_title = 'Time (hours)'
        elif hms == 'm':
            A, B, C = 60 , 1, 1 / 60
            column_title = 'Time (minutes)'
        elif hms == 's':
            A, B, C = 3600, 60, 1
            column_title = 'Time (seconds)'
        else:
            return 'Error: hms should be string "h" or "m" or "s"'
    
        for row_number in range(len(data_frame)):
            times_list.append(data_frame.loc[row_number, 'Elapsed Time'])
            hours = int(times_list[row_number][3])
            minutes = int(times_list[row_number][5:7])
            seconds = int(times_list[row_number][8:10])
            times_list[row_number] = (hours * A) + (minutes * B) + (seconds * C)

        hours_column = pd.Series(times_list)
        data_frame.insert(loc = 0, column = column_title, value = hours_column)

class Plot:

    def __init__(self, title, x_values, y_values):
        self.title = title
        self.x_values = x_values
        self.y_values = y_values

    def set_options(self, df, nx = 20, ny = 20, show_plot = False):
        df.plot(x = self.x_values, y = self.y_values)
        plt.title(self.title)
        plt.ylabel('Voltage (V)')
        ax = plt.axes()
        ax.xaxis.set_major_locator(plt.MaxNLocator(nx))
        ax.yaxis.set_major_locator(plt.MaxNLocator(ny))
        plt.minorticks_on()
        plt.grid(axis = 'both', which='both', color = 'gainsboro',
                 linestyle = '-', linewidth = 0.7)
        if show_plot:
            plt.show()
