import streamlit as st

st.title("Hey, Virtual, I am learning Streamlit!")

st.header("My custom header")

st.write("learning stream for the second time")

agree = st.checkbox("I agree with Mohit")

if agree:
    st.write("Great!")

genre = st.radio("what's your fav movie genre?", ["Comedy", "Drame", "Romance"])

if genre == "Comedy":
    st.write("Excited...Haha")
else:
    st.write("Cool")

