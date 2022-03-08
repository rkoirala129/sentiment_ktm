import numpy as np
import pandas as pd
import seaborn as sns
from pylab import rcParams
import matplotlib.pyplot as plt
from matplotlib import rc
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import pandas as pd
import calc_sentiment

df_sentiment = pd.read_csv("./csvs/dff_sentiment.csv")
df_wordcloud = pd.read_csv("./csvs/ktm_post_edit_new.csv")



def create_bar(story_df):
    class_names = ['negative', 'neutral', 'positive']
    ax = sns.countplot(story_df.new_sentiment)
    ax.bar_label(ax.containers[0])
    plt.xlabel('review sentiment')
    ax.set_xticklabels(class_names);
    plt.savefig('./images/sentiment_bar.png')


def create_wordcloud(story_df):
    text = story_df["Story"][0]
    wordcloud = WordCloud(max_font_size=60, max_words=30, background_color="black").generate(text)
    plt.figure(figsize=[25,12])
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.savefig('./images/sentiment_cloud.png')

create_bar(df_sentiment)

create_wordcloud(df_wordcloud)