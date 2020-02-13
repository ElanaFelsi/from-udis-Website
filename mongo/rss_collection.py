import datetime
from pprint import pprint

import feedparser
import pymongo
from pymongo.mongo_client import MongoClient

client = MongoClient()
db = client.get_database("my_rss")
rss_name= db.get_collection('rsss')
