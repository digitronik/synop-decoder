# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#    Platform        : RRR Amount of precipitation since 0300 GMT
#    Project Name    : SYNOP DATA DECODER
#    Author          : Nikhil Dhandre
#    Start Date      : 09-07-2016
#    Last Modified   : 21-09-2016
#------------------------------------------------------------------------------

import csv
def precipitation_amount(x):

    with open('db/amount_of_precipitation.csv') as csvfile:
        N_data=csv.reader(csvfile, delimiter=',')

        code_all=[]
        N_all=[]

        for row in N_data:
            code=row[0]
            N=row[1]

            code_all.append(code)
            N_all.append(N)

        print code_all

        index=code_all.index(x)

        return N_all[index]



if __name__=="__main__":
    print(precipitation_amount("062"))
#------------------------------------------------------------------------------