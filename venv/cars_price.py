import streamlit as st
import pandas as pd
import numpy as np

cars_df = pd.read_csv(r"C:\Users\Dell\Downloads\cars24-car-price-cleaned.csv")

st.title("Car Resale Price Prediction")
st.dataframe(cars_df.head())
