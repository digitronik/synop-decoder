# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#    Platform        : Visibility
#    Project Name    : SYNOP DATA DECODER
#    Author          : Nikhil Dhandre
#------------------------------------------------------------------------------
import csv
def visibility(x):

    with open('db/visibility.csv') as csvfile:
        vv_data=csv.reader(csvfile, delimiter=',')

        code_all=[]
        vv_all=[]

        for row in vv_data:
            code=row[0]
            vv=row[1]

            code_all.append(code)
            vv_all.append(vv)

        index=code_all.index(x)
        return vv_all[index]

#------------------------------------------------------------------------------