import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px

df = pd.read_csv("india.csv")


states = list(df['State'].unique())
states.insert(0, 'Overall India')
st.sidebar.title("India Data Visualization")
selected_state = st.sidebar.selectbox("Select a State",states)

primary = st.sidebar.selectbox("Select Primary Parameter", sorted(df.columns[5:]))
secondary = st.sidebar.selectbox("Select Secondary Parameter", sorted(df.columns[5:]))

plot = st.sidebar.button("Plot Graph")

if plot:
    if selected_state == 'Overall India':
        px.Sc
    else:
        

