from telethon import TelegramClient, sync
#import socks
from textblob import TextBlob
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

%matplotlib

# These example values won't work. You must get your own api_id and
# api_hash from https://my.telegram.org, under API Development.
api_id = 489168
api_hash = 'd176d923c48cf8e27ba5b3fd1db8d68b'

#client = TelegramClient('test-app', api_id, api_hash, proxy=(socks.SOCKS5, '67.218.149.76', 7702))
client = TelegramClient('tes-app', api_id, api_hash)
client.start()

group = client.get_entity('https://t.me/OSUniversity')

n_messages = 500
messages = client.get_messages(group, n_messages)

messages_df = pd.DataFrame(columns=['message','date'])

message_text = []
message_date = []
subjectivity = []
polarity = []

for i in range(0, n_messages):
    if messages[i].message == '':
        next
    else:
        message_text.append(messages[i].message)
        message_date.append(messages[i].date)
        analysis = TextBlob(messages[i].message)
        polarity.append(analysis.sentiment.polarity)
        subjectivity.append(analysis.sentiment.subjectivity)


messages_df['message'] = message_text
messages_df['date'] = message_date
messages_df['subjectivity'] = subjectivity
messages_df['polarity'] = polarity

polarity_daily = messages_df.groupby(messages_df.date.dt.date)['polarity'].mean()
polarity_hourly = messages_df.groupby([messages_df.date.dt.day, messages_df.date.dt.hour])['polarity'].mean()

polarity_daily = pd.DataFrame(polarity_daily)
polarity_daily['signal'] = polarity_daily['polarity'] >= 0

polarity_hourly = pd.DataFrame(polarity_hourly)
polarity_hourly['signal'] = polarity_hourly['polarity'] >= 0

plt.figure()
polarity_daily['polarity'].plot(kind='bar', color=polarity_daily.signal.map({True: 'g', False: 'r'}))
polarity_hourly['polarity'].plot(kind='bar', color=polarity_hourly.signal.map({True: 'g', False: 'r'}))

plt.plot(polarity_daily)
plt.figure

messages_df.date.dt.
print(messages_df)

print("Average Polarity", total_polarity/n_messages)
print("Average Subjectivity", total_subjectivity/n_messages)

print(client.get_me().stringify())

messages

#client.send_message('username', 'Hello! Talking to you from Telethon')
#client.send_file('username', '/home/myself/Pictures/holidays.jpg')
#
#client.download_profile_photo('me')
#messages = client.get_messages('username')
#messages[0].download_media()

