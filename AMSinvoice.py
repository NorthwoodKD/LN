# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import PyPDF2
import os
import LabNetwork_Inventory_Database as lnd
import AMSinvoiceFunctions as AMS

us = lnd.DataBase('LabNetwork Database.db')
us.connect_to_db()
us.connect_cursor()

os.chdir("C:/Users/Holt88/Desktop")
   
pdfFileObj = open("Invoice# 20000324.pdf","rb")
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

#us.lnidcas_table_add_record("LN02188200","1363380-81-7")

#us.products_table_add_record("LN01373952","WXCD00909811")

pn=pdfReader.numPages

print("Hello\n\nThe attached invoice is for the following LNIDs:\n")

for i in range(pn):
    pageObj=pdfReader.getPage(i)
    text = pageObj.extractText()
    text = text[::-1]
    casnum, asecnum = AMS.findCASandASEC(text)
    for i in casnum:
        t =  us.lnidcas_table_search_by_cas(i)
        print(t)
    for i in asecnum:
        t = us.products_table_search_by_productID(i)
        print(t)

for i in range(pn):
    pageObj=pdfReader.getPage(i)
    text = pageObj.extractText()
    ret = AMS.findWuxi(text) 
    for r in ret:
        t = us.products_table_search_by_productID(r)
        print(t)

for i in range(pn):
    pageObj=pdfReader.getPage(i)
    text = pageObj.extractText()
    ret = AMS.findChemSupply(text) 
    for r in ret:
        t = us.products_table_search_by_productID(r)
        print(t)

print("\nThanks\nZac")

us.commit_to_db()
us.close_db()   

