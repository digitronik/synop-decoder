# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#    Platform        : Low Cloud
#    Project Name    : SYNOP DATA DECODER
#    Author          : Nikhil Dhandre
#------------------------------------------------------------------------------

import csv
def low_c(x):

    with open('db/low_cloud.csv') as csvfile:
        lc_data=csv.reader(csvfile, delimiter=',')

        code_all=[]
        lc_all=[]

        for row in lc_data:
            code=str(row[0])
            lc=str(row[1])

            code_all.append(code)
            lc_all.append(lc)

        index=code_all.index(x)
        return lc_all[index]

#------------------------------------------------------------------------------