# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#    Platform        : elevation angle calculation
#    Project Name    : SYNOP DATA DECODER
#    Author          : Nikhil Dhandre
#------------------------------------------------------------------------------

import csv
def e_angle(x):

    with open('db/elevation_angle_cloud.csv') as csvfile:
        e_data=csv.reader(csvfile, delimiter=',')

        code_all=[]
        e_all=[]

        for row in e_data:
            code=row[0]
            e=row[1]

            code_all.append(code)
            e_all.append(e)

        index=code_all.index(x)
        return e_all[index]


#------------------------------------------------------------------------------