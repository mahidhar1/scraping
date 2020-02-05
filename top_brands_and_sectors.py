# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 09:49:17 2019

@author: Mahidhar
"""

import requests 

def get_data(year, inp_str):
    url = "https://www.interbrand.com/wp-admin/admin-ajax.php"
    payload = {
                'action': inp_str, 
                'study_year': year, 
                'league': 'best-global-brands'
            }
    response = requests.post(url, data = payload)
    print(f"Fetching {inp_str.split('get_')[1].replace('_', ' ')} for {year}. response status code:", response.status_code)
    return response

def get_top_brand_data(year): 
    res = get_data(year, 'get_top_growing_brands_chart_data')
    data_list = res.json()["brands"]
    data_list = list(map(lambda x: (x["brand"], x["delta"]), data_list))
    return data_list
    

def get_sector_comparision_data(year): 
    res = get_data(year, 'get_sector_comparison_chart_data')
    data_list = res.json()["sectors"]
    data_list = list(map(lambda x: (x["sector"], x["value"]), data_list))
    return data_list
    

if __name__ == "__main__":
    
    brands = dict()
    sectors = dict()
    for year in range(2001, 2020, 1):
        brands[year] = get_top_brand_data(year)
        sectors[year] = get_sector_comparision_data(year) 
        