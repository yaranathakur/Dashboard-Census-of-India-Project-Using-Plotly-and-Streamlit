import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px
import millify

st.set_page_config(
    layout="wide",
    page_title="Census of India 2011",
    page_icon="🧊",
    initial_sidebar_state="expanded",
    menu_items={
        "Get Help": "https://www.extremelycoolapp.com/help",
        "Report a bug": "https://www.extremelycoolapp.com/bug",
        "About": "# This is a header. This is an *extremely* cool app!",
    },
)

df = pd.read_csv("indiaDetailed.csv")


states = list(df["State"].unique())
states.insert(0, "India")
st.sidebar.title("India Data Visualization")
selected_state = st.sidebar.selectbox("Select a State", states)

primary = st.sidebar.selectbox("Select Primary Parameter", df.columns[5:])
secondary = st.sidebar.selectbox("Select Secondary Parameter", df.columns[5:])


# cards
st.markdown(
    f"""
    <h1 style='
        text-align: center;
        color: #ff5733; 
        font-size: 50px;
        font-family: Arial,
        font-weight: bold;
        border: 2px solid #ff5733;
        border-radius: 10px;
        padding: 10px;
        background-color: #f0f0f0;
    '>{selected_state}</h1>
""",
    unsafe_allow_html=True,
)

with st.container():
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        if selected_state == "India":
            st.metric(
                label="Population",
                value=millify.millify(df["Population"].sum(), precision=2),
            )
        else:
            st.metric(
                label="Population",
                value=millify.millify(
                    df[df["State"] == selected_state]["Population"].sum(), precision=2
                ),
            )
    with col2:
        if selected_state == "India":
            st.metric(
                label="Sex Ratio",
                value=int(df["Sex Ratio"].mean()),
            )
        else:
            st.metric(
                label="Sex Ratio",
                value=int(df[df["State"] == selected_state]["Sex Ratio"].mean()),
            )
    with col3:
        if selected_state == "India":
            st.metric(
                label="Literacy Rate",
                value=int(df["Literacy Rate"].mean()),
            )
        else:
            st.metric(
                label="Literacy Rate",
                value=int(df[df["State"] == selected_state]["Literacy Rate"].mean()),
            )
    with col4:
        if selected_state == "India":
            st.metric(
                label="Households",
                value=millify.millify(df["Households"].sum(), precision=2),
            )
        else:
            st.metric(
                label="Households",
                value=millify.millify(
                    df[df["State"] == selected_state]["Households"].sum(), precision=2
                ),
            )


st.text(f"Size : {primary} & Color: {secondary}")
if selected_state == "India":
    fig = px.scatter_mapbox(
        df,
        lat="Latitude",
        lon="Longitude",
        mapbox_style="carto-positron",
        size=primary,
        color=secondary,
        title="India",
        zoom=2,
    )
    st.plotly_chart(fig, use_container_width=True)
else:
    state_df = df[df["State"] == selected_state]
    fig = px.scatter_mapbox(
        state_df,
        lat="Latitude",
        lon="Longitude",
        mapbox_style="carto-positron",
        size=primary,
        color=secondary,
        hover_name="District",
        title=selected_state,
        zoom=5,
    )
    st.plotly_chart(fig, use_container_width=True)
