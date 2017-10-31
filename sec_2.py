# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#    Platform        : Section-2 decode code
#    Project Name    : SYNOP DATA DECODER
#    Author          : Nikhil Dhandre
#    Start Date      : 23-06-2016
#    Last Modified   : 02-07-2016
#------------------------------------------------------------------------------
def _section_2(st_no,sec_2):
    sec_2_return = {}
    sec_2_ndc = {}

    if sec_2 == {}:
        print("No Maritime data pertaining to a coastal station")
        station_data = [sec_2_return, sec_2_ndc]

    else:
        print("Maritime data pertaining to a coastal station")
        print(sec_2)
        _sec_2 = str(sec_2)

        for word in _sec_2.split():
            print(word)
        station_data = [sec_2_return, sec_2_ndc]
    return station_data