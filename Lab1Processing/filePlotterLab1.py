# You can use this file to plot the loged sensor data
# Note that you need to modify/adapt it to your own files
# Feel free to make any modifications/additions here

import sys
import os

# Get the parent directory and add it to the path to access utilities
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, parent_dir)

import matplotlib.pyplot as plt
from utilities import FileReader

def plot_errors(filename, title, xLabel, yLabel):
    
    headers, values=FileReader(filename).read_file() 
    time_list=[]
    first_stamp=values[0][-1]
    
    for val in values:
        time_list.append(val[-1] - first_stamp)

    for i in range(0, len(headers) - 1):
        plt.plot(time_list, [lin[i] for lin in values], label= headers[i]+ " linear")
    
    #plt.plot([lin[0] for lin in values], [lin[1] for lin in values])
    plt.legend()
    plt.grid()
    plt.title(title)
    plt.xlabel(xLabel)
    plt.ylabel(yLabel)
    plt.show()
    
import argparse

if __name__=="__main__":

    parser = argparse.ArgumentParser(description='Process some files.')
    parser.add_argument('--files', nargs='+', required=True, help='List of files to process')
    
    # Used to specify the title, xLabel, and yLabel for your plot
    parser.add_argument('--title', type=str, required=True, help='Title of the plot')
    parser.add_argument('--xLabel', type=str, required=True, help='X-axis label of the plot')
    parser.add_argument('--yLabel', type=str, required=True, help='Y-axis label of the plot')
    
    args = parser.parse_args()
    
    print("plotting the files", args.files)

    filenames=args.files
    title=args.title
    xLabel=args.xLabel
    yLabel=args.yLabel

    print(title)
    for filename in filenames:
        plot_errors(filename, title, xLabel, yLabel)
