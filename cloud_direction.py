# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#    Platform        : Cloud direction fetching
#    Project Name    : SYNOP DATA DECODER
#    Author          : Nikhil Dhandre
#------------------------------------------------------------------------------

import csv
def D_direction(x):

    with open('db/cloud_direction.csv') as csvfile:
        D_data=csv.reader(csvfile, delimiter=',')

        code_all=[]
        D_all=[]

        for row in D_data:
            code=row[0]
            D=row[1]

            code_all.append(code)
            D_all.append(D)

        index=code_all.index(x)
        return D_all[index]
#------------------------------------------------------------------------------0