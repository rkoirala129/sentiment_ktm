from tkinter import CENTER
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import numpy as np
import pandas as pd
import seaborn as sns
from pylab import rcParams
import matplotlib.pyplot as plt
from matplotlib import rc
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import pandas as pd
import nltk
import pandas as pd
#nltk.download('punkt')
# % matplotlib inline
# % config InlineBackend.figure_format='retina'


tokenizer = AutoTokenizer.from_pretrained('nlptown/bert-base-multilingual-uncased-sentiment')

model = AutoModelForSequenceClassification.from_pretrained('nlptown/bert-base-multilingual-uncased-sentiment')

def sentiment_score(story):
    tokens = tokenizer.encode(story, return_tensors='pt')
    result = model(tokens)
    return int(torch.argmax(result.logits))+1

def to_sentiment(rating):
  rating = int(rating)
  if rating <= 2:
    return "Negative"
  elif rating == 3:
    return "Neutral"
  else:
    return "Positive"

    
def to_list(text):
    new_list = nltk.tokenize.sent_tokenize(text)
    new_df = pd.DataFrame(new_list)
    new_df = new_df.rename({0 : 'sentences'}, axis=1)
    return new_df



def calculate_sentiment(story_df):
    story_df['sentiment'] = story_df['sentences'].apply(lambda x: sentiment_score(x[:512]))
    story_df['new_sentiment'] = story_df['sentiment'].apply(lambda x: to_sentiment(x))
    return story_df
    # story_df.to_csv("./csvs/dff_sentiment.csv")





