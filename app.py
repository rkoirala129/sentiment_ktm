from pdb import post_mortem
from turtle import width
import streamlit as st
import pandas as pd
from torch import div
import matplotlib.pyplot as plt
from matplotlib import rc
import seaborn as sns
import calc_sentiment
from calc_sentiment import to_list,calculate_sentiment
import visualize
from visualize import *



st.write("""

    # Sentiment Classification App

    Shown below is the editorial of Kathmandu post!
"""
)

df = pd.read_csv("./csvs/ktm_post_edit_new.csv")

# Displaying the contents of each day based on selection
date_list = tuple(df.Published_Date)
result = st.sidebar.selectbox('Select the date:', date_list)
date_index_df = df.set_index("Published_Date")
data_extracted = date_index_df.loc[result, 'Story']

with st.expander("See the editorial"):
    st.write(str(data_extracted))


# Displaying the dataframe of sentiments 
df_list = to_list((str(data_extracted)))
final_df = calculate_sentiment(df_list)
st.dataframe(final_df)

# Displaying the word cloud
create_wordcloud(data_extracted)
# create_bar(final_df)

# st.image("./images/sentiment_cloud.png", caption='Popular Words')
# st.image("./images/sentiment_bar.png", caption='Bar chart of the sentiments.')

def title(s):
    st.text("")
    st.title(s)
    st.text("")

def createwordcloud(text):
    title('Popular Words of the Editorial')
    fig3 = plt.figure()
    wordcloud = WordCloud(max_font_size=60, max_words=30, background_color="black").generate(text)
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    st.pyplot(fig3)


def createbar(final_df):
    title('Sentiment Classification of the Editorial')
    fig1 = plt.figure()
    ax = sns.countplot(data=final_df , x = 'new_sentiment',order=final_df['new_sentiment'].value_counts().index)
    ax.bar_label(ax.containers[0])
    plt.xticks(rotation=45)
    # ax.set_xlabel("Sentiments", fontsize = 20)
    ax.set_xlabel("")
    st.pyplot(fig1)

createbar(final_df=final_df)
createwordcloud(text =data_extracted)