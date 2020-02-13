import datetime
from pprint import pprint

import feedparser
import pymongo
from pymongo.mongo_client import MongoClient

client = MongoClient()
db = client.get_database("my_rss")
all_rss = db.get_collection('all_rss')

all_rss.create_index([('link', pymongo.ASCENDING)], unique=True)

all_rss.create_index([('published_at', pymongo.ASCENDING)])

all_rss.delete_many({})

#kikar_hashabat_RSS = feedparser.parse("https://www.kikar.co.il/rss.php")
#tech_crunch_RSS = feedparser.parse("http://feeds.feedburner.com/TechCrunch/")
#news_RSS = feedparser.parse("https://news.ycombinator.com/rss")
#yahoo_news_RSS = feedparser.parse("https://news.yahoo.com/rss")
#world_news_RSS = feedparser.parse("http://feeds.reuters.com/Reuters/worldNews")

#RSS = [kikar_hashabat_RSS, tech_crunch_RSS, news_RSS, yahoo_news_RSS, world_news_RSS]

for rss in RSS:
    ft = rss.feed.title
    for e in rss.entries:
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

for r in all_rss.find():
    pprint(r)
    print()