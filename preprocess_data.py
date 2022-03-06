import nltk
import pandas as pd
# nltk.download('punkt')

def to_list(text):
    new_list = nltk.tokenize.sent_tokenize(text)
    new_df = pd.DataFrame(new_list)
    new_df = new_df.rename({0 : 'sentences'}, axis=1)
    return new_df

# story_df = pd.read_csv("./csvs/ktm_post_edit_new.csv")


# print(to_list(story_df["Story"][0]))