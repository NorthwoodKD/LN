# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 15:00:04 2020

@author: holtz
"""

import sqlite3

class DataBase:
    
    def __init__(self,database_name):
        self.database_name = database_name
        self.conn = None
        self.c = None
        
    def connect_to_db(self):
        self.conn =  sqlite3.connect(self.database_name)
        print('connected to %s' % self.database_name)
    
    def connect_cursor(self):
        self.c = self.conn.cursor()
        print("cursor selected")
        
    def commit_to_db(self):
        self.conn.commit()
        print("updates committed")
    
    def close_db(self):
        self.conn.close()
        print("connection to %s was closed" % self.database_name)
        
    def create_master_table(self):
        self.c.execute('''CREATE TABLE IF NOT EXISTS master
                       (cab_id TEXT NOT NULL,
                        box_id TEXT NOT NULL,
                        product_id TEXT NOT NULL,
                        lot_id TEXT NOT NULL,
                        size TEXT NOT NULL,
                        supplier TEXT NOT NULL,
                        in_stock TEXT NOT NULL
                        )''')
        print("Table 'master' was created")
        
    def create_sales_table(self):
        self.c.execute('''CREATE TABLE IF NOT EXISTS sales
                        (product_id TEXT NOT NULL,
                        size TEXT NOT NULL,
                        shipped_month INT NOT NULL,
                        shipped_day INT NOT NULL,
                        shipped_year INT NOT NULL,
                        customer_name TEXT NOT NULL,
                        customer_po TEXT NOT NULL,
                        ln_po TEXT NOT NULL,
                        order_number INT NOT NULL,
                        tracking_number TEXT NOT NULL,
                        in_process TEXT NOT NULL,
                        value INT NOT NULL
                        )''')
        print("Table 'sales' was created")

    def add_record_master(self, cab_id,box_id, product_id, lot_id, size, supplier, in_stock):
        self.c.execute('INSERT INTO master VALUES (?,?,?,?,?,?,?)', (cab_id,box_id, product_id, lot_id, size, supplier, in_stock))  
    
    def add_record_sales(self,product_id, size, shipped_month, shipped_day, shipped_year, customer_name, customer_po, lnpo, order_numder, tracking, in_process, value):
        self.c.execute('INSERT INTO sales VALUES (?,?,?,?,?,?,?,?,?,?,?,?)', (product_id, size, shipped_month, shipped_day, shipped_year, customer_name, customer_po, lnpo, order_numder, tracking, in_process, value))


    def search_master_by_productid(self, product_id):
        self.c.execute("SELECT cab_id,box_id,lot_id,size FROM master WHERE product_id ='%s' and in_stock ='Y'" % product_id)
        t = self.c.fetchall()
        if len(t)==0:
            return None
        else:
            a=[]
            for row in t:
                cab_id=row[0]
                box_id=row[1]
                lot_id=row[2]
                size=row[3]
                a.append(product_id+" "+lot_id+" "+size)
            return a

    def build_database(self, initial_file):
        f = open(initial_file,"r")
        f= [a.split(',') for a in f]
        for i in range(1,len(f)-1):
            a = f[i]
            value = a[20].replace("\n","")
            if len(a[7])>0:
                print("sales")
                test_database.add_record_sales(a[3],a[5],a[7],a[8],a[9],a[10],a[11],a[12],a[14],a[15],a[18], value)
            else:
                print('master') 
                test_database.add_record_master(a[0],a[2],a[3],a[4],a[5],a[7],'Y')
        