import streamlit as st
import pandas as pd
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier
import pickle

from streamlit.runtime.metrics_util import F

st.write("""
# Finding the largest among the 3 given numbers

This app finds the largest number among the 3 given numbers
""")
#Get Input

st.header('Select three numbers')

def user_input_features():
    first_number = st.number_input("First Number", -1.797e+308, 1.797e+308, step=1.0)
    second_number = st.number_input("Second Number", -1.797e+308, 1.797e+308, step=1.0)
    third_number = st.number_input("Third Number", -1.797e+308, 1.797e+308, step=1.0)
    return first_number, second_number, third_number

# Call the function to get user input
num1, num2, num3 = user_input_features()

# Calculate the largest number
largest_number = max(num1, num2, num3)

# Display the result
st.write(f"The largest number among the three is: {largest_number}")