import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
# Simple Stock Price App

Shown are the stock closing price  and volume of google!

""")

# https://towardsdatascience.com/how-to-get-stock-data-using-python-c0de1df17e75
#define the ticker symbol
tickerSymbol = 'GOOGL'
#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)
#get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2010-7-31', end='2021-7-31')
# Open	High	Low	Close	Volume	Dividends	Stock Splits


st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)

'''get recommendation data for ticker
tickerData.recommendations'''

'''#get event data for ticker
tickerData.calendar'''

'''#info on the company
tickerData.info'''



