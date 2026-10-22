import re
import pandas as pd

# chat file read
chat_data = []
with open('chat.txt', 'r', encoding='utf-8') as f:
    for line in f:
        pattern = r'(\d+/\d+/\d+.*)\s-\s(.*?):\s(.*)'
        m = re.match(pattern, line)
        if m:
            chat_data.append([m.group(1), m.group(2), m.group(3)])

df = pd.DataFrame(chat_data, columns=['Date','User','Message'])
print("Total Messages:", len(df))
print(df['User'].value_counts())