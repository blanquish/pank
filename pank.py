#!/usr/bin/python -tt

"""A tiny program that parses a csv with bank
    transactions, classifies them and plots
    them in a pretty graph
"""

import sys
import os
import csv
import pandas as pd
import numpy as np

def parseCSV():
    """Will attempt to parse the file passed.
    Otherwise will display the correct usage for the program.
    """
    print 'Lets analyse some data!'
    
    if len(sys.argv) >= 3:
        csvFile = sys.argv[1]
        includesHeaders = sys.argv[2]   # should be true or false


        #for filename in os.listdir(INPUT_DIR):
        with open(csvFile, 'r') as infile:
            reader = csv.reader(infile)
            i = 1;
            for row in reader:
                if i > 0:
                    print 'Header ignored!'
                    i = 0;
                else:
                    print row

        return infile
    else:
     print 'Invoke me: pank.py [csvFile] [true|false]'

     return ''

def classifyRows(csvFile):

    #for row in reader:

    return 'nothing'


# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  csvFile = parseCSV()
  classifyRows(csvFile)
