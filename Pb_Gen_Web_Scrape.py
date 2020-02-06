# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 15:14:43 2020

@author: Holt88
"""

import bs4 as bs
import urllib.request

source = urllib.request.urlopen("https://worldadc-europe.com/whats-on/speakers/")
soup = bs.BeautifulSoup(source,'lxml')

wwn = soup.find_all("div",{"class":"content-wrapper"})

w = [x.get_text() for x in wwn]
w = [a.replace("\n",";").split(";") for a in w]


def export_for_hunter(file_name, dataset):
    '''
    DOCSTRING: Write out a txt file 
    IN: LIST
    OUT: FILE
    '''
    file = open(file_name, "w")
    file.write("Name;Position;Company\n")
    for a in dataset:
        file.write(a[1].strip() + ";" + a[2].strip() + ";" + a[3].strip() + "\n")   
    file.close()

