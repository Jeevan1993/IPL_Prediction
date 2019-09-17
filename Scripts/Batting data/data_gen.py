#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import io
import re 
import csv
import numpy as np
fh = io.open("README.txt","r")
links = fh.readlines()
count=0

match_ids=[]
for link in links :
    count+=1
    numbers = re.findall('\d+',link) 
    if len(numbers)>0:
        for i in range(len(numbers)):
            numbers[i]=int(numbers[i])
        numbers = max(numbers)
        if numbers>33598:
            match_ids.append(numbers)
    
len(match_ids)
match_ids[-10:]

np.save('IPL_2008-2019_match_ids',match_ids)

