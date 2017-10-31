# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#    Platform        : Section-1 decode code
#    Project Name    : SYNOP DATA DECODER
#    Author          : Nikhil Dhandre
#    Start Date      : 23-06-2016
#    Last Modified   : 02-07-2016
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
from stations import *
from ht_cloud_above_station import *
from visibility import *
from cloud_amount import *
from dd_dirction import *
from present_weather import *
from past_weather import *
from low_cloud import *
from medium_cloud import *
from high_cloud import *
from check_points import *

def _section_1(st_no, sec_1, wind_u):
    sec_1_return = {}    # define directory for returning values in section-1
    sec_1_ndc = {}

    if sec_1 == {}:
        print("No data for International exchange")
        section_data = [sec_1_return, sec_1_ndc]

    else:

        try:
            print("Data for international exchange")
            #print(sec_1)

            # Two field are mendetary  l.e  iR iX h V V and N d d f f so take it out

            sec_1_list = []
            _sec_1 = str(sec_1)

            for word in _sec_1.split():
                sec_1_list.append(word)

            sub_sec_1_list = sec_1_list[3:]

        except:
            print("Error: Seperating fix data in section-0 fail")
#----------------------------For fix data--------------------------------------

#----------------------------Station Index-------------------------------------
        try:
            station_index = sec_1_list[0]
            sec_1_return["Station_Index"] = station_index
            sec_1_ndc["1-5"] = station_index

            try:
                station = station_name(station_index)
                print("Station Name = ", station)
                sec_1_return["Station_Name"] = station
            except:
                print("Station Name Not available in database")

        except:
            print("Error: Station Index decoding fail")




#-------------------------------iRiXhVV----------------------------------------
        try:
            iRiXhVV = sec_1_list[1]

            if iRiXhVV != "NIL=":
                print("iRiXhVV = ", iRiXhVV)
                sec_1_irixhvv = True
            else:
                sec_1_irixhvv = False

            #-------------------------------iR-------------------------------------
            #iR>>> Indicator for inclusion or omission of precipitation data (Code 17)

            #Code figure                     Group 6RRRt
            #1                Included in Section 1
            #2                Included in Section 3
            #3                Omitted in Sec. 1 and 3   (Precipitation amount = 0)
            #4                Omitted in Sec. 1 and 3   (Precipitation amount not available)
            if sec_1_irixhvv:
                try:
                    iR = iRiXhVV[0]
                    #print("iR = ",iR)

                    if iR == "1":
                        gp_6RRRt = "Include in section 1"

                    if iR == "2":
                        gp_6RRRt = "Include in section 3"

                    if iR == "3":
                        gp_6RRRt = "Omitted in section 1 and 3"
                        precipitation_amount = "0"
                        print("precipitation_amount = ", precipitation_amount)
                        sec_1_return["Precipitation_amount"] = precipitation_amount

                    if iR == "4":
                        gp_6RRRt = "Omitted in Sec. 1 and 3"
                        precipitation_amount = 'None'
                        print("precipitation_amount = ", precipitation_amount)
                        sec_1_return["Precipitation_amount"] = precipitation_amount

                    print("Precipitation Status = ", gp_6RRRt)
                    sec_1_return["Precipitation_status"] = gp_6RRRt

                except:
                    print("Error: iR decoding fail")

                #-------------------------------iX-----------------------------------------------
                #ix>>> Indicator for type of  (manned or automatic) and for
                #present and past weather data (Code 19)

                #Code figure   Type of station operation   Group 7wwW 1 W 2 is
                #1                Manned                Included.
                #2                Manned                Omitted (no significant phenomenon to report)
                #3                Manned                Omitted (not observed data not available)
                #4                Automatic             Included
                #5                Automatic             Omitted (no significant phenomenon to report)
                #6                Automatic             Omitted (not observed data not available)

                try:
                    iX = iRiXhVV[1]
                    #print("iX = ", iX)

                    if iX == "1":
                        type_station_operation = "Manned"
                        gp_7wwW1W2 = "Included"

                    if iX == "2":
                        type_station_operation = "Manned"
                        gp_7wwW1W2 = "Omitted (no significant phenomenon to report)"

                    if iX == "3":
                        type_station_operation = "Manned"
                        gp_7wwW1W2 = "Omitted (not observed data not available)"

                    if iX == "4":
                        type_station_operation = "Automatic"
                        gp_7wwW1W2 = "Included"

                    if iX == "5":
                        type_station_operation = "Automatic"
                        gp_7wwW1W2 = "Omitted (no significant phenomenon to report)"

                    if iX == "6":
                        type_station_operation = "Automatic"
                        gp_7wwW1W2 = "Omitted (not observed data not available)"

                    print("Tytpe of station operation = ", type_station_operation)
                    print("Group 7wwW1W2 = ", gp_7wwW1W2)

                    sec_1_return["Station_Operation"] = type_station_operation
                    sec_1_return["7wwW1W2_Status"] = gp_7wwW1W2

                except:
                    print("Error: iX decoding fail")

                #-------------------------------h-----------------------------------------------
                #h>>>>>> Height above gro und of the base of the lowest cloud seen (Code 14)
                #Code Figure    Height of base of cloud above station
                #0                0 – 49 m
                #1                50 – 99 m
                #2                100 – 199 m
                #3                200 – 299 m
                #4                300 – 599 m
                #5                600 – 999 m
                #6                1000 – 1499 m
                #7                1500 – 1999 m
                #8                2000 – 2500 m
                #9                No cloud below 2500 m
                #/                Base of cloud at a level lower and tops at a
                                #level higher than that of the station (Only for
                                #mountain stations). Base of cloud not
                try:
                    h = iRiXhVV[2]
                    #print("h = ",h)

                    ht_c = ht_cloud(h)

                    print("Height of base of cloud above station = ", ht_c)

                    sec_1_return["ht_of_lowest_cloud"] = ht_c
                    sec_1_ndc["58"] = h

                except:
                    print("Error: h decoding fail")

                #-------------------------------VV-------------------------------------
                #VV>>>>> Horizontal visibility or distance at which objects can be seen in day
                #light (or at which lights can be seen at night) (Code 25)

                try:
                    VV = iRiXhVV[3:5]
                    #print("VV = ", VV)

                    vv_km = visibility(VV)
                    print("Horizontal visibility = ", vv_km)

                    sec_1_return["Visibility"] = vv_km
                    sec_1_ndc["46-47"] = VV
                except:
                    print("Error: VV decoding fail")

        except:
            print("Error: iRiXhVV decoding fail")

#----------------------------------Nddff---------------------------------------
        try:
            if sec_1_irixhvv:
                Nddff = sec_1_list[2]
                print("Nddff = ", Nddff)

                #---------------------------------N-------------------------------------
                #N>>>>>>>> The fraction of the sky covered by clouds of all types (Code 20)
                try:
                    N = Nddff[0]
                    #print("N = ",N)
                    N_amount = cloud_amount(N)
                    print("The fraction of the sky covered by clouds = ", N_amount)

                    sec_1_return["Cloud_Total_Amount"] = N_amount
                    sec_1_ndc["57"] = N

                except:
                    print("Error: N decoding fail")

                #-------------------------------dd-------------------------------------
                #dd>>>>> True direction from which the surface wind blows. (Code 8)
                try:
                    dd = Nddff[1:3]
                    #print("dd = ", dd)
                    dd_dir = dd_direction(dd)
                    print("Wind Direction = ", dd_dir)

                    sec_1_return["Wind_Direction"] = dd_dir
                    sec_1_ndc["39-40"] = dd
                except:
                    print("Error: dd decoding fail")

                #-------------------------------ff-------------------------------------
                #ff Wind speed in knots (Code 12)
                try:
                    ff = Nddff[3:5]
                    #print("ff = ", ff)

                    if wind_u == "knots":
                        ff_kmh = round((int(ff) *  1.852), 2)
                        ff_kmh_rounded = str(int(round(ff_kmh))).zfill(3)
                        print ff_kmh_rounded
                    else:
                        ff_kmh = ff
                        ff_kmh_ndc = ff_kmh.zfill(3)

                    print("Wind Speed = ", ff_kmh, "km/h")

                    sec_1_return["Wind_Speed_kmh"] = ff_kmh
                    sec_1_ndc["41-43"] = ff_kmh_ndc
                except:
                    print("Error: ff decoding fail")
            else:
                print("No Nddff data available")
        except:
            print("Error: Nddff decoding fail")

#----------------------------For non-fix data----------------------------------
        SnTTT = "None"
        SnTdTdTd = "None"
        P0P0P0P0 = "None"
        PPPP = "None"
        wwW1W2 = "None"
        NhCLCMCH = "None"

        def alph_decimal(n):
            alpha = ["}", "J", "K", "L", "M", "N", "O", "P", "Q", "R"]
            return alpha[n]

        for word in sub_sec_1_list:
#------------------------------SnTTT-------------------------------------------
            if word[0] == '1':
                SnTTT = word
                print("SnTTT = ", SnTTT)

                try:
                    # sn >>> Sign of temperature to be reported as zero (0) for positive
                    # temperatures or 0oC and one (1) for negative temperatures
                    Sn_1 = SnTTT[1]
                    #print("Sn = ", Sn_1)
                    # TTT >>> Air temperature in tenths of a degree Celsius. (Code 24)
                    TTT = SnTTT[2:5]
                    #print("TTT = ", TTT)
                    a_temp = int(TTT) * 0.1

                    if Sn_1 == '1':
                        a_temp_ndc = str(TTT[0:2]) + alph_decimal(int(TTT[2]))
                        a_temp = -1 * a_temp
                        print a_temp_ndc
                    else:
                        a_temp = TTT
                        a_temp_ndc = TTT

                    print("Air Temperature = ", a_temp)

                    sec_1_return["Air_Temperature"] = a_temp
                    sec_1_ndc["24-26"] = a_temp_ndc

                except:
                    print("Error: 1SnTTT decoding fail")

#------------------------------SnTdTdTd----------------------------------------
            elif word[0] == "2":
                SnTdTdTd = word
                print("SnTdTdTd = ", SnTdTdTd)

                try:
                    # sn >>> Sign of temperature to be reported as zero (0) for positive
                    #temperatures or 0oC and one (1) for negative temperatures
                    Sn_2 = SnTdTdTd[1]
                    #print("Sn = ",Sn_2)

                    # TdTdTd >>> Dew point temperature
                    TdTdTd = SnTdTdTd[2:5]
                    #print("TdTdTd = ", TdTdTd)

                    dew_temp = int(TdTdTd) * 0.1

                    if Sn_2 == '1':
                        dew_temp_ndc = str(TdTdTd[0:2]) + alph_decimal(int(TdTdTd[2]))
                        dew_temp = -1 * dew_temp

                    else:
                        dew_temp = TdTdTd
                        dew_temp_ndc = TdTdTd

                    print("Dew Point Temperature = ", dew_temp)

                    sec_1_return["Dew_Point_Temperature"] = dew_temp
                    sec_1_ndc["30-32"] = dew_temp_ndc

                except:
                    print("Error: 2snTdTdTd decoding fail")

#------------------------------P0P0P0P0----------------------------------------
            elif word[0] == "3":
                # P0P0P0P0 >>> Pressure at station level in tenths of a millibar,
                #              omitting thousands digit.
                P0P0P0P0 = word[1:5]

                if elisibility(P0P0P0P0):
                    if P0P0P0P0[0] == "0":
                        pressure = 1000 + int(P0P0P0P0) * 0.1

                    else:
                        pressure = int(P0P0P0P0) * 0.1

                    pressure = str(round(pressure,1))

                    #print("P0P0P0P0 = ", P0P0P0P0)
                    print("Pressure at station level in tenths of a millibar= ", pressure)

                    sec_1_return["Pressure_Station_Level"] = pressure
                    sec_1_ndc["14-18"] = P0P0P0P0.zfill(5)
                else:
                    print("Invalide data")

#------------------------------PPPP---------------------------------------------
            elif word[0] == "4":
                #PPPP >>> Pressure at mean sea level in tenths of a millibar,
                #         omitting thousands digit.
                PPPP = word[1:5]
                if elisibility(PPPP):
                    if PPPP[0] == "0":
                        sea_pressure = 1000 + int(PPPP) * 0.1

                    else:
                        sea_pressure = int(PPPP) * 0.1

                    sea_pressure = str(round(sea_pressure,1))

                    #print("PPPP =", PPPP)
                    print("Pressure at mean sea level in tenths of a millibar= ", sea_pressure)

                    sec_1_return["Pressure_Mean_Sea_Level"] = sea_pressure
                    sec_1_ndc["19-23"] = PPPP.zfill(5)
                else:
                    print("Invalide data")

#------------------------------wwW1W2-------------------------------------------
            elif word[0] == "7":
                wwW1W2 = word
                print("wwW1W2 = ", wwW1W2)
                try:
                    # ww >>> Present weather (Code 27)
                    ww = wwW1W2[1:3]
                    #print("ww = ", ww)

                    present_ww = present_wea(ww)
                    print("Present Weather= ", present_ww)

                    sec_1_return["Weather_Present"] = present_ww
                except:
                    print("Error: ww decoding fail")

                #W1W2 >>> Past weather (Code 26)
                try:
                    W1W2 = wwW1W2[3:5]
                    W1 = W1W2[0]
                    W2 = W1W2[1]
                    #print("W1W2 = ",W1W2)

                    past_W1 = past_wea(W1)
                    past_W2 = past_wea(W2)

                    print("Pass Weather= ", past_W1, "\n              ", past_W2)

                    sec_1_return["Weather_Past_W1"] = past_W1
                    sec_1_return["Weather_Past_W2"] = past_W2
                except:
                    print("Error: W1W2 decoding fails")

#------------------------------NhCLCMCH-----------------------------------------
            elif word[0] == "8":
                NhCLCMCH = word
                print("NhCLCMCH = ", NhCLCMCH)
                try:
                    # Nh >>> The fraction of the sky covered by low cloud reported
                    #        for CL. In case where no CL clouds exists Nh shall
                    #        refer to the amount of cloud reported for CM. (Code 20)
                    try:
                        Nh = NhCLCMCH[1]
                        #print("Nh = ", Nh)

                        cx_amount = cloud_amount(Nh)
                        print("Low cloud Ammount = ", cx_amount)

                        sec_1_return["Low_cloud_Amount"] = cx_amount
                        sec_1_ndc["49"] = Nh
                    except:
                        print("Error: Nh decoding fail")

                    try:
                        # CL >>> Form of Low Clouds (Code 4)
                        CL = NhCLCMCH[2]
                        #print("CL = ", CL)

                        lc = low_c(CL)
                        print("Form of Low Clouds= ", lc)

                        sec_1_return["Clound_Low_Form"] = lc
                        sec_1_return["48"] = CL
                    except:
                        print("Error CL decoding fail")

                    try:
                        # CM >>> Form of Medium Clouds (Code 5)
                        CM = NhCLCMCH[3]
                        #print("CM = ", CM)
                        mc = medium_c(CM)
                        print("Form of Medium Clouds= ", mc)

                        sec_1_return["Cloud_Medium_Form"] = mc
                        sec_1_ndc["50"] = CM
                    except:
                        print("Error: CM decoding fail")

                    try:
                        # CH >>> Form of High Clouds (Code 3)
                        CH = NhCLCMCH[4]
                        #print("CH = ", CH)
                        hc = high_c(CH)
                        print("Form of High Clouds= ", hc)

                        sec_1_return["Cloud_High_Form"] = hc
                        sec_1_ndc["52"] = CH
                    except:
                        print("Error: CH decoding fail")

                except:
                    print("Error: NhCLCMCH Decoding fail")

        section_data = [sec_1_return, sec_1_ndc]
    return section_data

#-------------------------------------------------------------------------------