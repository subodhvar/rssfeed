from django.shortcuts import render
from django.http import HttpResponse

import feedparser

def home(request):
    return render(request, 'fetch/base.html')

def hindu(request):
    # if request.GET.get("url"):
    #     url = request.GET["url"] #Getting URL
    feed = feedparser.parse("https://www.thehindu.com/news/cities/Delhi/feeder/default.rss") #Parsing XML data
    # else:
    #     feed = None
    return render(request, 'fetch/reader.html', {'feed' : feed,})

def ndtv(request):
    feed = feedparser.parse("https://feeds.feedburner.com/ndtvnews-top-stories")
    return render(request, 'fetch/reader.html', {'feed' : feed,})

def zee(request):
    feed = feedparser.parse("https://zeenews.india.com/rss/india-national-news.xml")
    return render(request, 'fetch/reader.html', {'feed' : feed,})

def toi(request):
    feed = feedparser.parse("http://timesofindia.indiatimes.com/rssfeedstopstories.cms")
    return render(request, 'fetch/reader.html', {'feed' : feed,})

def news18(request):
    feed = feedparser.parse("https://www.news18.com/rss/india.xml")
    return render(request, 'fetch/reader.html', {'feed' : feed,})

def indiatoday(request):
    feed = feedparser.parse("https://www.indiatoday.in/rss/home")
    return render(request, 'fetch/reader.html', {'feed' : feed,})
