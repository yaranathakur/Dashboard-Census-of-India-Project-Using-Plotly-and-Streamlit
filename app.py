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

st.markdown(
    """
    <hr style="border: 2px double black; margin: 20px 0;">
""",
    unsafe_allow_html=True,
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
        zoom=2,
    )
    fig.update_layout(
        title={
            "text": "India",
            "font": {"size": 30, "color": "black"},
            "x": 0.5,
            "xanchor": "center",
            "y": 0.95,
            "yanchor": "top",
        }
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
        zoom=5,
    )
    fig.update_layout(
        title={
            "text": selected_state,
            "font": {"size": 30, "color": "black"},
            "x": 0.5,
            "xanchor": "center",
            "y": 0.95,
            "yanchor": "top",
        }
    )
    st.plotly_chart(fig, use_container_width=True)

st.markdown(
    """
    <hr style="border: 2px double black; margin: 20px 0;">
""",
    unsafe_allow_html=True,
)

with st.container():
    col1, col2 = st.columns(2)
    with col1:
        # pie chart of religion
        if selected_state == "India":
            st.markdown(
                "<h7 style='color: black; font-size: 20px;'>Religion Distribution in India</h7>",
                unsafe_allow_html=True,
            )
            religion = [
                "State",
                "District",
                "Hindus",
                "Muslims",
                "Christians",
                "Sikhs",
                "Buddhists",
                "Jains",
                "Others Religions",
                "Religion Not Stated",
            ]
            data = df[religion].sum()[2:]
            fig = px.pie(values=data, labels=data.index, names=data.index)
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.markdown(
                f"<h7 style='color: black; font-size: 20px;'>Religion Distribution in {selected_state}</h7>",
                unsafe_allow_html=True,
            )
            religion = [
                "State",
                "District",
                "Hindus",
                "Muslims",
                "Christians",
                "Sikhs",
                "Buddhists",
                "Jains",
                "Others Religions",
                "Religion Not Stated",
            ]
            data = df[religion][df[religion]["State"] == selected_state].sum()[2:]
            fig = px.pie(values=data, labels=data.index, names=data.index)
            st.plotly_chart(fig, use_container_width=True)
    with col2:
        # pie age
        if selected_state == "India":
            st.markdown(
                "<h7 style='color: black; font-size: 20px;'>Age Demographics of India</h7>",
                unsafe_allow_html=True,
            )
            age_cols = [
                "State",
                "District",
                "Age Group 0 29",
                "Age Group 30 49",
                "Age Group 50",
                "Age Not Stated",
            ]
            data = df[age_cols].sum()[2:]
            fig = px.pie(values=data, labels=data.index, names=data.index)
            st.plotly_chart(fig, use_container_width=True)

        else:
            st.markdown(
                f"<h7 style='color: black; font-size: 20px;'>Age Demographics of {selected_state}</h7>",
                unsafe_allow_html=True,
            )
            age_cols = [
                "State",
                "District",
                "Age Group 0 29",
                "Age Group 30 49",
                "Age Group 50",
                "Age Not Stated",
            ]
            data = df[age_cols][df[age_cols]["State"] == selected_state].sum()[2:]
            fig = px.pie(
                values=data,
                labels=data.index,
                names=data.index,
            )
            st.plotly_chart(fig, use_container_width=True)


st.markdown(
    """
    <hr style="border: 2px double black; margin: 20px 0;">
""",
    unsafe_allow_html=True,
)


# barplot of education
if selected_state == "India":
    st.markdown(
        "<h7 style='color: black; font-size: 20px;'>India's Educational Distribution</h7>",
        unsafe_allow_html=True,
    )
    ed_cols = [
        "State",
        "District",
        "Below Primary Education",
        "Primary Education",
        "Middle Education",
        "Secondary Education",
        "Higher Education",
        "Graduate Education",
        "Other Education",
        "Literate Education",
        "Illiterate Education",
    ]
    data = df[ed_cols].sum()[2:]
    fig = px.bar(data, x=data.index, y=data.values, color=data.index)
    fig.update_layout(showlegend=False)
    st.plotly_chart(fig, use_container_width=True)

else:
    st.markdown(
        f"<h7 style='color: black; font-size: 20px;'>{selected_state}'s Educational Distribution</h7>",
        unsafe_allow_html=True,
    )
    ed_cols = [
        "State",
        "District",
        "Below Primary Education",
        "Primary Education",
        "Middle Education",
        "Secondary Education",
        "Higher Education",
        "Graduate Education",
        "Other Education",
        "Literate Education",
        "Illiterate Education",
    ]
    data = df[ed_cols][df[ed_cols]["State"] == selected_state].sum()[2:]
    fig = px.bar(data, x=data.index, y=data.values, color=data.index)
    fig.update_layout(showlegend=False)
    st.plotly_chart(fig, use_container_width=True)


st.markdown(
    """
    <hr style="border: 2px double black; margin: 20px 0;">
""",
    unsafe_allow_html=True,
)

with st.container():
    col1, col2, col3 = st.columns(3)
    with col1:
        # sex ratio top 10 state/district
        if selected_state == "India":
            st.markdown(
                "<h7 style='color: black; font-size: 20px;'>Top 10 State by Sex Ratio</h7>",
                unsafe_allow_html=True,
            )
            temp_df = (
                df.groupby("State")["Sex Ratio"]
                .mean()
                .sort_values(ascending=False)
                .head(10)
                .reset_index()
            )
            temp_df = temp_df.set_index("State")
            st.dataframe(temp_df)
        else:
            st.markdown(
                f"<h7 style='color: black; font-size: 20px;'>Top 10 District of {selected_state} by Sex Ratio</h7>",
                unsafe_allow_html=True,
            )
            temp_df = (
                df[df["State"] == selected_state]
                .groupby("District")["Sex Ratio"]
                .mean()
                .sort_values(ascending=False)
                .reset_index()
                .head(10)
            )
            temp_df = temp_df.set_index("District")
            st.dataframe(temp_df)

    with col2:
        # literacy rate top 10 state/district
        if selected_state == "India":
            st.markdown(
                "<h7 style='color: black; font-size: 20px;'>Top 10 State by Literacy Rate</h7>",
                unsafe_allow_html=True,
            )
            temp_df = (
                df.groupby("State")["Literacy Rate"]
                .mean()
                .sort_values(ascending=False)
                .head(10)
                .reset_index()
            )
            temp_df = temp_df.set_index("State")
            st.dataframe(temp_df)
        else:
            st.markdown(
                f"<h7 style='color: black; font-size: 20px;'>Top 10 District of {selected_state} by Literacy Rate</h7>",
                unsafe_allow_html=True,
            )
            temp_df = (
                df[df["State"] == selected_state]
                .groupby("District")["Literacy Rate"]
                .mean()
                .sort_values(ascending=False)
                .reset_index()
                .head(10)
            )
            temp_df = temp_df.set_index("District")
            st.dataframe(temp_df)
    with col3:
        # households of top state/district
        if selected_state == "India":
            st.markdown(
                "<h7 style='color: black; font-size: 20px;'>Top 10 State by Number of Households</h7>",
                unsafe_allow_html=True,
            )
            temp_df = (
                df.groupby("State")["Households"]
                .sum()
                .sort_values(ascending=False)
                .head(10)
                .reset_index()
            )
            temp_df = temp_df.set_index("State")
            st.dataframe(temp_df)
        else:
            st.markdown(
                f"<h7 style='color: black; font-size: 20px;'>Top 10 District of {selected_state} by Number of Households</h7>",
                unsafe_allow_html=True,
            )
            temp_df = (
                df[df["State"] == selected_state]
                .groupby("District")["Households"]
                .sum()
                .sort_values(ascending=False)
                .reset_index()
                .head(10)
            )
            temp_df = temp_df.set_index("District")
            st.dataframe(temp_df)


st.markdown(
    """
    <hr style="border: 2px double black; margin: 20px 0;">
""",
    unsafe_allow_html=True,
)
