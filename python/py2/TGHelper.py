import bs4
import requests
from Movie import Movie

def commonRequest(url):
	r = requests.get(url)
	result = bs4.BeautifulSoup(r.content, "html5lib")
	return result

def tgPageIterator(url, listMovies):
	soup = commonRequest(url)
	headerList = soup.find_all('header')

	for header in headerList:
		h = header.findChild('div', {"class": "image-holder"})
		if h != None:
			m = Movie(header.img['alt'].strip(), header.img['src'].strip(), header.findChild('div', class_="view-video-play").a['href'].strip())
			listMovies.append(m)

	return listMovies


def iterateMovies(mList):
	for l in mList:
		print(l.toJson())


def getIframeMovie(iframeLink):
	bsIframe = commonRequest(iframeLink)
	iframes = bsIframe.find_all('iframe' , {'width':'100%'})
	return iframes[0]['src']

def getm38uLink(iframeLink):
	bsIframe = commonRequest(iframeLink)
	iframes = bsIframe.find_all('iframe' , {'width':'100%'})
	iframe = iframes[0]['src']
	
	return iframes[0]['src']
