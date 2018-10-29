import pandas as pd
import os
import matplotlib.pyplot as plt
import datetime as dt
import numpy as np
from scipy import interpolate
from mpl_toolkits.basemap import Basemap, cm

def sfc_plot(starttime, endtime, variables, variablest, locations, 
             met, xi, yi, xmin, xmax, ymin, ymax,shapefile):
    ''' Script for plotting the mesonet data with wind barbs over a 
    county map in a given time interval 
    '''
    interval = int((endtime - starttime).total_seconds()/300)
    z_max = np.max(met[variablest[1]])                                                                  
    z_min = np.min(met[variablest[1]])                                                                  
    levels = np.arange(int(z_min)-1, int(z_max)+1, 1.)
    if not os.path.exists('%s' %(variables)):
        os.makedirs('%s' %(variables))
    for i in range(interval):
        time_selection = starttime + dt.timedelta(minutes=5*i)
        zi = interpolate.griddata((met.loc[time_selection]['Lon'], 
                                   met.loc[time_selection]['Lat']), 
                                   met.loc[time_selection][variablest[1]],
                                   (xi, yi), method='cubic')
        fig=plt.figure(figsize=(6.5,4))
        maps = Basemap(llcrnrlon=xmin, llcrnrlat=ymin, 
                       urcrnrlon=xmax, urcrnrlat=ymax, projection='cyl')
        maps.readshapefile(shapefile, name='counties')
        if (variables == 'dew_point'):
            maps.contourf(xi, yi, zi, np.arange(0.,21, 1), cmap=plt.cm.gist_earth_r)
        if (variables == 'relative_humidity'):
            maps.contourf(xi, yi, zi, np.arange(15.,75., 2.), cmap=plt.cm.gist_earth_r)
        if ((variables == 'temperature') or (variables== 'theta_e')):
            maps.contourf(xi, yi, zi, levels, cmap=plt.cm.jet)
        if variables == 'rainfall':
            maps.contourf(xi, yi, zi, levels, cmap=plt.cm.YlGn)
        if ((variables == 'pressure') or (variables == 'wind_speed') or 
            (variables == 'gust_speed')):
            maps.contourf(xi, yi, zi, levels, cmap=plt.cm.gist_earth)
        c = plt.colorbar()  
        # c.set_clim(20,38)
        c.set_label(variablest[0])  
        maps.scatter(met.loc[time_selection]['Lon'], 
                     met.loc[time_selection]['Lat'], latlon=True, marker='o', c='b', s=5)
        maps.barbs(met.loc[time_selection]['Lon'], 
                   met.loc[time_selection]['Lat'], 
                   met.loc[time_selection]['u'].values*1.94384, 
                   met.loc[time_selection]['v'].values*1.94384, latlon=True)
        # maps.drawparallels(np.arange(31.,36,1.), color='0.5',
        #     labels=[1,0,0,0], fontsize=10)
        # maps.drawmeridians(np.arange(-104.,-98.,1.), color='0.5',
        #     labels=[0,0,0,1], fontsize=10)
        # plt.title(variablest[1]) 
        filename = '{0}_{1}.png'.format(variables, 
                                  time_selection.strftime('%Y%m%d_%H%M'))
        plt.tight_layout()
        plt.savefig(variables + '/' + filename, dpi=250)
        plt.clf()
