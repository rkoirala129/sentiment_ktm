from pdb import post_mortem
from turtle import width
import streamlit as st
import pandas as pd
from torch import div
import matplotlib.pyplot as plt
import seaborn as sns



st.write("""

    # Sentiment Classification App

    Shown below is the sentiment of editorial of Kathmandu post!
"""
)
st.image("./images/sentiment_cloud.png", caption='Popular Words')

st.image("./images/sentiment_bar.png", caption='Bar chart of the sentiments.')

df = pd.read_csv("./csvs/dff_sentiment.csv")
df = df.iloc[: , 1:]


st.dataframe(df)
"""

"""

