# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#    Platform        : Medium Cloud
#    Project Name    : SYNOP DATA DECODER
#    Author          : Nikhil Dhandre
#------------------------------------------------------------------------------

import csv
def medium_c(x):

    with open('db/medium_cloud.csv') as csvfile:
        mc_data=csv.reader(csvfile, delimiter=',')

        code_all=[]
        mc_all=[]

        for row in mc_data:
            code=row[0]
            mc=row[1]

            code_all.append(code)
            mc_all.append(mc)

        index=code_all.index(x)
        return mc_all[index]

#------------------------------------------------------------------------------