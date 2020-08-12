# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import PyPDF2
import os

os.chdir("C:/Users/holtz/Desktop")

def findCas(pagetext):
    for i in range(len(text)):
        if text[i].isdigit():
            ret = text[i]
            if text[i+1]=="-":
                ret = ret+text[i+1]
                if text[i+2].isdigit():
                    ret = ret+text[i+2]
                    if text[i+3].isdigit():
                        ret = ret+text[i+3]
                        if text[i+4]=="-":
                            ret = ret+text[i+4]
                            if text[i+5].isdigit():
                                ret = ret+text[i+5]
                                if text[i+6].isdigit():
                                    ret = ret+text[i+6]
                                    if text[i+7].isdigit():
                                        ret = ret+text[i+7]
                                        if text[i+8].isdigit():
                                            ret = ret+text[i+8]
                                            if text[i+9].isdigit():
                                                ret = ret+text[i+9]
                                                if text[i+10].isdigit():
                                                    ret = ret+text[i+10]
                                                    if text[i+11].isdigit():
                                                        ret = ret+text[i+11]
                                                        
            if len(ret)>4:
                print(ret[::-1])                    

def findWuxi(text):
    for i in range(len(text)):
        ret = ""
        if text[i] == "W":
            if text[i+1] == "X":
                if text[i+2] == "C":
                    if text[i+3] == "D":
                        ret="WXCD"
                        if text[i+4].isdigit():
                            ret = ret + text[i+4]
                            if text[i+5].isdigit():
                                ret = ret + text[i+5]
                                if text[i+6].isdigit():
                                    ret = ret + text[i+6]
                                    if text[i+7].isdigit():
                                        ret = ret + text[i+7]
                                        if text[i+8].isdigit():
                                            ret = ret + text[i+8]
                                            if text[i+9].isdigit():
                                                ret = ret + text[i+9]
                                                if text[i+10].isdigit():
                                                    ret = ret + text[i+10]
                                                    if text[i+11].isdigit():
                                                        ret = ret + text[i+11]
            if len(ret)>4:
                print(ret)                                                         

def findCASandASEC(text):
    cas = []
    asec = []
    for i in range(len(text)):
        if text[i].isdigit():
            ret = text[i]
            if text[i+1]=="-":
                ret = ret+text[i+1]
                if text[i+2].isdigit():
                    ret = ret+text[i+2]
                    if text[i+3].isdigit():
                        ret = ret+text[i+3]
                        if text[i+4]=="-":
                            ret = ret+text[i+4]
                            if text[i+5].isdigit():
                                ret = ret+text[i+5]
                                if text[i+6].isdigit():
                                    ret = ret+text[i+6]
                                    if text[i+7].isdigit():
                                        ret = ret+text[i+7]
                                        if text[i+8].isdigit():
                                            ret = ret+text[i+8]
                                            if text[i+9].isdigit():
                                                ret = ret+text[i+9]
                                                if text[i+10].isdigit():
                                                    ret = ret+text[i+10]
                                                    if text[i+11].isdigit():
                                                        ret = ret+text[i+11]
                                                        
            if len(ret)>4:
                if text[i+len(ret)] =='C':
                    if text[i+len(ret)+1]=='E':
                        if text[i+len(ret)+2]=='S':
                            if text[i+len(ret)+3]=='A':
                                ret = ret + 'CESA'
                                asec.append(ret[::-1])
                else:
                    cas.append(ret[::-1])
    return cas,asec

def runit(file_name):
                   
    pdfFileObj = open(file_name,"rb")
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    pn=pdfReader.numPages

    for i in range(pn):
        pageObj=pdfReader.getPage(i)
        text = pageObj.extractText()
        text = text[::-1]
        casnum,asecnum = findCASandASEC(text)
        for c in casnum:
            print(c)
        for a in asecnum:
            print(a)

    for i in range(pn):
        pageObj=pdfReader.getPage(i)
        text = pageObj.extractText()
        findWuxi(text)  

