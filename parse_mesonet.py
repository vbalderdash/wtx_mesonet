import pandas as pd
import datetime as dt

from read_mesonet import MesoFile

class MesoArrays(object):
    '''For pulling out the meteorological, agricultural or Reese-only data
    from the raw mesonet data files, correctly index those arrays and 
    correct the station pressure measurement
    '''
    def __init__(self, filename):
        self.data = MesoFile(filename).read()
        self.year = MesoFile(filename).year

    def MetArray(self): # Just the meteorological data array
        meso2 = self.data
        groups = meso2.groupby(0)
        met = meso2.ix[groups.groups.get(1)]
        columns = ['Time', 'Array ID', 'Station ID', '10 m Scalar Wind Speed',
                   '10 m Vector Wind Speed', '10 m Wind Direction',
                   '10 m Wind Direction Std', '10 m Wind Speed Std', 
                   '10 m Gust Wind Speed', '1.5 m Temperature', 
                   '9 m Temperature', '2 m Temperature', 
                   '1.5 m Relative Humidity', 'Station Pressure', 'Rainfall', 
                   'Dewpoint', '2 m Wind Speed', 'Solar Radiation', 'foo'] 
        met.columns = columns[:len(met.columns)]
        met = met.set_index('Time')
        met['Station Pressure'] = met['Station Pressure']+600
        return met

    def AgrArray(self): # Just the agricultural data array
        agr2 = self.data
        groups = agr2.groupby(0)
        agr = agr2.ix[groups.groups.get(2)]
        agr = agr.dropna(axis=1, how='all')
        columns = ['Time', 'Array ID', 'Station ID', 
                   '5 cm Natural Soil Temperature', 
                   '10 cm Natural Soil Temperature', 
                   '20 cm Natural Soil Temperature', 
                   '5 cm Bare Soil Temperature', 
                   '20 cm Bare Soil Temperature', 
                   '5 cm Water Content', '20 cm Water Content', 
                   '60 cm Water Content', '75 cm Water Content', 
                   'Leaf Wetness', 'Battery Voltage', 'Program Signature']
        agr.columns = columns
        agr = agr.set_index('Time')
        return agr

    def ReeseArray(self): # Just the Reese-specific data array
        reese2 = self.data
        groups = reese2.groupby(0)
        reese = reese2.ix[groups.groups.get(3)]
        reese = reese.dropna(axis=1, how='all')
        year = self.year
        if year<2006: 
            reese.columns = ['Array ID', 'Time', 'Station ID', 
                             'Total Radiation', 
                             'SPLite Accumulated Radiation', 
                             'Licor Accumulated Radiation', 
                             'CM21 Accumulated Radiation', 
                             'CM3 Accumulated Radiation']
        if year>2008: 
            reese.columns = ['Time', 'Array ID', 'Station ID', 
                             '10 m Scalar Wind Speed 2', 
                             '10 m Vector Wind Speed 2', 
                             '10 m Wind Direction 2', 
                             '10 m Wind Direction Std 2', 
                             '10 m Wind Speed Std 2', 
                             '10 m Peak Wind Speed 2', 
                             '20 ft Wind Speed', '2 m Wind Speed 2']
        reese = reese.set_index('Time')
        return reese