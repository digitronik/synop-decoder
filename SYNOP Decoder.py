# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#    Platform        : GUI Decoder file
#    Project Name    : SYNOP DATA DECODER
#    Author          : Nikhil Dhandre
#    Start Date      : 03-07-2016
#    Last Modified   : 09-01-2017
#------------------------------------------------------------------------------


#--------------------------import library files--------------------------------
from Tkinter import *
import tkFont
from tkFileDialog import askopenfilename, asksaveasfilename
from PIL import ImageTk, Image
import datetime
from main import *
from export_data_csv_file import *
#------------------------------------------------------------------------------
decoding_status = None
msg_file_status = None
ndc_form_III_status = None
#----------------------------GUI Initialization--------------------------------

root = Tk()
root.title("SYNOP Decoder")
#root.geometry("600x450")
#root.geometry("600x450")
# we are using pack method
helv36 = tkFont.Font(family='Helvetica', size=12, weight='bold')
#------------------------------------------------------------------------------

#------------------------------Fuction Defining--------------------------------


#-----------Clock fuction------------------------------------------------------
def tick():
    global time1

    #time2 = time.strftime('%H:%M:%S')
    utc_time = datetime.datetime.utcnow()
    time2 = utc_time.strftime("%H:%M:%S")

    # if time string has changed, update it
    if time2 != time1:
        time1 = time2
        clock.config(text=time2 + " UTC")
    clock.after(200, tick)


#------------------------file name reading fuction-----------------------------
def o_file():
    try:
        print("Opening file")
        msg = askopenfilename()     # fuction for opening file
        msg = str(msg)
        print(msg)
        status_list  = decoder(msg)

        global decoding_status
        decoding_status = status_list[1]
        global msg_file_status
        msg_file_status = status_list[0]
        global ndc_form_III_status
        ndc_form_III_status = status_list[2]
    except:
        print("Error: Opening file and decoding fail")

#------------------------file Saving fuction-----------------------------------
def s_CVC_file():
    save_filename = asksaveasfilename(filetypes = [('CSV', '.csv'),('all files', '.*') ],defaultextension=".csv")
    if save_filename:
        print("Save file name is - ", save_filename )
        csv_save(save_filename)

def s_NDC_III_comma():
    save_filename = asksaveasfilename(filetypes = [('Text', '.txt'),('all files', '.*') ],defaultextension=".txt")
    if save_filename:
        print("Save file name is - ", save_filename )
        ndc_III_save_comma(save_filename)


def s_NDC_III():
    save_filename = asksaveasfilename(filetypes = [('Text', '.txt'),('all files', '.*') ],defaultextension=".txt")
    if save_filename:
        print("Save file name is - ", save_filename )
        ndc_III_save(save_filename)
#------------------------------------------------------------------------------




#--------------------------Main loop Start-------------------------------------

#----------------- logo of IMD-------------------------------------------------
img_l = ImageTk.PhotoImage(Image.open("figures/IMDLogo2.png"))
#img_l = img_l.resize((250,250), Image.ANTIALIAS )
panel_l = Label(root, image = img_l)
panel_l.pack()

#-------------------blank label------------------------------------------------
bl_1=Label(root, text='').pack(fill=X)


#-----------------clock--------------------------------------------------------
time1 = ''    # variable for saving current time
clock = Label(root, font=('times', 25, 'bold'),fg="blue")
clock.pack()
tick()    # calling fuction

#-------------------blank label------------------------------------------------
bl_2=Label(root, text='').pack(fill=X)


#---------------- open msg file button------------------------------------------
open_button = Button(root,
    text="Open Message",
    font=helv36,
    padx=55,
    pady=10,
    fg="green",
    command=o_file)
open_button.pack()
#-------------------  label in  --------------------------------------------

bl_3 = Label(root, text='').pack(fill=X)

#---------------- Save file button---------------------------------------------
save_button = Button(root,
    text="Decoded CSV",
    font=helv36,
    padx=57,
    pady=10,
    fg="red",
    command = s_CVC_file)
save_button.pack()

#---------------- Export NDC-Form-III file button ----------------------------
ndc_III_button = Button(root,
    text="NDC FORM-III",
    font=helv36,
    padx=59,
    pady=10,
    fg="blue",
    command = s_NDC_III)
ndc_III_button.pack()

#---------------- Export NDC-Form-III file button ----------------------------
ndc_III_button = Button(root,
    text="NDC FORM-III (csv)",
    font=helv36,
    padx=38,
    pady=10,
    fg="blue",
    command = s_NDC_III_comma)
ndc_III_button.pack()


#-------------------blank label------------------------------------------------
bl_4 = Label(root, text='').pack(fill=X)

#-------------------blank label------------------------------------------------
bl_5 = Label(root, text='').pack(fill=X)

#-------------------blank label------------------------------------------------
bl_6 = Label(root, text='').pack(fill=X)

#-------------------blank label------------------------------------------------
bl_7=Label(root, text='').pack(fill=X)


#------------------------------------------------------------------------------
root.mainloop()
#----------------------------sript end-----------------------------------------