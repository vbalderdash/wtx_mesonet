import pandas as pd
import os
import datetime as dt
import numpy as np

import mesonet_calculations
from plotting import sfc_plot

''' For reading in and creating surface plots of mesonet data in a given time 
interval saved in folders in the current working directory for each variable 
plotted 
'''

variables = {'temperature' : ('Degrees Celsius', '2 m Temperature'),
             'pressure': ('Millibars', 'Sea Level Pressure'),
             'dew_point': ('Degrees Celsius', 'Dewpoint'),
             'wind_speed': ('Meters per second', '10 m Scalar Wind Speed'),
             'gust_speed': ('Meters per second', '10 m Gust Wind Speed'),
             'rainfall': ('Inches', 'Rainfall'),
             }

# to_plot = 'temperature'
to_plot = np.array(['temperature', 'pressure', 'dew_point', 'wind_speed', 
                    'gust_speed', 'rainfall'])

# Note that the start time should be divisble by 5 minutes
starttime = dt.datetime(2012, 6, 15, 1, 0) 
endtime   = dt.datetime(2012, 6, 15, 2, 0) 

filename = 'locations.txt'
locations = pd.read_csv(filename, sep='	')

met = pd.DataFrame()
dir = os.listdir('raw_data')
for file in dir:
    if file[-4:] == '.txt': 
        met = pd.concat([met, 
            mesonet_calculations.meso_operations('raw_data/%s' %(file), 
            starttime,endtime,locations)], axis=0)

xmin = np.min(met['Lon'])
xmax = np.max(met['Lon'])
ymin = np.min(met['Lat'])
ymax = np.max(met['Lat'])
xi, yi = np.meshgrid(np.linspace(xmin, xmax, 200), 
                     np.linspace(ymin, ymax, 200))

sfc_plot(starttime, endtime, to_plot[0], variables[to_plot[0]], 
    locations, met, xi, yi, xmin, xmax, ymin, ymax)
sfc_plot(starttime, endtime, to_plot[1], variables[to_plot[1]], 
    locations, met, xi, yi, xmin, xmax, ymin, ymax)
sfc_plot(starttime, endtime, to_plot[2], variables[to_plot[2]], 
    locations, met, xi, yi, xmin, xmax, ymin, ymax)
sfc_plot(starttime, endtime, to_plot[3], variables[to_plot[3]], 
    locations, met, xi, yi, xmin, xmax, ymin, ymax)
sfc_plot(starttime, endtime, to_plot[4], variables[to_plot[4]], 
    locations, met, xi, yi, xmin, xmax, ymin, ymax)
sfc_plot(starttime, endtime, to_plot[5], variables[to_plot[5]], 
    locations, met, xi, yi, xmin, xmax, ymin, ymax)
