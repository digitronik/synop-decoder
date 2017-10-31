# -*- coding: utf-8 -*-
import csv


def csv_save(save_filename):
    print save_filename

    with open("Export_Data.csv", 'rt') as f_in, open(save_filename, 'wt') as f_out:
        headings = next(iter(csv.reader(f_in)))
        csv.writer(f_out).writerow(headings)
        csvout = csv.DictWriter(f_out, fieldnames=headings)
        for d in csv.DictReader(f_in,fieldnames=headings):
            csvout.writerow(d)


def ndc_III_save_comma(save_filename):
    print save_filename
    with open("NDC-FORM-III(csv).txt", 'r') as f_in, open(save_filename, 'w') as f_out:
        try:
            data_in = f_in.read()
            f_out.write(data_in)
        except:
            print("Error in saving NDC-III file")
        finally:
            f_in.close()
            f_out.close()


def ndc_III_save(save_filename):
    print save_filename
    with open("NDC-FORM-III.txt", 'r') as f_in, open(save_filename, 'w') as f_out:
        try:
            data_in = f_in.read()
            f_out.write(data_in)
        except:
            print("Error in saving NDC-III file")
        finally:
            f_in.close()
            f_out.close()
if __name__ == "__main__":
    csv_save("nik.csv")