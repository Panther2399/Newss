from django.shortcuts import render
from django.http import HttpResponse
from newsapi import NewsApiClient
from bs4 import BeautifulSoup
import requests
import re

from decouple import config

# Views


def home(request):

    API_KEY='417892c8bf9b4c7588155eee90e09865'
    api = NewsApiClient(api_key=API_KEY)
    topheadlines = api.get_top_headlines()

    articles = topheadlines['articles']

    desc = []
    news = []
    img = []
    url = []

    for i in range(len(articles)):
        myarticles = articles[i]

        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
        url.append(myarticles['url'])

    mylist = zip(news, desc, img, url)

    context = {'mylist': mylist}

    return render(request, 'news/index.html', context)
