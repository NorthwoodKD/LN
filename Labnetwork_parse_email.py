#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  9 13:48:07 2018

@author: zac
"""

import imaplib
import email
import csv

def parse_email():
    FROM_EMAIL = "emailparserforryan@gmail.com"
    FROM_PW = "RyanGorman123"
    IMAP_SERVER = "imap.gmail.com"
    
    # header and body are multipart. If we just needed the header we would not need this
    def getBody(msg):
        if msg.is_multipart():
            return getBody(msg.get_payload(0))
        else:
            return msg.get_payload(None,True)
        
    def search(key,value,mail):
        result, data = mail.search(None,key,'"{}"'.format(value))
        return data    
    
    def get_emails(return_bytes):
        msgs =[]
        for num in return_bytes[0].split():
            typ, data = mail.fetch(num, '(RFC822)')
            msgs.append(data)
            #mail.store(num, '+FLAGS', '\\Deleted')
    		#mail.expunge() was causing errors
            #mail.expunge()
        return msgs
    
    mail = imaplib.IMAP4_SSL(IMAP_SERVER)
    mail.login(FROM_EMAIL,FROM_PW)
    mail.select('inbox')
    
    #This just grabs the emails (in bytes) from a specific sender. You can set this to all 
    msgs = get_emails(search("FROM","contact@labnetwork.com",mail))
    
    data = []
    
    #This cleans out the html and appends to data as a single line seperated by ';@;'
    #so that it is easy to split again
    
    for msg in msgs:
        raw = str(getBody(email.message_from_bytes(msg[0][1])))
        raw = raw.replace("\\r\\n\\r","")
        raw = raw.replace("\\r","")
        raw = raw.split("\\n")
        se=raw[2].split(": ")[1]
        cn=raw[13].split(": ")[1]
        fn = raw[8].split(": ")[1]
        ln = raw[9].split(": ")[1]
        em = raw[10].split(": ")[1]
        ph = raw[11].split(": ")[1]
        data.append(se+";@;"+cn+";@;"+fn+";@;"+ln+";@;"+em+";@;"+ph)
    	
    #this just writes out to a file
    outputFile = open("ZoHoUpLoaDs.csv",'w',newline="")
    outputWriter= csv.writer(outputFile)
    for record in data:
        outputWriter.writerow(record.split(";@;"))
    outputFile.close()

    return("Parsed")
