# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#    Platform        : Present Weather condition
#    Project Name    : SYNOP DATA DECODER
#    Author          : Nikhil Dhandre
#------------------------------------------------------------------------------

import csv
def present_wea(x):

    with open('db/present_weather.csv') as csvfile:
        ww_data=csv.reader(csvfile, delimiter=',')

        code_all=[]
        ww_all=[]

        for row in ww_data:
            code=row[0]
            ww=row[1]

            code_all.append(code)
            ww_all.append(ww)

        index=code_all.index(x)
        return ww_all[index]

#------------------------------------------------------------------------------
