# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#    Platform        : Section-0 decode code
#    Project Name    : SYNOP DATA DECODER
#    Author          : Nikhil Dhandre
#    Start Date      : 20-06-2016
#    Last Modified   : 02-07-2016
#------------------------------------------------------------------------------


def _section_0(st_no, sec_0):
    import time
    try:
        sec_0_return = {}
        sec_0_ndc = {}

        def report(MiMiMjMj):
            try:
                if MiMiMjMj == 'ZZYY':
                    report_type = "BUOY report"

                elif MiMiMjMj == 'BBXX':
                    report_type = "SHIP report"

                elif MiMiMjMj == 'AAXX':
                    report_type = "SYNOP report"
            except:
                print("Error: Report type not recognize")
                return "None"
            else:
                return report_type

    #-------------------------------MiMiMjMj---------------------------------------
        try:
            MiMiMjMj = sec_0[0]
            print("MiMiMjMj = ", MiMiMjMj)
            report_type = report(MiMiMjMj)

            print("Report Type: ", report_type)
            sec_0_return["Report_Type"] = report_type

        except:
                print("Error: MiMiMjMj fail")

    #--------------------------------YYGGiw----------------------------------------
        try:
            YYGGiw = sec_0[1]
            if YYGGiw != "NIL=":
                print("YYGGiw =", YYGGiw)
                sec_0_YYGGiw = True
            else:
                sec_0_YYGGiw = False
                print("YYGGiw absent")
        except:
            print("YYGGiw absent")
    #-------------------------------YY---------------------------------------------
    #YY>>>>
    #Present weather (Code 27)
    #i. Day of the month on which the actual time (GMT) of the observation falls.
        #01 means 1 st day of the month.
        #02 means 2 nd day of the month ... etc.
    #ii. The day is defined with reference to Greenwich Mean Time and not to local time.
        if sec_0_YYGGiw is True:
            try:
                YY = YYGGiw[0:2]
                #print("YY = ", YY)
                print("Date = ", YY)

                year = time.strftime("%y")
                month = time.strftime("%m")


                sec_0_return["Day"] = YY
                sec_0_ndc["12-13"] = YY
                sec_0_return["Month"] = month
                sec_0_ndc["8-9"] = month
                sec_0_return["Year"] = year
                sec_0_ndc["6-7"] = year

                # NDC century field
                century = time.strftime("%Y")[0:2]
                sec_0_ndc["78-79"] = century
                sec_0_ndc["80"] = "2"        # indicator (2)



            except:
                print("Error: YY fail")
        #------------------------------------------------------------------------------

        #-------------------------------GG---------------------------------------------
        #GG>>>>
        #Actual time of observation to the nearest whole hour GMT i.e. the actual time at which
        #the barometer is to be read.
            try:
                GG = YYGGiw[2:4]
                #print("GG =", GG)
                print("Hour = ", GG, "GMT")
                sec_0_return["Time"] = GG
                sec_0_ndc["10-11"] = GG

            except:
                print("Error: GG fail")

        #------------------------------------------------------------------------------
        #-------------------------------iw---------------------------------------------
        #iw >>>>Wind indicator (Code 18)

        #    iw       wind indicator                                Unit
        #    0        Wind speed estimated                        Wind speed in meters per second
        #    1        Wind speed obtained from anemometer         Wind speed in meters per second
        #    3        Wind speed estimated                        Wind speed in knots
        #    4        Wind speed obtained from anemometer         Wind speed in knots

            try:
                iw = YYGGiw[4]
                #print("iw = ", iw)

                if iw == "0":
                    wind_method = "estimated"
                    wind_unit = "m/s"

                elif iw == "1":
                    wind_method = "anemometer"
                    wind_unit = "m/s"

                elif iw == "3":
                    wind_method = "estimated"
                    wind_unit = "knots"

                elif iw == "4":
                    wind_method = "anemometer"
                    wind_unit = "knots"
                else:
                    print("Error: Synop not sended wind specifications")
                    wind_method = "None"
                    wind_unit = "None"

                print("Wind Method = ", wind_method)
                sec_0_return["Wind_Method"] = wind_method

                print("Wind Unit = ", wind_unit)
                sec_0_return["Wind_Unit"] = wind_unit

            except:
                print("Error: Synop decoding fail")

            section_data = [sec_0_return, sec_0_ndc]

    except:
        print("Error: Section-0 fail for decode")
        return [{}, {}]

    else:
        return section_data
#------------------------------------------------------------------------------
