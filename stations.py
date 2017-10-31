# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#    Platform        : Station Name fetch
#    Project Name    : SYNOP DATA DECODER
#    Author          : Nikhil Dhandre
#------------------------------------------------------------------------------
import csv
def station_name(x):

    with open('db/station_data.csv') as csvfile:
        data_stations=csv.reader(csvfile, delimiter=',')

        id_all=[]
        station_no_all=[]
        station_name_all=[]

        for row in data_stations:
            id=row[0]
            station_no=row[1]
            station_name=row[2]

            id_all.append(id)
            station_no_all.append(station_no)
            station_name_all.append(station_name)

        index=station_no_all.index(x)
        return station_name_all[index]

#------------------------------------------------------------------------------