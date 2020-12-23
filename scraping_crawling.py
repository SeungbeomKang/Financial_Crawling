# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 19:20:47 2020

@author: 강승범
"""

import pandas as pd
from bs4 import BeautifulSoup

from urllib.request import urlopen

url = 'https://finance.naver.com/item/sise_day.nhn?code=068270&page=1'

with urlopen(url) as doc:
    html = BeautifulSoup(doc, 'lxml')
    pgrr = html.find('td', class_='pgRR')
    s = str(pgrr.a['href']).split('=')
    last_page = s[-1]
    
df = pd.DataFrame()
sise_url = 'https://finance.naver.com/item/sise_day.nhn?code=068270'

for page in range(1, int(last_page)+1):
    page_url = '{}&page={}'.format(sise_url, page)
    df = df.append(pd.read_html(page_url, header=0)[0])
    
df = df.dropna()

