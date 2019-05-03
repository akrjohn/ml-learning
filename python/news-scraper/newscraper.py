#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
import bs4
from news import News
import json
from json import JSONEncoder
from news import MyEncoder
import feedparser


def ndtvTopNews():
    ts = []
    ndtv = requests.get('https://www.ndtv.com/')
    rndtv = bs4.BeautifulSoup(ndtv.content)
    topstoryBlock = rndtv.find('div', {'data-tb-region': 'top-stories'})
    stories = topstoryBlock.ul.find_all('li')

    for story in stories:
        title = ''
        image = ''
        link = ''
        try:
            title = story.h2.text.strip()
        except Exception as e:
            print ('Attribute story.h2.text is not present')

        try:
            image = story.a.img['src'].strip()
        except Exception as e:
            print ('Attribute image = story.a.img src is not present')

        try:
            link = story.h2.a['href'].strip()
        except Exception as e:
            print ('Attribute link is not present')

        news = News(title, image, link, 'top', 'ndtv')
        ts.append(news)
    return ts


def timesTopNews():
    ts = []
    times = requests.get('https://timesofindia.indiatimes.com/')
    rtimes = bs4.BeautifulSoup(times.content)
    topstoryBlock = rtimes.find('div', {'id': 'lateststories'})
    stories = topstoryBlock.ul.find_all('li')

    for story in stories:
        news = News(story.a['title'], '', story.a['href'], 'top',
                    'times')
        ts.append(news)
    return ts


def deccanTopNews():
    ts = []
    url = 'https://www.deccanherald.com'
    deccan = requests.get(url)
    rdeccan = bs4.BeautifulSoup(deccan.content)
    uls = rdeccan.find_all('ul', {'class': 'grid-noslide-wrapper'})

    for ul in uls:
        lis = ul.find_all('li')
        for li in lis:
            news = News(li.find('h1').text.strip(), url + li.find('img'
                        )['src'].strip(), url + li.a['href'].strip(),
                        'top', 'deccan')
            ts.append(news)
    return ts


def topHeadlines(stories):
    for story in stories:
        print (story.title + ' --- ' + story.source)


def getAllHeadlines():
    ts = []
    ts = ndtvTopNews()
    ts += timesTopNews()
    ts += cnnTopNews()
    #ts += deccanTopNews()
    return json.dumps(ts, cls=MyEncoder)


def getByType(source):
    ts = []
    if source == 'ndtv':
        ts = ndtvTopNews()
    elif source == 'times':
        ts = timesTopNews()

    return json.dumps(ts, cls=MyEncoder)


def cnnTopNews():
    ts = []
    url = 'http://rss.cnn.com/rss/cnn_topstories.rss'
    feed = feedparser.parse('http://rss.cnn.com/rss/cnn_topstories.rss')
    entries = feed['entries']
    for e in entries:
        title = e['title']
        link = e['id']
        description = ''
        summary = e['summary']
        summaryArray = summary.split('<div class="feedflare">')
        if len(summaryArray) > 1:
            description = summaryArray[0]
            news = News(title,
                        'https://cdn.cnn.com/cnnnext/dam/assets/150325082152-social-gfx-cnn-logo-t1-main.jpg'
                        , link, 'top', 'cnn')
            news.setDescription(description)
        ts.append(news)
    return ts



            