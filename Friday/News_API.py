import gnewsclient
from gnewsclient import gnewsclient

def getNews():
    news = []
    client = gnewsclient.NewsClient(language='english',
                                location='india',
                                topic='Nation',
                                max_results=5)


    news_list = client.get_news()

    for headline in news_list:
        news.append(headline['title'])
    return news

