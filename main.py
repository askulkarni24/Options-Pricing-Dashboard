#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 14 12:07:15 2023

@author: abhi
"""

import ticker_data
import webpage
import graph
    
if __name__ == "__main__":
    
    stock = ticker_data.TickerData()
    
    wbpg = webpage.Webpage()
    wbpg.layout(stock.get_ticker_list(), stock.get_ticker_data())
    wbpg.server_run(8060)
