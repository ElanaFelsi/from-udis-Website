import feedparser

feed = feedparser.parse("https://www.kikar.co.il/rss.php")

for e in feed.entries:
    print(e.title)
    print(e.link)
    print()