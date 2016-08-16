# -*- coding: utf-8 -*-
"""
Created on Mon Aug 15 20:40:10 2016

@author: Ken
"""

# stocks = ($symbol, $shares, $open_px, $close_px)

stocks = (('APPL', 1000, 251.80, 252.73),
          ('CSCO', 5000, 23.09, 23.74),
          ('GOOG', 500, 489.23, 491.34),
          ('MSFT', 2000, 24.63, 25.44))

class Portfolio(object): 
    def __init__(self):
        self.basket = [] # portfolio instantiated with empty
    
    def add(self, share_data):
        symbol = share_data[0]
        shares = share_data[1]
        open_px = share_data[2]
        close_px = share_data[3]
        self.basket.append((symbol, shares, open_px, close_px))
        # unpack tuple of share_data
    
    def __iter__(self):
        return (i for i in self.basket)
    
    def __getitem__(self, idx):
        return [x for x in self.basket if x[0]==idx]
        # making the class index-able        
    
    def __str__(self):
        for stuple in self.basket:
            stock_data = Stocks(*stuple)
            print(stock_data)
                    

    def quantity(self, ticker):
        if ticker not in [x[0] for x in self.basket]:
            return 'Symbol not found in portfolio'
        qty =  [x[1] for x in self.basket if x[0]==ticker]
        return qty[0]
    
    def close(self, ticker):
        if ticker not in [x[0] for x in self.basket]:
            return 'Symbol not found in portfolio'
        clz = [x[3] for x in self.basket if x[0]==ticker]
        return clz[0]
    
    def opening_px(self, ticker):
        if ticker not in [x[0] for x in self.basket]:
            return 'Symbol not found in portfolio'
        the_open = [x[2] for x in self.basket if x[0]==ticker]
        return the_open[0]
    
    def total_gain(self, ticker):
        # Total monetary gain for the position
        if ticker not in [x[0] for x in self.basket]:
            return 'Symbol not found in portfolio'
        return (self.quantity(ticker)) * (self.close(ticker) - self.opening_px(ticker))

    def gain(self, ticker):
        # intraday gain/loss in share px
        if ticker not in [x[0] for x in self.basket]:
            return 'Symbol not found in portfolio'
        return self.close(ticker) - self.opening_px(ticker)

class Stocks(object):
    def __init__(self, symbol, shares, open_px, close_px):
        self.symbol = symbol
        self.shares = shares
        self.open_px =  open_px
        self.close_px = close_px
    
    def __str__(self):
        return str(self.shares) + ' shares of ' + str(self.symbol) + ' worth ' + str(self.shares * self.close_px)

def Investment(*shares_data):
    return shares_data
    # star unpacking due to nature of data inputs


### For ease of debugging:
#
#del p
#p = Portfolio()
#for stock in stocks:
#    p.add(stock)