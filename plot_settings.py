import pandas as pd
import matplotlib.pyplot as plt

if __name__ == "__main__":
    print("I prefer to be a module.")

class Plot:

    def __init__(self, title, x_values, y_values):
        self.title = title
        self.x_values = x_values
        self.y_values = y_values

    def set_options(self, df):
        df.plot(x = self.x_values, y = self.y_values)
        plt.title(self.title)
        plt.ylabel('Voltage (V)')
        ax = plt.axes()
        ax.xaxis.set_major_locator(plt.MaxNLocator(10))
        plt.minorticks_on()
        #plt.grid(color = 'black', linestyle = '-.', linewidth = 0.7)

# Create instance of Plot for the discharge data
discharge = Plot('Cell Voltages: Discharge on Cell 3 & Cell 5',
                 'Time (hours)', ['Cell 1', 'Cell 2', 'Cell 3',
                                  'Cell 4', 'Cell 5', 'Cell 6'])

