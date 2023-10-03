import streamlit as st 
import yfinance as yf
import datetime 
st.title("Welcome to stockviz")
ticker_symbol=st.text_input("type your symbol",value='AAPL')

ticker_Data = yf.Ticker(ticker_symbol)


dc1,dc2= st.columns(2)
with dc1:
    start = st.date_input("Start Date", datetime.date(2019, 7, 6))
with dc2:
    end = st.date_input("End Date", datetime.date(2020, 7, 6))

ticker_df = ticker_Data.history(period="1d",start=start,end=end)


col1, col2 = st.columns(2)

with col1:
    st.write("""
## Daily CLose Price chart
""")
    st.line_chart(ticker_df, y="Close")

with col2:
    st.write("""
## Daily Volume  chart
""")
    st.line_chart(ticker_df, y="Volume")









