# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#    Platform        : High cloud
#    Project Name    : SYNOP DATA DECODER
#    Author          : Nikhil Dhandre
#------------------------------------------------------------------------------
import csv
def high_c(x):

    with open('db/high_cloud.csv') as csvfile:
        hc_data=csv.reader(csvfile, delimiter=',')

        code_all=[]
        hc_all=[]

        for row in hc_data:
            code=row[0]
            hc=row[1]

            code_all.append(code)
            hc_all.append(hc)

        index=code_all.index(x)
        return hc_all[index]

#------------------------------------------------------------------------------
