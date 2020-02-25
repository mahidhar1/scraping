# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 22:31:51 2020

@author: Mahidhar
"""

import bs4 as bs
import requests
import pandas as pd



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


if __name__ == "__main__":
    url = r"https://www.finviz.com/news.ashx"
    r = requests.get(url)
    soup = bs.BeautifulSoup(r.content)

    raw_data = soup.findAll("div", {"class": "news"})
    tables = raw_data[0].find_all("table")
    
    data_news = get_news(tables)
    data_blogs = get_blogs(tables)
    
        
    
    