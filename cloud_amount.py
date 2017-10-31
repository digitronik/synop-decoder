#------------------------------------------------------------------------------
#    Platform        : Cloud Amount fetching
#    Project Name    : SYNOP DATA DECODER
#    Author          : Nikhil Dhandre
#    Start Date      : 09-07-2016
#    Last Modified   : 3-07-2016
#------------------------------------------------------------------------------

import csv
def cloud_amount(x):

    with open('db/cloud_amount.csv') as csvfile:
        N_data=csv.reader(csvfile, delimiter=',')

        code_all=[]
        N_all=[]

        for row in N_data:
            code=row[0]
            N=row[1]

            code_all.append(code)
            N_all.append(N)

        index=code_all.index(x)
        return N_all[index]
#------------------------------------------------------------------------------