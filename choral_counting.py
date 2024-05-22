import numpy as np
import pandas as pd
import streamlit as st

st.title("RCOE Choral Counting App")
st.sidebar.image("logo.jpg", width=150)
st.sidebar.title("Settings")
num_cols = st.sidebar.slider(
    label="Number of columns",
    value=5,
    min_value=1,
    max_value=10,
    step=1,
    key="num_cols",
)
num_rows = st.sidebar.slider(
    label="Number of rows", value=5, min_value=1, max_value=10, step=1, key="num_rows"
)
mode = st.sidebar.radio(
    label="Mode", options=["Integer", "Decimal"], index=0, key="mode"
)
if mode == "Integer":
    start_num = st.sidebar.number_input(
        label="Starting number",
        value=1,
        min_value=-1000,
        max_value=1000,
        step=1,
        key="start_num",
    )
    increment = st.sidebar.number_input(
        label="Count by:",
        value=1,
        min_value=-1000,
        max_value=1000,
        step=1,
        key="increment",
    )
elif mode == "Decimal":
    start_num = st.sidebar.number_input(
        label="Starting number",
        value=1.0,
        min_value=-1000.0,
        max_value=1000.0,
        step=0.01,
        key="start_num",
    )
    increment = st.sidebar.number_input(
        label="Count by:",
        value=1.0,
        min_value=-1000.0,
        max_value=1000.0,
        step=0.01,
        key="increment",
    )
direction = st.sidebar.select_slider(
    label="Direction", options=["Left to right", "Top to bottom"], key="direction"
)

total_numbers = num_cols * num_rows

numbers = [start_num + i * increment for i in range(total_numbers)]

if direction == "Left to right":
    numbers = np.array(numbers).reshape(num_rows, num_cols)
else:
    numbers = np.array(numbers).reshape(num_cols, num_rows).T

# Main table
df_numbers = pd.DataFrame(numbers)

if mode == "Integer":

    st.markdown(
        df_numbers.style.set_properties(**{"text-align": "center", "font-size": "50px"})
        .hide(axis=0)
        .hide(axis=1)
        .to_html(),
        unsafe_allow_html=True,
    )
elif mode == "Decimal":
    st.markdown(
        df_numbers.style.set_properties(**{"text-align": "center", "font-size": "45px"})
        .hide(axis=0)
        .hide(axis=1)
        .format("{:,.2f}")
        .to_html(),
        unsafe_allow_html=True,
    )
