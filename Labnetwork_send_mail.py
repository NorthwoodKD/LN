#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 16:02:53 2018

@author: zac
"""

import smtplib
import email.mime.multipart
import email.mime.text

def send_csv():
    SEND_MAIL_ADDRESS = "emailparserforryan@gmail.com"
    SEND_PW = "RyanGorman123"
    TO_MAIL = 'Ryan.Gorman@labnetwork.com'
    SMTP_SERVER = "smtp.gmail.com"
    
    mail_to_send = email.mime.multipart.MIMEMultipart()
     
    mail_to_send['From'] = SEND_MAIL_ADDRESS 
    mail_to_send['To'] = TO_MAIL
    mail_to_send['Subject'] = "Your ZoHo upload sheet"
    body = "Here is the test file for your time saving enjoymente. Please share any feeback."
    mail_to_send.attach(email.mime.text.MIMEText(body, 'plain'))
    filename = "ZoHoUpLoaDs.csv"
    attachment = open("ZoHoUpLoaDs.csv", "rb")
    p = email.mime.base.MIMEBase('application', 'octet-stream')
    p.set_payload((attachment).read())
    email.encoders.encode_base64(p)
    p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
    mail_to_send.attach(p)
     
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(SEND_MAIL_ADDRESS, SEND_PW)
    txt = mail_to_send.as_string()
    s.sendmail(SEND_MAIL_ADDRESS, TO_MAIL, txt)
    s.quit()
    
    return("Sent")