# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#    Platform        : ht above station cloud layer
#    Project Name    : SYNOP DATA DECODER
#    Author          : Nikhil Dhandre
#------------------------------------------------------------------------------

import csv
def ht_cloud_cloud_layer(x):

    with open('db/ht_above_station_cloud_layer.csv') as csvfile:
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
