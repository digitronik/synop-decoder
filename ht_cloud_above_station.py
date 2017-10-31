# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#    Platform        : ht above station
#    Project Name    : SYNOP DATA DECODER
#    Author          : Nikhil Dhandre
#------------------------------------------------------------------------------
import csv
def ht_cloud(x):

    with open('db/ht_cloud_above_station.csv') as csvfile:
        N_data=csv.reader(csvfile, delimiter=',')

        code_all=[]
        N_all=[]

        for row in N_data:
            code=row[0]
            N=row[1]

            code_all.append(code)
            N_all.append(N)

        index=code_all.index(x)
        return N_all[index]

#------------------------------------------------------------------------------
