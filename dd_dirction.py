# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#    Platform        : dd_direction
#    Project Name    : SYNOP DATA DECODER
#    Author          : Nikhil Dhandre
#------------------------------------------------------------------------------

import csv
def dd_direction(x):

    with open('db/dd_direction.csv') as csvfile:
        dd_data=csv.reader(csvfile, delimiter=',')

        code_all=[]
        dd_all=[]

        for row in dd_data:
            code=row[0]
            dd=row[1]

            code_all.append(code)
            dd_all.append(dd)

        index=code_all.index(x)
        return dd_all[index]


#------------------------------------------------------------------------------
