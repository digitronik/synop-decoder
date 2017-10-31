# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#    Platform        : Section-5 decode code
#    Project Name    : SYNOP DATA DECODER
#    Author          : Nikhil Dhandre
#    Start Date      : 23-06-2016
#    Last Modified   : 02-07-2016
#------------------------------------------------------------------------------


import csv
from dq_direction import *
from max_F_wind_squall import *
from nature_of_squall import *
from time_of_squall import *

def _section_5(st_no, sec_5):

    sec_5_return = {}
    sec_5_ndc = {}

    if sec_5 == {}:
        print("No data for National Exchange")
        section_data = [sec_5_return, sec_5_ndc]

    else:
        try:
            print("Data for National Exchange")
            #print(sec_5)

#--------------------------seperation of data --------------------------------
            sec_5_list = []
            _sec_5 = str(sec_5)

            R24R24R24R24 = "None"
            RTRTRTRT = "None"
            DqFqqqt = "None"

            for word in _sec_5.split():
                sec_5_list.append(word)
#------------------------------------------------------------------------------

            for word in sec_5_list:

                if word[0] == '0':
                    try:
                        # R24R24R24R24 >>> Amount of precipitation since 0300 GMT
                        #                    in tenths of millimeter.
                        R24R24R24R24 = word[1:5]
                        print("R24R24R24R24 = ", R24R24R24R24)
                        print("Amound of Precipitation since 0300 GMT = ", R24R24R24R24)

                        sec_5_return["Rainfall(24hr)"] = R24R24R24R24
                        sec_5_ndc["63-66"] = R24R24R24R24

                    except:
                        print("Error: R24R24R24R24 decoding fail")


                elif word[0] == '1':
                    try:
                        # RTRTRTRT >>> Progressive seasonal total of precipitation
                        #                in full millimeters.
                        RTRTRTRT = word[1:5]
                        print("RTRTRTRT = ", RTRTRTRT)
                        print("Rainfall(SeasonalTotal) = ", RTRTRTRT)

                        sec_5_return["Rainfall(SeasonalTotal)"] = RTRTRTRT
                    except:
                        print("Error: RTRTRTRT decoding fail")

                elif word[0] == '2':
                    try:
                        DqFqqqt = word[1:5]
                        print("DqFqqqt = ", DqFqqqt)

                        try:
                            # Dq >>> Direction of wind during squall (Code 7)
                            Dq = DqFqqqt[0]
                            #print("Dq = ", Dq)
                            dir_wind_squall = dq_direction(Dq)
                            print("Direction of wind during squall = ", dir_wind_squall)

                            sec_5_return["Squal_Wind_Direction"] = dir_wind_squall
                        except:
                            print("Error: Dq decoding fail")

                        try:
                            # Fq >>>> Maximum force of wind on the Beaufort Scale during the squall (Code 11)
                            #The observatories which are not provided with anemographs should report by estimation
            #from the effect of the squall on the surrounding objects as described in the third and fourth
            #columns in the Tables in Code 12.
                            Fq=DqFqqqt[1]
                            #print("Fq = ",Fq)
                            max_f_wind_squall=max_F(Fq)
                            print("Maximum force of wind on the Beaufort Scale during the squall = ",max_f_wind_squall)

                            sec_5_return["Squal_Wind_Force_Max"]=max_f_wind_squall
                        except:
                            print("Error: Fq decoding fail")

                        try:
                            # q >>> Nature of squall (Code 21)
                            q = DqFqqqt[2]
                            #print("q = ", q)
                            nat_of_squall = nat_squall(q)
                            print("Nature of squall = ", nat_of_squall)

                            sec_5_return["Squall_Nature"] = nat_of_squall
                        except:
                            print("Error: q decoding fail")

                        try:
                            # qt >>> Time of occurrence of squall (Code 22)
                            qt = DqFqqqt[3]
                            #print("qt = ",qt)
                            t_squall = time_squall(qt)
                            print("Time of occurrence of squall = ", t_squall)

                            sec_5_return["Squall_Time"] = t_squall
                        except:
                            print("Error: qt decoding fail")

                    except:
                        print("Error: DqFqqqt decoding fail")

            section_data = [sec_5_return, sec_5_ndc]

        except:
            print("Error: Section-5 decoding fail")
    return section_data