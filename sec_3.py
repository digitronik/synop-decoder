# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#    Platform        : Section-3 decode code
#    Project Name    : SYNOP DATA DECODER
#    Author          : Nikhil Dhandre
#    Start Date      : 23-06-2016
#    Last Modified   : 02-07-2016
#------------------------------------------------------------------------------
from cloud_direction import *
from type_of_cloud import *
from elevation_angle_cloud import *
from cloud_amount import *
from ht_above_station_cloud_layer import *
import csv


def _section_3(st_no, sec_3):

    sec_3_return = {}
    sec_3_ndc = {}

#------------------------Check section-3 availibility--------------------------
    if sec_3 == {}:
        print("No data for Regional Exchange")
        section_data = [sec_3_return, sec_3_ndc]

    else:
        print("Data for Regional Exchange")
        #print(sec_3)

##------------------------Split data and make one list-------------------------
        sec_3_list = []
        _sec_3 = str(sec_3)

        for word in _sec_3.split():
            sec_3_list.append(word)

#-----------------------------itterating data start----------------------------

        SnTxTxTx = "None"
        SnTnTnTn = "None"
        _6DLDMDH = "None"
        _7CDaec = "None"
        _8P24P24P24= "None"
        _9P24P24P24= "None"
        RRRtR = "None"
        NsChshs = "None"
        SpSpspsp = "None"

        for word in sec_3_list:
#-------------------------------SnTxTxTx---------------------------------------
            if word[0]=='1':
                try:
                    SnTxTxTx = word
                    print("SnTxTxTx = ", SnTxTxTx)

                    # sn >>> Sign of temperature to be reported as zero (0) for positive
                    #temperatures or 0oC and one (1) for negative temperatures
                    Sn_1 = word[1]
                    #print("Sn = ", Sn_1)

                    # TxTxTx >>> Maximum day time temperature in tenths of a
                    # degree Celsius. (Code 24)
                    TxTxTx = word[2:5]
                    #print("TxTxTx = ",TxTxTx)
                    TxTxTx = round(float(TxTxTx) * 0.1, 2)

                    if Sn_1 == '1':
                        Max_day_temp = str(-1 * TxTxTx)
                    else:
                        Max_day_temp = str(TxTxTx)

                    print("Maximum day time temperature = ", Max_day_temp)

                    sec_3_return["Temp_Day_Max"] = Max_day_temp

                except:
                    print("Error: SnTxTxTx decoding fail")

#-------------------------------SnTnTnTn---------------------------------------

            elif word[0] == '2':
                try:
                    SnTnTnTn = word
                    print("SnTnTnTn = ",SnTnTnTn)

                    # sn >>> Sign of temperature to be reported as zero (0) for positive
                    #temperatures or 0oC and one (1) for negative temperatures
                    Sn_2 = SnTnTnTn[1]
                    #print("Sn = ",Sn_2)

                    # TnTnTn >>>> Minimum night time temperature in tenths of a
                    #            degree Celsius. (Code 24)
                    TnTnTn = SnTnTnTn[2:5]
                    #print("TnTnTn = ",TnTnTn)
                    TnTnTn = round(float(TnTnTn) * 0.1, 2)

                    if Sn_2 == '1':
                        Min_night_temp = str(-1 * TnTnTn)
                    else:
                        Min_night_temp = str(TnTnTn)

                    print("Minimum night time temperature = ",Min_night_temp)

                    sec_3_return["Temp_Night_Min"] = Min_night_temp

                except:
                    print("Error: SnTnTnTn decoding fail")


#-------------------------------_6DLDMDH---------------------------------------
            elif word[0:2] == '56':
                try:
                    _6DLDMDH = word
                    print("_6DLDMDH = ",_6DLDMDHP)

                    # DL >>>> Direction from which Low Cloud is moving towards
                    #            station (Code 6)
                    DL = _6DLDMDH[2]
                    #print("DL = ",DL)
                    lcd = D_direction(DL)
                    print("Direction from which Low Cloud is moving towards station =", lcd)

                    sec_3_return["Cloud_Direction_Low"] = lcd
                    sec_3_ndc["54"] = DL
                except:
                    print("Error: DL decoding fail")

                try:
                    # DM >>>> Direction from which Medium Cloud is moving
                    #        towards station (Code 6)
                    DM = _6DLDMDH[3]
                    #print("DM = ",DM)
                    mcd = D_direction(DM)
                    print("Direction from which Medium Cloud is moving towards station =", mcd)

                    sec_3_return["Cloud_Direction_Medium"] = mcd
                    sec_3_ndc["55"] = DM
                except:
                    print("Error: DM decoding fail")

                try:
                    #DH >>>>    Direction from which High Cloud is moving
                    #            towards station (Code 6)
                    DH = _6DLDMDH[4]
                    #print("DH = ",DH)
                    hcd = D_direction(DH)
                    print("Direction from which High Cloud is moving towards station =", hcd)

                    sec_3_return["Cloud_Direction_High"] = hcd
                    sec_3_ndc["56"] = DH
                except:
                    print("Error: DL decoding fail")

#--------------------------------_7CDaec---------------------------------------
            elif word[0:2] == '57':
                _7CDaec = word
                print("_7CDaec = ", _7CDaec)

                try:
                    # C >>>> Type of cloud (Code 2)
                    C = _7CDaec[2]
                    #print("C = ", C)
                    cloud_type = type_c(C)
                    print("Type of cloud = ", cloud_type)

                    sec_3_return["Cloud_Type"] = cloud_type
                except:
                    print("Error: C decoding fail")

                try:
                    # Da >>>> Direction in which orographic clouds or clouds
                    #        with vertical development are seen (Code 6)
                    Da = _7CDaec[3]
                    #print("Da = ", Da)
                    d_orographic_cloud = D_direction(Da)
                    print("Direction in which orographic clouds or clouds of vertical development are seen = ", d_orographic_cloud)

                    sec_3_return["Cloud_Direction"] = d_orographic_cloud
                except:
                    print("Error: Da decoding fail")

                try:
                    # eC >>>> Elevation angle of the top of the cloud
                    #        indicated by C (Code 10)
                    ec = _7CDaec[4]
                    #print("ec = ",ec)
                    ele_angle=e_angle(ec)
                    print("Elevation angle of the top of the cloud = ",ele_angle)

                    sec_3_return["Cloud_Elevation_Angle"]=ele_angle
                except:
                    print("Error: eC decoding fail")


#-------------------------------_8P24P24P24------------------------------------
            elif word[0:2]=='58':
                try:
                    _8P24P24P24 = word
                    # P24P24P24 >>> Change of station level pressure in last 24
                    #            hours in tents of a millibar
                    P24P24P24_8 = _8P24P24P24[2:5]
                    print("58P24P24P24 = ",P24P24P24_8)
                    print("Change of station level pressure in last 24 hours in tents of a millibar = ", P24P24P24_8)

                    sec_3_return["Change_Pressure_Station_Level(24hr)"] = P24P24P24_8
                except:
                    print("Error: P24P24P24 decoding fail")
    #-------------------------------_9P24P24P24------------------------------------
            elif word[0:2]== '59':
                _9P24P24P24 = word
                # P24P24P24 >>> Change of station level pressure in last 24
                #            hours in tents of a millibar
                P24P24P24_9 = _9P24P24P24[2:5]

                print("59P24P24P24 = ",P24P24P24_9)
                print("Change of station level pressure in last 24 hours in tents of a millibar = ",P24P24P24_9)
                sec_3_return["Pressure_Station_Level_Change(24hr)"]=P24P24P24_9

#------------------------------- RRRtR-----------------------------------------
            elif word[0] == '6':
                RRRtR = word
                print("6RRRtR = ",RRRtR)
                try:
                    # RRR >>> Amount of precipitation since 0300 GMT (Code 23)
                    RRR = RRRtR[1:4]
                    #print("RRR = ",RRR)

                    sec_3_return["Rainfall(sec-3)"] = RRR
                except:
                    print("Error: RRR decoding fail")

                try:
                    # tR >>>> Duration of period of precipitation in units of 6
                    #        hours and ending at the time of the observation.
                    #        In India tR will always be reported as “/” as RRR is
                    #        always the amount of precipitation since 0300 GMT.
                    tR = RRRtR[4]
                    #print("tR = ",tR)
                    sec_3_return["Rainfall_Period"] = tR
                except:
                    print("Error: tR decoding fail")
#------------------------------- NsChshs---------------------------------------
            elif word[0] == '8':
                NsChshs = word
                print("NsChshs = ", NsChshs)

                try:
                    #Ns Amount of individual cloud layer or mass of type C (Code 20)
                    Ns = NsChshs[1]
                    #print("Ns = ", Ns)
                    amt_ind_cloud = cloud_amount(Ns)
                    print("Amount of individual cloud layer = ", amt_ind_cloud)

                    sec_3_return["Individual_Layer_Cloud_Amount"] = amt_ind_cloud
                    sec_3_ndc["60"] = Ns
                except:
                    print("Error: Ns decoding fail")

                try:
                    # C >>> Type of cloud (Code 2)
                    C = NsChshs[2]
                    #print("C = ", C)
                    type_of_ind_c = type_c(C)
                    print("Type of individual cloud Layer = ", type_of_ind_c)

                    sec_3_return["Individual_Layer_Cloud_Form"] = type_of_ind_c
                    sec_3_ndc["59"] = C
                except:
                    print("Error: C decoding fail")

                try:
                    # hshs >>> Height above station of base of cloud layer or mass
                    #            whose type is indicated by C (Code 16)
                    hshs = NsChshs[3:5]
                    #print("hshs = ",hshs)
                    ht_above_station_mass = ht_cloud_cloud_layer(hshs)
                    print("Height of Individual Layer Cloud = ",ht_above_station_mass)

                    sec_3_return["Individual_Layer_Cloud_height"]=ht_above_station_mass
                    sec_3_ndc["61-62"] = hshs
                except:
                    print("Error: hshs decoding fail")

#-------------------------------SpSpspsp----------------------------------------
            elif word[0]== '9':
                try:
                    # SpSpspsp >>> Special Phenomena (See “Supplement to Weather Code 1955”)
                    SpSpspsp=word
                    print("SpSpspsp = ",SpSpspsp)
                    print("Special Phenomena")
                except:
                    print("Error: SpSpspsp decoding fail")

        section_data = [sec_3_return, sec_3_ndc]
    return section_data
#------------------------------------------------------------------------------