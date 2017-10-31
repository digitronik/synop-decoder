# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#    Platform        : Past Weather condition
#    Project Name    : SYNOP DATA DECODER
#    Author          : Nikhil Dhandre
#------------------------------------------------------------------------------

import csv
def past_wea(x):

    with open('db/past_weather.csv') as csvfile:
        w1w2_data=csv.reader(csvfile, delimiter=',')

        code_all=[]
        w1w2_all=[]

        for row in w1w2_data:
            code=row[0]
            w1w2=row[1]

            code_all.append(code)
            w1w2_all.append(w1w2)

        index=code_all.index(x)
        return w1w2_all[index]

#------------------------------------------------------------------------------
#