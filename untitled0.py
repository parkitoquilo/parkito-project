



"""%%writefile app.py

import streamlit as st
"""

set.title("My First Python Web App")

st.write("Welcome! This app was build entirely on a Chromebook")

st.header("currency converter")

ksh_amount = st.number_input("Enter amount in Kenyan Shillings(Ksh):",min_value=0.0, step=1.0)

usd_amount = ksh_amount / 130.0

st.success(f"That is approximately **${usd_amount:.2f} USD**")

st.header("Quick Math Challenge")

st.write("Since you love math, solve this:")

user_answer = st.number_input("What is 15 multiplied by 6?", min_value=0, step=1)

if user_answer == 90:
    st.balloons()
    st.success("correct! outstanding job!")
elif user_answer != 0:
    st.error("Not quite right yet. Try again!")


