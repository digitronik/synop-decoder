# -*- coding: utf-8 -*-
import csv
#import pandasd as pd


def blank(n):
    n = n.split("-")
    n_len = len(n)
    count = 1
    space = " "
    if n_len > 1:
        for ele in range(int(n[0]), int(n[1])):
            count += 1
    #print count
    return count * space

def header():
    header_string = ""
    for x in range(1,9):
        for i in range(1,10):
            header_string  += str(i)
        header_string += "0"
    return header_string

def data_csv_save(all_data):
    print("Exporting data in CSV file")
    print(all_data)

    with open("Export_Data.csv", "w") as csvfile:
        fieldnames = ['Report_Type',
'Station_Index',
'Station_Name',
'Day',
'Time',
'Wind_Method',
'Wind_Unit',
'Precipitation_amount',
'6RRRt',
'Station_Operation',
'7wwW1W2',
'ht_of_lowest_cloud',
'Visibility',
'Cloud_Total_Amount',
'Wind_Direction',
'Wind_Speed_kmh',
'Air_Temperature',
'Temp_Dew_Point',
'Pressure_Station_Level',
'Pressure_Mean_Sea_Level',
'Weather_Present',
'Weather_Past_W1',
'Weather_Past_W2',
'Cloud_Low_Amount',
'Clound_Low_Form',
'Cloud_Medium_Form',
'Cloud_High_Form',
'Temp_Day_Max',
'Temp_Night_Min',
'Cloud_Direction_Low',
'Cloud_Direction_Medium',
'Cloud_Direction_High',
'Cloud_Type',
'Cloud_Direction',
'Cloud_Elevation_Angle',
'Pressure_Station_Level_Change(24hr)',
'Rainfall(code23)',
'Rainfall_Period',
'Individual_Layer_Cloud_Amount',
'Individual_Layer_Cloud_Form',
'Individual_Layer_Cloud_height',
'Rainfall(24hr)',
'Rainfall(SeasonalTotal)',
'Squal_Wind_Direction',
'Squal_Wind_Force_Max',
'Squall_Nature',
'Squall_Time']

        data_writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
        data_writer.writeheader()

        for station_data in all_data:
            data_writer.writerow(station_data)
    csvfile.close()

def data_ndc_III_save(data):
    form_III_fiels = ["1-5", "6-7", "8-9", "10-11", "12-13", "14-18",
         "19-23", "24-26", "27-29", "30-32", "33-35", "36-38", "39-40",
         "41-43", "44-45", "46-47", "48", "49", "50", "51", "52", "53",
         "54", "55", "56", "57", "58", "59", "60", "61-62", "63-66",
         "67-69", "70-71", "72", "73", "74-76", "77", "78-79", "80"]

    try:
        f = open("NDC-FORM-III(csv).txt","w+")
        f1 = open("NDC-FORM-III.txt","w+")

        f1.write("%s \r\n" %header()) # ADDING HEADER TO ANALIZE
        for di in data:
            line = ""
            line_string = ""

            for field in form_III_fiels:

                if field in di.keys():
                    line += di[field]
                    line_string += di[field]
                    if field != "80":
                        line = line + ","
                else:
                    line_string += blank(field)
                    #print field
                    if field != "80":
                        line = line + ","
            f.write("%s \r\n" %line)
            f1.write("%s \r\n" %line_string)
            print("%s \r\n" %line_string)
        f.close()
        f1.close()
    except:
        print("Error: Exporting NDC Form-III fail")
        return False
    else:
        print("NDC Form-III generated ready to save")
        return True


if __name__ == "__main__":
    test = [{'Clound_Low_Form': 'Cumulonimbus, the summits of which, at least partially, lack sharp outlines, but are neither clearly fibrous (Cirriform) nor in the form of an anvil; Cumulus, Stratocumulus or Stratus may also be present', 'Pressure_Mean_Sea_Level': '0079', 'Report_Type': 'SYNOP report', 'Rainfall(code23)': '038', 'Squal_Wind_Direction': 'E', 'Wind_Unit': 'knots', 'Time': '03', '6RRRt': 'Include in section 3', 'Wind_Method': 'anemometer', 'Cloud_High_Form': 'Cirrus, Cirrocumulus and Cirrostratus are invisible owing to darkness, fog, blowing dust or sand or other similar phenomena, or more often, because of the presence of a continuous layer of lower clouds', 'Weather_Past_W1': 'Rain', 'Weather_Past_W2': 'Cloud covering more than half of the sky throughout the appropriate period.', 'Air_Temperature': '22.4', 'Temp_Night_Min': 20.1, 'Rainfall(SeasonalTotal)': '0593', 'Squal_Wind_Force_Max': ' ', 'Station_Name': 'North Lakhimpur', 'Station_Operation': 'Manned', 'Wind_Direction': 'NE', 'Rainfall(24hr)': '0384', 'Temp_Dew_Point': '22.4', 'Squall_Nature': 'Line squall.', 'Squall_Time': '2 to 3 hours ago', 'Cloud_Low_Amount': '6 Okta', 'Pressure_Station_Level_Change(24hr)': '015', 'Cloud_Total_Amount': '8 Okta', 'Visibility': '2000 m', 'Day': '17', '7wwW1W2': 'Included', 'Station_Index': '42309', 'ht_of_lowest_cloud': '200-299', 'Weather_Present': 'Haze', 'Wind_Speed_kmh': '7.41', 'Rainfall_Period': '/', 'Cloud_Medium_Form': 'Altostratus, the greater part of which is sufficiently dense to hide the sun (or moon), or Nimbostratus.'}]

    data_save(test)