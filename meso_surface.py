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
             'theta_e': ('Kelvin', 'Theta_e'),
             'relative_humidity': ('%', '1.5 m Relative Humidity')
             }

shapefile = 'UScounties/UScounties'
locations_filename = 'locations.txt'
data_dir = 'raw_data'

# to_plot = 'temperature'
to_plot = np.array(['temperature', 'pressure', 'dew_point', 'wind_speed', 
                    'gust_speed', 'rainfall', 'theta_e', 'relative_humidity'])

# Note that the start time should be divisble by 5 minutes
starttime = dt.datetime(2012, 6, 4, 15, 0) 
endtime   = dt.datetime(2012, 6, 4, 15, 30) 

locations = pd.read_csv(locations_filename, sep='	')

met = pd.DataFrame()
dir = os.listdir(data_dir)
for file in dir:
    if file[-4:] == '.txt': 
        met = pd.concat([met, 
            mesonet_calculations.meso_operations('{0}/{1}'.format(data_dir,file), 
                                                  starttime,endtime,locations)], axis=0)

# xmin = np.min(met['Lon'])
# xmax = np.max(met['Lon'])
# ymin = np.min(met['Lat'])
# ymax = np.max(met['Lat'])

xmin = -103.3
xmax = -100.9
ymin = 33.0
ymax = 34.8

xi, yi = np.meshgrid(np.linspace(xmin, xmax, 200), 
                     np.linspace(ymin, ymax, 200))

for i in range(len(to_plot)):
    sfc_plot(starttime, endtime, to_plot[i], variables[to_plot[i]], 
        locations, met, xi, yi, xmin, xmax, ymin, ymax,shapefile)