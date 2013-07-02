import pandas as pd
import os
import matplotlib.pyplot as plt
import datetime as dt
import numpy as np
from scipy import interpolate
from mpl_toolkits.basemap import Basemap, cm

import mesonet_calculations

''' Quick code for using the existing scripts to create a single 
surface plot from mesonet data
'''

# Note that the start time should be divisible by 5 minutes
starttime = dt.datetime(2012, 6, 15, 0)
endtime   = starttime + dt.timedelta(minutes=5)
time_selection = starttime

filename  = 'locations.txt'
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

to_plot = '2 m Temperature'
z_max   = np.max(met[to_plot])                                                                    
z_min   = np.min(met[to_plot])                                                                    
levels  = np.arange(z_min, z_max+0.1, 0.1)


zi = interpolate.griddata((met.ix[time_selection]['Lon'], 
                           met.ix[time_selection]['Lat']), 
                           met.ix[time_selection][to_plot], 
                           (xi, yi), method='linear')
shapefile = 'UScounties/UScounties'
maps = Basemap(llcrnrlon=xmin, llcrnrlat=ymin, 
               urcrnrlon=xmax, urcrnrlat=ymax, projection='cyl')
maps.readshapefile(shapefile, name='counties')
maps.contourf(xi, yi, zi, levels, cmap = plt.cm.gist_earth_r)
c = plt.colorbar()  
c.set_label('2 m Temperature')  
maps.scatter(met.ix[time_selection]['Lon'], 
             met.ix[time_selection]['Lat'], marker='o', c='b', s=5)
maps.barbs(met.ix[time_selection]['Lon'], 
           met.ix[time_selection]['Lat'], 
           met.ix[time_selection]['u'].values, 
           met.ix[time_selection]['v'].values)
plt.title(to_plot)             
plt.tight_layout()
plt.show()