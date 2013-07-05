The Python scripts are for ingesting converted West Texas Mesonet data into useable DataFram objects and for investigating
the data either through individual station meteorgrams or through basic surface
plotting.

## West Texas Mesonet
Current West Texas Mesonet data and more information can be found at 
www.mesonet.ttu.edu

## Data
The mesonet_sftp.py script can be used to get the raw data for a month from the 
West Texas Mesonet site after entering your username and password into the script
along with the month of interest. 

## Meteograms
The meso_meteogram.py script plots a single day and station's meteogram 
including soil temperature and moisture (if soil measurements were taken)
when run from the terminal as:
python meso_meteogram.py [4 letter station identifier] yymmdd

## Surface Plotting
For surface plotting there are two scripts:

*single_meso_surface.py is setup to create only one quick plot as 
specified in the file for trouble-shooting or plot manipulation.

*meso_surface.py is setup to create single-variable surface plots with wind 
barbs for a range of times at 5-minute intervals (the most common sampling
freqency of the stations) saved in varible-specific folders.  The plotted variable 
and time range are specified in the file.

## Configuration and Dependencies
The scripts assume that the mesonet data is stored in a 'raw_data/' folder in the
working directory in the original [Station]YYMM.txt file format.

These surface-plotting scripts also use a location.txt file in the working
directory downloaded from:
http://www.mesonet.ttu.edu/stationfile.htm

They are also currently setup to plot county boundaries which can be found in
mpl_toolkits/basemap/data in the basemap package or downloaded from an external
source.  The current configuration uses the county data in a local UScounties
directory.

### Original Data Formats 
#### Array 1 (the meteorological array) 
Array ID, Julian Day, Time (CST), Station ID, 
    10 m Scalar Wind Speed (m/s, 5 min (or 1 min) ave of 3 sec samples),
    10 m Vector Wind Speed (m/s), 
    10 m Wind Direction (degrees),
    10 m Wind Direction Std (degrees),
    10 m Wind Speed Std (m/s),
    10 m Gust Wind Speed (m/s),
    1.5 m Temperature (C),
    9 m Temperature (heat flux),
    2 m Temperature (heat flux),
    1.5 m Relative Humidity,
    Station Pressure (in mb minus 600 mb),
    Rainfall (in),
    Dewpoint (C), 
    2 m Wind Speed (m/s),
    Solar Radiation (W/m^2)

#### Array 2 (does not exist for all stations)
Array ID, Julian Day, Time (CST),
             Station ID,
             5 cm Natural Soil Temperature (C), 
             10 cm Natural Soil Temperature (C),
             20 cm Natural Soil Temperature (C),
             5 cm Bare Soil Temperature (C),
             20 cm Bare Soil Temperature (C),
             5 cm Water Content (considered %),
             20 cm Water Content (considered %),
             60 cm Water Content (considered %),
             75 cm Water Content (considered %),
             Leaf Wetness (%),
             Battery Voltage (V),
             Program Signature (random)

#### Old Reese Array (array 3 pre-2006) 
Array ID (pre-2006), Julian Day, Time (CST),
             Station ID,
             Total Radiation (W/m^2),
             SPLite Accumulated Radiation (W/m^2),
             Licor Accumulated Radiation (W/m^2),
             CM21 Accumulated Radiation (W/m^2),
             CM3 Accumulated Radiation (W/m^2)
             

#### New Reese Array (array 3 post-2009)
Array ID, Julian Day, Time (CST),
             Station ID,
             10 m Scalar Wind Speed 2 (m/s),
             10 m Vector Wind Speed 2 (m/s),
             10 m Wind Direction 2 (degrees),
             10 m Wind Direction Std 2 (degrees),
             10 m Wind Speed Std 2 (m/s),
             10 m Peak Wind Speed 2 (m/s),
             20 ft Wind Speed (m/s),
             2 m Wind Speed 2 (m/s)
