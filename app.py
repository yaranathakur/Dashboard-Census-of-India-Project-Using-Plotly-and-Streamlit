import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px

df = pd.read_csv("india.csv")

df.rename(
    columns={
        "Housholds_with_Electric_Lighting": "Housholds with Electric Lighting",
        "Households_with_Internet": "Households with Internet",
        "literacy_rate": "Literacy Rate",
        "sex_ratio": "Sex Ratio",
    },
    inplace=True,
)

states = list(df["State"].unique())
states.insert(0, "Overall India")
st.sidebar.title("India Data Visualization")
selected_state = st.sidebar.selectbox("Select a State", states)

primary = st.sidebar.selectbox("Select Primary Parameter", sorted(df.columns[5:]))
secondary = st.sidebar.selectbox("Select Secondary Parameter", sorted(df.columns[5:]))

plot = st.sidebar.button("Plot Graph")

if plot:
    st.text("Size of the Bubble Represents Primary Parameter")
    st.text("Color of the Bubble Represents Secondary Parameter")
    if selected_state == "Overall India":
        fig = px.scatter_mapbox(
            df,
            lat="Latitude",
            lon="Longitude",
            mapbox_style="carto-positron",
            zoom=3,
            size=primary,
            color=secondary,
            width=1200,
            height=800,
        )
        st.plotly_chart(fig, use_container_width=True)
    else:
        state_df = df[df["State"] == selected_state]
        fig = px.scatter_mapbox(
            state_df,
            lat="Latitude",
            lon="Longitude",
            mapbox_style="carto-positron",
            zoom=3,
            size=primary,
            color=secondary,
            width=1200,
            height=800,
            hover_name="District",
        )
        st.plotly_chart(fig, use_container_width=True)
