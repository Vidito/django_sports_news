from django.shortcuts import render
import requests

def index(request):
    r = requests.get('https://newsapi.org/v2/top-headlines?country=gb&category=sports&apiKey=###')
    res = r.json()
    data = res['articles']
    author = []
    title = []
    source = []
    date = []
    url = []
    description = []
    for i in data:
        author.append(i['author'])
        title.append(i['title'])
        source.append(i['source']['name'])
        dates = i['publishedAt'].replace('T', ' ')
        dates = dates.replace('Z', '')
        date.append(dates)
        url.append(i['url'])
        description.append(i['description'])
    news = zip(author,title, description,date,url,source)
    return render(request, 'index.html', {'news':news} )
