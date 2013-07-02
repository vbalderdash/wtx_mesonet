import pandas as pd
import datetime as dt

class MesoFile(object):
    ''' For reading in a raw mesonet data file after 2000 and correctly 
    parse the date and time into a datetime object in the same array (in UTC) 
    which replaces the original columns 1-2
    '''
    def __init__(self, filename):
        self.year = int('20'+filename[-8:-6])
        self.filename = filename

    def parse(self, day, hrmin):
        # Converting from Julian Day with CST to standard datetime and UTC
        return (dt.datetime(self.year, 1, 1, int(hrmin)/100, int(hrmin)%100) 
              + dt.timedelta(int(day)-1) + dt.timedelta(hours=6))

    def read(self):
        meso2 = pd.read_csv(self.filename, sep=',', parse_dates=[[1,2]], 
            date_parser=self.parse, header=None)
        return meso2