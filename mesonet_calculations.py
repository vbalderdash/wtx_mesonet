import pandas as pd
import datetime as dt
import numpy as np

from parse_mesonet import MesoArrays

def to_xy(dire, speed):
    ''' Calculates the u and v directions for wind barb plotting from 
    the direction and speed 
    '''
    u = np.zeros_like(dire)
    v = np.zeros_like(dire)
    u = -np.sin(dire * np.pi/180.) * speed
    v = -np.cos(dire * np.pi/180.) * speed
    return u, v

def meso_operations(filename, starttime, endtime, locations):
    ''' Combines the location information, u, v, and calculated sea level
    pressure into one array 
    '''
    met = MesoArrays(filename).MetArray()[starttime:endtime]
    tag = str(int(met.ix[starttime]['Station ID']))
    met['Lat'] = (np.ones(len(met.index)) * 
                 locations[locations['Logger ID'] == tag]
                 ['Lat-decimal'].values)
    met['Lon'] = (np.ones(len(met.index)) * 
                 locations[locations['Logger ID'] == tag]
                 ['Long.-decimal'].values)
    met['Ele'] = (np.ones(len(met.index)) * 
                 float(str(locations[locations['Logger ID'] == tag]
                 ['Elevation'].values[0])[:-3])*0.3048) # Elevation is in m
    met['u'], met['v'] = to_xy(met['10 m Wind Direction'], 
                               met['10 m Scalar Wind Speed'])
    met['Sea Level Pressure'] = (met['Station Pressure'] * 
             np.exp(met['Ele'] / ((met['2 m Temperature']+273.15)*29.263)))
    return met