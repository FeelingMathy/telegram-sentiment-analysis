from telethon import TelegramClient, sync
#import socks
from textblob import TextBlob

import seaborn as sns
import matplotlib.pyplot as plt

# These example values won't work. You must get your own api_id and
# api_hash from https://my.telegram.org, under API Development.
api_id = 489168
api_hash = 'd176d923c48cf8e27ba5b3fd1db8d68b'

#client = TelegramClient('test-app', api_id, api_hash, proxy=(socks.SOCKS5, '67.218.149.76', 7702))
client = TelegramClient('tes-app', api_id, api_hash)
client.start()

group = client.get_entity('https://t.me/OSUniversity')


n_messages = 5000
messages = client.get_messages(group, n_messages)

total_polarity = 0
total_subjectivity = 0

for i in range(0, n_messages):
#    print(messages[i].message)
    analysis = TextBlob(messages[i].message)
#    print(analysis.sentiment)
    total_polarity += analysis.sentiment.polarity
    total_subjectivity += analysis.sentiment.subjectivity
#    print("")

print("Average Polarity", total_polarity/n_messages)
print("Average Subjectivity", total_subjectivity/n_messages)

print(client.get_me().stringify())

#client.send_message('username', 'Hello! Talking to you from Telethon')
#client.send_file('username', '/home/myself/Pictures/holidays.jpg')
#
#client.download_profile_photo('me')
#messages = client.get_messages('username')
#messages[0].download_media()

