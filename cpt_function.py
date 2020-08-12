# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 11:46:58 2018

@author: Holt88
"""

import xlrd

def check_payment_terms(file_name):
    data={}
    
    def cash_in_advance():
        cia = "Cash in Advance"
        c=[]
        for row in range(sheet.nrows):
            if sheet.cell_value(row,4) == "Cash in Advance               ":
                c.append(sheet.cell_value(row,1))
        data[cia] = set(c)
       
    def cash_on_delivery():
        cod = "Cash on Deliver"
        c =[]
        for row in range(sheet.nrows):
            if sheet.cell_value(row,4) == "Cash on Delivery              ":
                c.append(sheet.cell_value(row,1))
        data[cod]=set(c)
    
    def mismatch_payment_terms():
        mpt="Mismatched Terms"
        c=[]
        for row in range(1,sheet.nrows):
            for col in range(sheet.ncols):
                opt = sheet.cell_value(row,3)
                cmpt = sheet.cell_value(row,5)
            if opt != cmpt:
                c.append(sheet.cell_value(row,1)+":"+sheet.cell_value(row,10))
        data[mpt]=set(c)
    
    file_name=file_name + ".xls"
    file = xlrd.open_workbook(file_name)
    sheet = file.sheet_by_name("Sheet1")
    cash_in_advance()
    cash_on_delivery()
    mismatch_payment_terms()
    return(data)