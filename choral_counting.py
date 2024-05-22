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
start_num = st.sidebar.number_input(
    label="Starting number",
    value=1,
    min_value=-1000,
    max_value=1000,
    step=1,
    key="start_num",
)
increment = st.sidebar.number_input(
    label="Count by:", value=1, min_value=-1000, max_value=1000, step=1, key="increment"
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

st.markdown(
    df_numbers.style.set_properties(**{"text-align": "center", "font-size": "50px"})
    .hide(axis=0)
    .hide(axis=1)
    .to_html(),
    unsafe_allow_html=True,
)
