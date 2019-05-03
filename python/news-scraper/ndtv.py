import requests
import bs4
from news import News
import json
from json import JSONEncoder
from news import MyEncoder
import newscraper


ts = []
ts = newscraper.ndtvTopNews()

ts += newscraper.timesTopNews()
#print(json.dumps(ts, cls=MyEncoder))
newscraper.topHeadlines(ts)


