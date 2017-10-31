# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#    Platform        : Main Decoder file
#    Project Name    : SYNOP DATA DECODER
#    Author          : Nikhil Dhandre
#    Start Date      : 01-06-2016
#    Last Modified   : 09-01-2017
#------------------------------------------------------------------------------
# Took the msg file from SYNOP Decoder in decoder fuction
# Seperate all data and make one directory of tatal data with station names
# and send station wise data to station_decoder.py for further process
#------------------------------------------------------------------------------

from station_decoder import *
from export_data import *


#-----------------------FILE OPENING-------------------------------------------
def decoder(msg):
    status_list = [] #[msg_file_status, decoding_status, ndc_form_III_status]
    try:
        try:
            file = open(msg, "r")
            searchlines = file.readlines()
            file.close()

        except:
            print("Error-1: Messege file reading fail")
            msg_file_status = False

        else:
            print("Messeger File read successfully")
            msg_file_status = True

        status_list.append(msg_file_status)     # appending status of msg file

    #--------------------------------------------------------------------------

    #-----------------------INITIALISATION-------------------------------------
        print("WELCOME TO SYNOP DATA DECODER ")
        print("INITIALISATION STARTING")

        data = []                       # Total data in list format
        sec_0 = []                      # Section-0 common to all data
        total_station = 0               # Count total number of stations from line
        terminating_line_no = []        # Terminating line number list

        all_station_data = []     # list of all returning data for exporting in csv
        all_ndc_form_III = []

        try:
            for i, line in enumerate(searchlines):
                data.append(line)

                if "XX" in line:
                    sl = line.split()
                    for word in sl:
                        sec_0.append(word)

                if "=" in line:
                    total_station += 1
                    terminating_line_no.append(i + 1)
            #-------------------------------------------------------------------------

            #---------------------MAKING DICTIONARY WITH KEYS IN FORMAT---------------
            print("MAKING DICTIONARY WITH KEYS")

            station_data = {}            # Main Dirctionary Initialization

            for s_num in range(1, total_station + 1):
                station_data['station_%02d' % s_num] = {}
                station_data['station_%02d' % s_num]['section_0'] = {}
                station_data['station_%02d' % s_num]['section_1'] = {}
                station_data['station_%02d' % s_num]['section_2'] = {}
                station_data['station_%02d' % s_num]['section_3'] = {}
                station_data['station_%02d' % s_num]['section_5'] = {}
            #-------------------------------------------------------------------------

            #---APPENDING DATA OF sec-0 IN section-0 PART OF MAIN DIRECTORY-----------

            print("APPENDING section-0 DATA")

            for s_num in range(1, total_station + 1):
                station_data['station_%02d' % s_num]['section_0'] = sec_0

            #-------------------------------------------------------------------------
        #-APPENDING DATA OF OTHER SECTION DATA IN RESPECTIVE SECTION OF MAIN DIRECTORY-
            print("APPENDING OTHER SECTION DATA")

            start_bit = 1            # set start bit of for loop to 1 (index set to 1)
            st = 1                   # station count set to 1

            for num in terminating_line_no:
                end_bit = num

                for idx in range(start_bit, end_bit):
                    st_name = 'station_%02d' % st

                    row_start_len = len(data[idx].split()[0])

                    if row_start_len == 3:
                        if "222" in data[idx]:
                            #print("222 gp of", st_name)
                            #print(data[idx])
                            station_data[st_name]['section_2'] = data[idx]

                        elif "333" in data[idx]:
                            #print("333 gp of", st_name)

                            station_data[st_name]['section_3'] = data[idx]

                        elif "555" in data[idx]:
                            #print("555 gp of", st_name)
                            #print(data[idx])
                            station_data[st_name]['section_5'] = data[idx]

                    else:
                        #print("section-1 data of", st_name)
                        #print(data[idx])
                        station_data[st_name]['section_1'] = data[idx]

                start_bit = end_bit               # make end_bit as start bit
                st = st + 1                           # increase station count
        except:
            print("Error: Sorting and making Total station Data directory fail")

        #print("TOTAL STATION DATA IN SEPERATED FORM:")
        #print(station_data)
        #--------------------------------------------------------------------------

        #---------------------------CALLING FUNCTION------------------------------
        try:
            for s_num in range(1, total_station + 1):
                st_name = 'station_%02d' % s_num
                print("\n \n \nCALLING DECODER FOR ", st_name)

                station_return = decode_station(st_name, station_data[st_name])
                                # calling to station_decoder.py file for decoding
                deco_all = station_return[0]
                deco_ndc = station_return[1]
                all_station_data.append(deco_all)
                all_ndc_form_III.append(deco_ndc)
        except:
            print("Error: Decoding of station data fail")
            decoding_status = False

        else:
            print("Decoding done")
            decoding_status = True

        status_list.append(decoding_status)

        #data_csv_save(all_station_data)
        ndc_form_III_status = data_ndc_III_save(all_ndc_form_III)
        status_list.append(ndc_form_III_status)

    except:
        print("Error: Decoding fail")
    else:
        return status_list

if __name__ == "__main__":
    decoder("/home/nik/Dropbox/IMD/Decoder/Decoder-090117/msg/msg1.txt")