import numpy as np
import pandas as pd
import streamlit as st
import altair as alt
from wordcloud import WordCloud
import plotly.express as px
from add_data import db_execute_fetch

def loadData():
    query = "select * from TweetInformation"
    df = db_execute_fetch(query, dbName="tweetInfodb", rdf=True)
    return df

def barChart(data, title, X, Y):
    title = title.title()
    st.title(f'{title} Chart')
    msgChart = (alt.Chart(data).mark_bar().encode(alt.X(f"{X}:N", sort=alt.EncodingSortField(field=f"{Y}", op="values",
                order='ascending')), y=f"{Y}:Q"))
    st.altair_chart(msgChart, use_container_width=True)

def stBarChart():
    df = loadData()
    dfCount = pd.DataFrame({'Tweet_count': df.groupby(['original_author'])['original_text'].count()}).reset_index()
    dfCount["original_author"] = dfCount["original_author"].astype(str)
    dfCount = dfCount.sort_values("Tweet_count", ascending=False)

    num = st.slider("Select number of Rankings", 0, 50, 21)
    title = f"Top {num} Ranking By Number of tweets"
    barChart(dfCount.head(num), title, "original_author", "Tweet_count")

def app():
    st.title('Home Page')
    st.write('Home Page ...')
    stBarChart()

