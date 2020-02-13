import sys
import datetime
from pprint import pprint

import feedparser
import pymongo
from pymongo.mongo_client import MongoClient

arg = sys.argv
new_rss = feedparser.parse(arg[1])

client = MongoClient()
db = client.get_database("my_rss")
all_rss = db.get_collection('all_rss')

ft = new_rss.feed.title
for e in new_rss.entries:
    tt = e.published_parsed
    dt = datetime.datetime(*tt[:6], tzinfo=datetime.timezone.utc) if tt else None
    d = {
        'published_parsed': dt,
        'title': e.title,
        'link': e.link,
        'content': e.description,
        'feed_title': ft
    }
    result = all_rss.replace_one({'link': e.link}, d, upsert=True)

print('Feed added.')
