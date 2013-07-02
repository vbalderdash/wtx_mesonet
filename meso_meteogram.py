import datetime as dt
import matplotlib.pyplot as plt
from parse_mesonet import MesoArrays
import sys

'''For creating a one-day meteogram with temperature, dew point, 
wind speeds, wind direction, rainfall amounts, solar radiation, 
station pressure, soil temperature, soil moisture and leaf wetness 
for any on station primarily for data-checking purposes
'''

# To execute from the command line with python meso_meteogram.py XXXX YYMMDD 
# where XXXX is the station symbol and with the raw data files in a 
# raw_data directory from the working directory.
filename  = 'raw_data/' + sys.argv[1] + sys.argv[2][:4] + '.txt'
starttime = dt.datetime(int('20'+sys.argv[2][:2]), int(sys.argv[2][2:4]), 
            int(sys.argv[2][4:]))

# # Or to execute in more direct manner adjust the following:
# filename = '/home/vanna/Desktop/originals/CHIL1206.txt'
# starttime = dt.datetime(2012,6,15,0)

# To plot a longer time period, change the time delta value below
endtime   = starttime + dt.timedelta(hours=24)
met       = MesoArrays(filename).MetArray()[starttime:endtime]

# To plot all basic data if it exists or just the meteorological if 
# there is no soil data
try: 
    agr = MesoArrays(filename).AgrArray()[starttime:endtime]
    fig = plt.figure(1)
    ax1 = fig.add_subplot(611)
    ln1 = ax1.plot(met[starttime:endtime].index, 
                   met['10 m Scalar Wind Speed'][starttime:endtime], 
                   label='Average Wind Speed')
    ln2 = ax1.plot(met[starttime:endtime].index, 
                   met['10 m Gust Wind Speed'][starttime:endtime], 
                   label='Maximum Wind Speed')
    plt.ylabel('Wind Speed\nat 10 m (m/s)', multialignment='center')
    plt.setp(ax1.get_xticklabels(), visible=False)

    ax7 = ax1.twinx()
    ln3 = ax7.plot(met[starttime:endtime].index, 
                   met['10 m Wind Direction'][starttime:endtime], 
                   '.k', linewidth=0.5, label='Wind Direction')
    plt.ylabel('Wind\nDirection\n(degrees)', multialignment='center')
    plt.ylim(0,360)
    lns = ln1+ln2+ln3
    labs = [l.get_label() for l in lns]
    ax7.legend(lns, labs, prop={'size':8})

    ax2 = fig.add_subplot(612, sharex=ax1)
    ax2.plot(met[starttime:endtime].index, 
             met['1.5 m Temperature'][starttime:endtime], 
             label='1.5 m Temperature')
    ax2.plot(met[starttime:endtime].index, 
             met['9 m Temperature'][starttime:endtime], 
             label='9 m Temperature')
    ax2.plot(met[starttime:endtime].index, 
             met['Dewpoint'][starttime:endtime], 
             label='1.5 m Dewpoint')
    plt.setp(ax2.get_xticklabels(), visible=False)
    plt.ylabel('Temperature\n(C)', multialignment='center')
    plt.legend(prop={'size':8})

    ax3 = fig.add_subplot(613, sharex=ax1)
    ln1 = ax3.plot(met[starttime:endtime].index, 
                   met['Rainfall'][starttime:endtime], 
                   'g', label='Rainfall')
    plt.setp(ax3.get_xticklabels(), visible=False)
    plt.ylabel('Rainfall\nAmount\n(in)', multialignment='center')
    plt.gca().set_ylim(bottom=0)

    ax8 = ax3.twinx()
    ln2 = ax8.plot(met[starttime:endtime].index, 
                   met['Solar Radiation'][starttime:endtime], 
                   label='Solar Radiation')
    plt.ylabel('Solar\nRadiation\n(W/m2)', multialignment='center')
    lns = ln1+ln2
    labs = [l.get_label() for l in lns]
    ax8.legend(lns, labs, prop={'size':8})

    ax4 = fig.add_subplot(614, sharex=ax1)
    ax4.plot(met[starttime:endtime].index, 
             met['Station Pressure'][starttime:endtime], 
             label='Station Pressure')
    plt.setp(ax4.get_xticklabels(), visible=False)
    plt.ylabel('Station\nPressure\n(mb)', multialignment='center')
    plt.legend(prop={'size':8})

    ax5 = fig.add_subplot(615, sharex=ax1)
    ax5.plot(agr[starttime:endtime].index, 
             agr['5 cm Natural Soil Temperature'][starttime:endtime], 
             label='5 cm Soil Temperature')
    ax5.plot(agr[starttime:endtime].index, 
             agr['20 cm Natural Soil Temperature'][starttime:endtime], 
             label='20 cm Soil Temperature')
    plt.setp(ax5.get_xticklabels(), visible=False)
    plt.ylabel('Natural Soil\nTemperature (C)', multialignment='center')
    plt.legend(prop={'size':8})

    ax6 = fig.add_subplot(616, sharex=ax1)
    ax6.plot(agr[starttime:endtime].index, 
             agr['5 cm Water Content'][starttime:endtime], 
             label='5 cm Soil Water Content')
    ax6.plot(agr[starttime:endtime].index, 
             agr['20 cm Water Content'][starttime:endtime], 
             label='20 cm Soil Water Content')
    ax6.plot(agr[starttime:endtime].index, 
             agr['75 cm Water Content'][starttime:endtime], 
             label='75 cm Soil Water Content')
    ax6.plot(agr[starttime:endtime].index, 
             agr['Leaf Wetness'][starttime:endtime], 
             label='Leaf Wetness')
    plt.ylabel('Agricultural\nWater\nContent (%)', multialignment='center')
    plt.xlabel('Time (UTC)')
    plt.legend(prop={'size':8})

except: 
    KeyError
    print 'No Agricultural Data Available'
    fig = plt.figure(1)
    ax1 = fig.add_subplot(611)
    ln1 = ax1.plot(met[starttime:endtime].index, 
                   met['10 m Scalar Wind Speed'][starttime:endtime], 
                   label='Average Wind Speed')
    ln2 = ax1.plot(met[starttime:endtime].index, 
                   met['10 m Gust Wind Speed'][starttime:endtime], 
                   label='Maximum Wind Speed')
    plt.ylabel('Wind Speed\nat 10 m (m/s)', multialignment='center')
    plt.setp(ax1.get_xticklabels(), visible=False)

    ax7 = ax1.twinx()
    ln3 = ax7.plot(met[starttime:endtime].index, 
                   met['10 m Wind Direction'][starttime:endtime], 
                   '.k', linewidth=0.5, label='Wind Direction')
    plt.ylabel('Wind\nDirection\n(degrees)', multialignment='center')
    plt.ylim(0,360)
    lns = ln1+ln2+ln3
    labs = [l.get_label() for l in lns]
    ax7.legend(lns, labs, prop={'size':8})

    ax2 = fig.add_subplot(612, sharex=ax1)
    ax2.plot(met[starttime:endtime].index, 
             met['1.5 m Temperature'][starttime:endtime], 
             label='1.5 m Temperature')
    ax2.plot(met[starttime:endtime].index, 
             met['9 m Temperature'][starttime:endtime], 
             label='9 m Temperature')
    ax2.plot(met[starttime:endtime].index, 
             met['Dewpoint'][starttime:endtime], 
             label='1.5 m Dewpoint')
    plt.setp(ax2.get_xticklabels(), visible=False)
    plt.ylabel('Temperature\n(C)', multialignment='center')
    plt.legend(prop={'size':8})

    ax3 = fig.add_subplot(613, sharex=ax1)
    ln1 = ax3.plot(met[starttime:endtime].index, 
                   met['Rainfall'][starttime:endtime], 
                   'g', label='Rainfall')
    plt.setp(ax3.get_xticklabels(), visible=False)
    plt.ylabel('Rainfall\nAmount\n(in)', multialignment='center')
    plt.gca().set_ylim(bottom=0)

    ax8 = ax3.twinx()
    ln2 = ax8.plot(met[starttime:endtime].index, 
                   met['Solar Radiation'][starttime:endtime], 
                   label='Solar Radiation')
    plt.ylabel('Solar\nRadiation\n(W/m2)', multialignment='center')
    lns = ln1+ln2
    labs = [l.get_label() for l in lns]
    ax8.legend(lns, labs, prop={'size':8})

    ax4 = fig.add_subplot(614, sharex=ax1)
    ax4.plot(met[starttime:endtime].index, 
             met['Station Pressure'][starttime:endtime], 
             label='Station Pressure')
    plt.setp(ax4.get_xticklabels(), visible=False)
    plt.ylabel('Station\nPressure\n(mb)', multialignment='center')
    plt.legend(prop={'size':8})

plt.show()

