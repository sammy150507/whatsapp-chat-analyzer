from urlextract import URLExtract
from wordcloud import WordCloud
from collections import Counter
import pandas as pd
import emoji

extract = URLExtract()

def fetch_stats(selected_user, df):
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]
    num_messages = df.shape[0]
    words = []
    for message in df['message']:
        words.extend(message.split())
    num_media = df[df['message'] == '<Media omitted>\n'].shape[0]
    links = []
    for message in df['message']:
        links.extend(extract.find_urls(message))
    return num_messages, len(words), num_media, len(links)

def most_busy_users(df):
    x = df['user'].value_counts().head()
    df_percent = round((df['user'].value_counts() / df.shape[0]) * 100, 2).reset_index().rename(columns={'user':'name','count':'percent'})
    return x, df_percent

def create_wordcloud(selected_user, df):
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    temp = df[df['user'] != 'group_notification'].copy()
    temp = temp[temp['message'].astype(str) != '<Media omitted>']
    temp = temp[temp['message'].astype(str).str.strip() != '']
    temp = temp[temp['message'].astype(str) != 'This message was deleted']
    temp = temp[temp['message'].astype(str) != 'You deleted this message']

    if temp.empty:
        return None

    text = ' '.join(temp['message'].astype(str).tolist())
    wc = WordCloud(width=500, height=500, min_font_size=10, background_color='white')
    df_wc = wc.generate(text)
    return df_wc