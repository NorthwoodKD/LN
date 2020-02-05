# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 08:36:49 2020

@author: holtz
"""
from tkinter import *
import database_testing 

class DataBaseGui:
    
    def __init__(self, root):
        self.root = root
        self.test_database = database_testing.DataBase("test_database.db")

        root.title("LN Database GUI")
        
        # command search master table for products with 'in_stock' == 'Y'
        self.product_search_button = Button(root, text="search product availability", command = self.product_search)
        self.product_search_button.pack()
        
        #command needs to change 'in_stock' to 'N'
        #command needs to add shipped_month, shipped_day, shipped_year, customer_name, 
        #customer_po, lnpo, order_numder, tracking, in_process, value
        self.enter_order_button = Button(root, text="IMPORT new order")
        self.enter_order_button.pack()
        
        #command return a view of 'in_process' == 'Y' and shipped month > 0 
        self.view_inprocess_button = Button(root, text="View orders in process")
        self.view_inprocess_button.pack()
        
        #command takes the return of view 'in_process' and creates the csv files
        #required to update the inventory on LN.com
        self.update_inventory_button = Button(root, text="Update Inventory")
        self.update_inventory_button.pack()
        
        #command takes the results of 'in_process' and changes value from 'Y' to 'N'
        self.advance_order_button = Button(root, text="Advance orders")
        self.advance_order_button.pack()
        
        self.close_button = Button(root,text="close", command=self.root.destroy)
        self.close_button.pack()
        
    def connect_to_database(self):
        self.test_database.connect_to_db()
        self.test_database.connect_cursor()

    def product_search(self):
        def add_to_order():
            self.label_text1.set(self.chkValue.get())
        def search_database():
            self.pn = self.test_database.search_master_by_productid(self.pn_entry.get())
            if self.pn != None:
                for i in range(len(self.pn)):
                    self.chkValue=BooleanVar()
                    self.chkValue.set(False)
                    self.s = Checkbutton(self.window, text=self.pn[i], var=self.chkValue)
                    self.s.pack()
                
                #self.pn_entry.delete(0,END)
                self.make_order = Button(self.window, text = "Add to order", command=add_to_order)
                self.make_order.pack()
            else:
                self.label_text1.set(self.pn_entry.get() + " is not available")
                self.pn_entry.delete(0,END)
        def close_window():
            self.window.destroy()
            self.test_database.close_db()
        
        self.connect_to_database()
        self.window=Toplevel()
        self.window.title("Product Search")
        self.product_number = StringVar()
        self.pn_entry=Entry(self.window, textvariable=self.product_number)
        self.pn_entry.pack()
        self.check_button=Button(self.window, text="Check Product", command=search_database)
        self.check_button.pack()
        self.label_text1=StringVar() 
        self.label1=Label(self.window, textvariable=self.label_text1)
        self.label1.pack()
        self.close_button = Button(self.window,text="close", command=close_window)
        self.close_button.pack()


master = Tk()
gui = DataBaseGui(master)
master.mainloop()



#test_database.commit_to_db()
#