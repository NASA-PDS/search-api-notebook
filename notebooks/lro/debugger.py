from __future__ import print_function
from builtins import input
import requests
import csv
import spiceypy
from astropy.table import Table,Column
from astropy.time import Time
import pandas as pd
from astropy import units as u
import numpy as np
import datetime

from pywwt.jupyter import WWTJupyterWidget
from pywwt.jupyter import connect_to_app


def getsta(mag_time):
    #
    # Local parameters
    #
    METAKR = 'getgll.tm'
    spiceypy.furnsh(METAKR)
    row = []
    for t in mag_time:
        time_string = t.strftime('%Y-%m-%d %H:%M:%S')

        # ephemeris time after iterating
        et = spiceypy.str2et(time_string)

        #
        # Compute the apparent state of GLL as seen from
        # Jupiter in the J2000 frame.  All of the ephemeris
        # readers return states in units of kilometers and
        # kilometers per second.
        #
        [state, ltime] = spiceypy.spkezr('5', et, 'J2000',
                                         'LT+S', '-77')
        row.append([state[0], state[1], state[2], state[3], state[4], state[5]])
    return row


#
# Fetch parent Collections file and return appropriate dataset
#

def get_data(url):
    parent_response = requests.get(url)
    # just use pandas
    if parent_response.status_code == 200:
        print('Successfully loaded JSON')
        parent_data = parent_response.json()
        parent_urlkey = parent_data['properties']["ops:Data_File_Info.ops:file_ref"][0]
        tab_urls_res = requests.get(parent_urlkey)
        tab_urls_cont = tab_urls_res.text.splitlines()
        # Define mag arrays
        mag_time = []
        mag_tot = []

        for i in range(len(tab_urls_cont)):
            if 'irc' in tab_urls_cont[i].split(',')[1]:  # check for body null rate measurements
                time_data, iter_data = get_tabs(tab_urls_cont[i].split(',')[1])  # get rid of column in csv
                mag_time.extend(time_data)
                mag_tot.extend(iter_data)

    return mag_time, mag_tot


#
# Fetch the corresponding tabs to the parent data set
#

def get_tabs(url):
    # load lid found from parent collection
    lid_response = requests.get('https://pds.nasa.gov/api/search/1/products/' + url)
    lid_data = lid_response.json()

    time_data = []
    iter_data = []
    for i in range(1):  # range(len(lid_data['data'])):
        tab_url = lid_data['properties']['ops:Data_File_Info.ops:file_ref'][0]
        # load in tab data
        tab_response = requests.get(tab_url)
        tab_content = tab_response.text
        lines = tab_content.splitlines()

        for line in lines:
            raw_data = line.split()
            time_data.append(raw_data[0])
            iter_data.append(float(raw_data[4]))
    return time_data, iter_data


if __name__ == '__main__':

    url = "https://pds.nasa.gov/api/search/1/products/urn:nasa:pds:galileo-mag-jup-calibrated:data-highres-magnetosphere::1.0"
    mag_time, mag_tot = get_data(url)

    # Remove duplicates and maintain order of mag_data
    df = pd.DataFrame({'time': mag_time, 'data': mag_tot})
    df['time'] = pd.to_datetime(df['time'])
    # now sort values
    df.sort_values('time', inplace=True)
    df.drop_duplicates(subset='time', keep='first', inplace=True)

    df.reset_index(drop=True, inplace=True)

    # Obtain the position data that corresponds to the measurements
    print('Obtaining ephemeris for magnetometer data points...')
    mag_ephem_data = getsta(df['time'])  # Takes time input
    print("Number of data points: " + str(len(mag_ephem_data)))

    # Fill in the gaps for the ephemeris data
    print("Filling in ephemeris data...")
    ephem_time = []
    start_time = df['time'][0]
    for i in range(3000):
        # start_time = datetime.datetime.strptime(t, "%Y-%m-%d %H:%M:%S")
        ephem_time.append(start_time + datetime.timedelta(minutes=i * 1000))
        # Grab the states
    ephem_data = getsta(ephem_time)

    # Create csv for ephemeris data
    eph_file = 'data/eph_data2.csv'

    #         mag_tab = df['time'].replace

    #         with open(eph_file, 'w',newline='') as file:
    #                 writer1 = csv.writer(file)
    #                 writer1.writerow(['Time', 'X', 'Y', 'Z'])
    #                 for i in range(len(ephem_data)):
    #                         writer1.writerow([ephem_time[i].replace(tzinfo=None).isoformat(), float(ephem_data[i][0]),
    #                                           float(ephem_data[i][1]), float(ephem_data[i][2])])

    #         csv_file = 'data/comp_tot_data2.csv'
    #         with open(csv_file, 'w',newline='') as file:
    #                 writer = csv.writer(file)
    #                 writer.writerow(['Time','Magnitude (nT)', 'X', 'Y', 'Z'])
    #                 for i in range(0,len(mag_ephem_data),100):
    #                         writer.writerow([df['time'][i].replace(tzinfo=None).isoformat(), float(df['data'][i]),
    #                                           float(mag_ephem_data[i][0]), float(mag_ephem_data[i][1]),
    #                                             float(mag_ephem_data[i][2])])

    # # Assign variables to table for pyWWT
    # ephem_tab = Table()
    # mag_tab = Table()
    # for i in range(len(ephem_data)):
    #     ephem_tab['Time'] = [ephem_time[i].replace(tzinfo=None).isoformat()]
    #     ephem_tab['X'] = [float(ephem_data[i][0])]
    #     ephem_tab['Y'] = [float(ephem_data[i][1])]
    #     ephem_tab['Z'] = [float(ephem_data[i][2])]
    #
    # for i in range(len(mag_ephem_data)):
    #     mag_tab['Time'] = [df['time'][i].replace(tzinfo=None).isoformat()]
    #     mag_tab['Magnitude (nT)'] = float(df['data'][i])
    #     mag_tab['X'] = [float(mag_ephem_data[i][0])]
    #     mag_tab['Y'] = [float(mag_ephem_data[i][1])]
    #     mag_tab['Z'] = [float(mag_ephem_data[i][2])]

    # Assign variables to table for pyWWT
ephem_tab = Table()
mag_tab = Table()
# for i in range(len(ephem_data)):
# ephem_tab['Time'] = [ephem_time[i].replace(tzinfo=None).isoformat()]
timecolumn = Column(ephem_data[:][0], name='Time', dtype=str)
ephem_tab[timecolumn]
xcolumn = Column(ephem_data[:][0], name='X', dtype=float)
ephem_tab[xcolumn]
ycolumn = Column(ephem_data[:][1], name='Y', dtype=float)
ephem_tab[ycolumn]
zcolumn = Column(ephem_data[:][2], name='Z', dtype=float)
ephem_tab[zcolumn]
# ephem_tab['X'] = np.array(float(ephem_data[:][0]))
# ephem_tab['Y'] = [float(ephem_data[:][1])]
# ephem_tab['Z'] = [float(ephem_data[:][2])]


timecolumn = Column(df['time'][:], name='Time', dtype=str)
mag_tab[timecolumn]
magcolumn = Column(df['data'][:], name='Magnitude (nT)', dtype=float)
mag_tab[xcolumn]
xcolumn = Column(mag_ephem_data[:][0], name='X', dtype=float)
mag_tab[ycolumn]
ycolumn = Column(mag_ephem_data[:][1], name='Y', dtype=float)
mag_tab[ycolumn]
zcolumn = Column(mag_ephem_data[:][2], name='Z', dtype=float)
mag_tab[zcolumn]
# # for i in range(len(mag_ephem_data)):
# mag_tab['Time'] = [df['time'][:].replace(tzinfo=None).isoformat()]
# mag_tab['Magnitude (nT)'] = float(df['data'][:])
# mag_tab['X'] = [float(mag_ephem_data[:][0])]
# mag_tab['Y'] = [float(mag_ephem_data[:][1])]
# mag_tab['Z'] = [float(mag_ephem_data[:][2])]

print('Done!')