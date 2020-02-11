# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 15:12:45 2018

@author: Holt88
"""

from tkinter import *
import Labnetwork_parse_email
import Labnetwork_send_mail
import cpt_function
import temp



def create_window(window_name):
    window=Toplevel()
    window.title("%s" % window_name)
    
    window_width=380
    window_height=330
    screen_width = window.winfo_screenwidth()
    screen_height= window.winfo_screenheight()
    x_cord= int(screen_width/2 - window_width/2)
    y_cord= int(screen_height/2 - window_height/2)
    window.geometry("%sx%s+%s+%s" % (window_width,window_height,x_cord,y_cord))

    spacer=Label(window, text="").grid(row=0, column=0)
    return window

def exit_button(win):
    be=Button(win, 
          text = "Click to\nexit", 
          command = win.destroy, 
          borderwidth=3,
          relief="solid", 
          bg="red",
          fg="white",
          width=20,
          anchor=CENTER, #default value
          justify=CENTER) #default value
    return(be)

def email_parser():
    def update_label_text1():
        label_text1.set(Labnetwork_parse_email.parse_email())
    def update_label_text2():
        label_text2.set(Labnetwork_send_mail.send_csv())
    
    window = create_window("Email Parser")
	
    label_text1=StringVar() 
    label1=Label(window, textvariable=label_text1)
    label1.grid(row=1,column=1)
    label_text1.set("Parse it")
    
    label_text2=StringVar()
    label2=Label(window,textvariable=label_text2)
    label2.grid(row=3,column=1)
    label_text2.set("Send it")
    
    spacer=Label(window, text="").grid(row=0, column=0)
    spacer=Label(window, text="").grid(row=2, column=0)
    spacer=Label(window, text="").grid(row=4, column=0)
    
    parse_button=Button(window,text="Run Parse", command=update_label_text1)
    parse_button.grid(row=1, column=0)
    send_button=Button(window,text="Send the file", command=update_label_text2)
    send_button.grid(row=3,column=0)
    exitbutton=exit_button(window)
    exitbutton.grid(row=5,column=0)


def check_payment_terms():
    def check_terms():
        data_set=cpt_function.check_payment_terms(date_entry.get())
        cia = "Cash in Advance"
        cod = "Cash on Deliver"
        mpt="Mismatched Terms"
        
        label_text1.set(cia + ":"+str(data_set[cia])+"\n"+cod+":"+str(data_set[cod])+"\n"+mpt+":"+str(data_set[mpt]))
        date_entry.delete(0,END)
    
    window=create_window("Check Payment Terms")
    
    spacer=Label(window, text="").grid(row=0, column=0)
    enter_button=Button(window,text="Enter name of file", command = check_terms)
    enter_button.grid(row=1, column=0)
    add_date=StringVar()
    date_entry=Entry(window, textvariable=add_date)
    date_entry.grid(row=1,column=1)
    label_text1=StringVar() 
    label1=Label(window, textvariable=label_text1)
    label1.grid(row=2,column=1)
    label_text1.set("Enter File")
    
    nw_eb=exit_button(window)
    nw_eb.grid(row=10,column=0)

def AMS_Invoice_func():
    
    def check_invoice():
        label_text1.set(temp.runit(date_entry.get()))
        date_entry.delete(0,END)
        
    window = create_window("AMS Invoice Program")
    
    spacer=Label(window, text="").grid(row=0, column=0)
    enter_button=Button(window,text="Enter name of file", command = check_invoice)
    enter_button.grid(row=1, column=0)
    add_date=StringVar()
    date_entry=Entry(window, textvariable=add_date)
    date_entry.grid(row=1,column=1)
    label_text1=StringVar() 
    label1=Label(window, textvariable=label_text1)
    label1.grid(row=2,column=1)
    label_text1.set("Enter File")
    
    nw_eb=exit_button(window)
    nw_eb.grid(row=10,column=0)    
    
def check_pubchem_lcss():
    window=create_window("Check PubChem LCSS")

    nw_eb=exit_button(window)
    nw_eb.grid(row=10,column=0)
   
def scrape_combi_blocks():
    window=create_window("Scrape Combi-Blocks")

    nw_eb=exit_button(window)
    nw_eb.grid(row=10,column=0)    
    
def inventory_database():
    window= create_window("Inventory Database")
    
    nw_eb=exit_button(window)
    nw_eb.grid(row=10,column=0)


    
window = Tk()
window.title("LabNetwork INC")
window_width=400
window_height=400
screen_width = window.winfo_screenwidth()
screen_height= window.winfo_screenheight()
x_cord= int(screen_width/2 - window_width/2)
y_cord= int(screen_height/2 - window_height/2)
window.geometry("%sx%s+%s+%s" % (window_width,window_height,x_cord,y_cord))
label1 = Label(window, text= "LabNetwork Automated Workflows", font = "Broadway 14 bold").grid(row=0,column=0)
spacer=Label(window, text="").grid(row=1, column=0)
email_parser_button=Button(window,text="Run email parser", width=20, bg = "Blue", fg="White", command = email_parser)
email_parser_button.grid(row=2, column=0)
spacer=Label(window, text="").grid(row=3, column=0)
check_payment_terms_button=Button(window, text="Check Payment Terms", width=20, bg='Blue', fg="White", command = check_payment_terms)
check_payment_terms_button.grid(row=4, column=0)
spacer=Label(window, text="").grid(row=5, column=0)
pubchem_button=Button(window,text='PubChem LCSS', width=20, bg="Blue", fg="White", command = check_pubchem_lcss)
pubchem_button.grid(row=6, column=0)
spacer=Label(window, text="").grid(row=7, column=0)
combiblocks_button=Button(window, text="Scrape Combi-Blocks", width=20, bg="Blue", fg="White", command = scrape_combi_blocks)
combiblocks_button.grid(row=8, column=0)
spacer=Label(window, text="").grid(row=9, column=0)
inventory_button=Button(window, text="Inventory Database", width=20, bg='Blue', fg='White', command = inventory_database)
inventory_button.grid(row=10, column=0)
spacer=Label(window, text="").grid(row=11, column=0)

AMS_invoice_button=Button(window, text="AMS Invoice", width=20, bg="Blue", fg="White", command = AMS_Invoice_func)
AMS_invoice_button.grid(row=12,column=0)

spacer=Label(window, text="").grid(row=13, column=0)
exitbutton=exit_button(window)
exitbutton.grid(row=14, column=0)
window.mainloop()