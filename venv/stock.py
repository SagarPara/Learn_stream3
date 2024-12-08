import streamlit as st
import yfinance as yf
import datetime


st.title("Stock Price Analyser!")



#Input date _ start code

col1, col2, col3 = st.columns(3)

#INPUT company name
with col1:
    stock_name = st.text_input("which stock you want to analyse", "MSFT")
    ticker_data = yf.Ticker(stock_name)


with col2:
    start_date = st.date_input("Please enter Starting Date",
                           datetime.date(2023,12,1))
with col3:
    end_date = st.date_input("Please enter Ending Date",
                           datetime.date(2024,12,31))



ticker_df = ticker_data.history(period="1d", start=start_date, end=end_date)
#Input date _ end code



st.dataframe(ticker_df)

st.subheader("Here is the raw day wise stock price")
st.dataframe(ticker_df.head())

st.subheader("Price movement over time")
st.line_chart(ticker_df["Close"])

st.subheader("Volumes over time")
st.line_chart(ticker_df["Volume"])