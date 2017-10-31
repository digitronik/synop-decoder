# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#    Platform        : Type of Cloud
#    Project Name    : SYNOP DATA DECODER
#    Author          : Nikhil Dhandre
#------------------------------------------------------------------------------

import csv
def type_c(x):

    with open('db/type_of_cloud.csv') as csvfile:
        tc_data=csv.reader(csvfile, delimiter=',')

        code_all=[]
        tc_all=[]

        for row in tc_data:
            code=row[0]
            tc=row[1]

            code_all.append(code)
            tc_all.append(tc)

        index=code_all.index(x)
        return tc_all[index]

#------------------------------------------------------------------------------
