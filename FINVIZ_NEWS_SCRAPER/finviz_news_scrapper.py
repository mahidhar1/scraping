# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 22:31:51 2020

@author: Mahidhar
"""

import bs4 as bs
import requests
import pandas as pd
import re


def get_news(tables):
    news = tables[3].find_all("tr")
    data_news = []
    for row in news:
        td = row.find_all("td")
        d = [el.text for el in td] + [td[-1].find_all('a')[0]["href"]]
        data_news.append(d)
    
    return pd.DataFrame(data_news)


def get_blogs(tables):
    blogs = tables[4].find_all("tr")
    data_blogs = []    
    for row in blogs:
        td = row.find_all("td")
        d = [el.text for el in td] + [td[-1].find_all('a')[0]["href"]]
        data_blogs.append(d)
    return pd.DataFrame(data_blogs)


def find_data_source_news(link):
    m = re.findall(r'(?<=feeds.)\w+(?<=.)|(?<=www.)\w+(?<=.)', link)
    return m[0]

def find_data_source_blogs(link):
    src = link.split("/")[2:]
    if src[0] == "feedproxy.google.com":
        return src[2]
    else: 
        return src[0].split(".")[0]
   
    

if __name__ == "__main__":
    url = r"https://www.finviz.com/news.ashx"
    r = requests.get(url)
    soup = bs.BeautifulSoup(r.content)

    raw_data = soup.findAll("div", {"class": "news"})
    tables = raw_data[0].find_all("table")
    
    data_news = get_news(tables)
    data_blogs = get_blogs(tables)
    
    data_news[0] = data_news[3].apply(lambda x: find_data_source_news(x))
    data_blogs[0] = data_blogs[3].apply(lambda x: find_data_source_blogs(x))
    
    data_news.columns = ["source", "time/date", "headline", "url"]
    data_blogs.columns = ["source", "time/date", "headline", "url"] 
        
    