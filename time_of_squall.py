# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#    Platform        : Time of Squall
#    Project Name    : SYNOP DATA DECODER
#    Author          : Nikhil Dhandre
#------------------------------------------------------------------------------

import csv
def time_squall(x):

    with open('db/time_of_squall.csv') as csvfile:
        dq_data=csv.reader(csvfile, delimiter=',')

        code_all=[]
        dq_all=[]

        for row in dq_data:
            code=row[0]
            dq=row[1]

            code_all.append(code)
            dq_all.append(dq)

        index=code_all.index(x)
        return dq_all[index]
#------------------------------------------------------------------------------