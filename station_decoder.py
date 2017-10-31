# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#    Platform        : Station Decoder
#    Project Name    : SYNOP DATA DECODER
#    Author          : Nikhil Dhandre
#    Start Date      : 04-06-2016
#    Last Modified   : 3-07-2016
#------------------------------------------------------------------------------
# taking perticular station data and send to the section file for
# decoding and decode


#------------------------------------------------------------------------------
def decode_station(st_no, station):
    from sec_0 import _section_0
    from sec_1 import _section_1
    from sec_2 import _section_2
    from sec_3 import _section_3
    from sec_5 import _section_5

    station_return = []
    station_decoded = {}
    station_ndc = {}
    try:
        print("\n")
        print station
        print("STARTING OPERATION ON ", st_no)

        print("\n")
        print("CALLING SECTION-0 \n")
        r_sec_0 = _section_0(st_no, station['section_0'])
        #print(r_sec_0)
        print("-------------------------------------------------------- \n")
        try:
            wind_unit = r_sec_0[0]["Wind_Unit"]
        except:
            wind_unit = "None"

        print("\n")
        print("CALLING SECTION-1 \n")
        r_sec_1 = _section_1(st_no, station['section_1'], wind_unit)
        #print(r_sec_1)
        print("-------------------------------------------------------- \n")

        print("\n")
        print("CALLING SECTION-2 \n")
        r_sec_2 = _section_2(st_no, station['section_2'])
        print("section-2 return is    ", r_sec_2)
        print("-------------------------------------------------------- \n")

        print("\n")
        print("CALLING SECTION-3 \n")
        r_sec_3 = _section_3(st_no, station['section_3'])
        #print(r_sec_3)
        print("-------------------------------------------------------- \n")

        print("\n")
        print("CALLING SECTION-5 \n")
        r_sec_5 = _section_5(st_no, station['section_5'])
        #print(r_sec_5)
        print("-------------------------------------------------------- \n")

        for d in r_sec_0, r_sec_1, r_sec_2, r_sec_3, r_sec_5:
            if d != [{}, {}]:
                sec_dec = d[0]
                sec_ndc = d[1]

                station_decoded.update(sec_dec)
                station_ndc.update(sec_ndc)
        print("...................")
        #print station_decoded
        print("...................")
        print station_ndc

    except:
        print("Error: Station decoding fail")

    else:
        station_return = [station_decoded, station_ndc]
        return station_return