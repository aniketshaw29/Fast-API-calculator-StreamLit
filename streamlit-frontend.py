from cgitb import text
from locale import format_string
import streamlit as st
import json
import requests

st.title("Basic Calculator App")

option=st.selectbox('What operation you want to perform? ',('Addition', 'Subtraction', 'Multiplication', 'Division'))

st.write("Select the number from the slider below")

x = st.slider("X", 0, 100, 20)
y = st.slider("Y", 0, 130, 10)

inputs = {
    "operation": option,
    "x": x,
    "y": y
}

if st.button('calculate'):
    res = requests.post(url="http://localhost:8000/calculate",data=json.dumps(inputs))
    st.subheader(f"response from api = {res.text}")
