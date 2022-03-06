from bs4 import BeautifulSoup
import requests
import pandas as pd


html_text = requests.get('https://kathmandupost.com/opinion/editorial').text
#print(html_text)
soup = BeautifulSoup(html_text, 'lxml')
df = pd.DataFrame(columns = ['Heading', 'Description', 'Link'])
jobs = soup.find_all('article', class_='article-image badge--editorial__block')
for job in jobs:
  heading = job.find('h3').text
  desc = job.find('p').text
  link_site = job.a['href']
  web = "https://kathmandupost.com"
  link_edit =web + link_site
  
  df = df.append({"Heading": heading, "Description": desc, "Link": link_edit}, ignore_index=True)

story_df= pd.DataFrame(columns = ['Published_Date', "Story"])
for i in range(df.shape[0]):
  html_new_text = requests.get(df["Link"][i]).text
  newsoup = BeautifulSoup(html_new_text, 'lxml')
  time_updated = newsoup.find('div', class_ = "updated-time").text
  story_section = newsoup.find('section', class_ = "story-section").text

  story_df = story_df.append({"Published_Date": time_updated, "Story": story_section}, ignore_index=True)

  story_df.to_csv("./csvs/ktm_post_edit_new.csv")