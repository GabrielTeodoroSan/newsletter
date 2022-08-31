from urllib.request import urlopen
from bs4 import BeautifulSoup


def createBs(url):
    html = urlopen(url)
    return BeautifulSoup(html, 'html.parser')


def getNews():
    bs = createBs('https://g1.globo.com/')
    notices = bs.find_all('a', {'class': 'feed-post-link'}, limit=4)
    return formatNews(notices)


def formatNews(news):
    formatedNews = []
    for notice in news:
        formatedNews.append([
            notice.text,
            notice.attrs['href']
        ])
    return formatedNews


if __name__ == "__main__":
    print(getNews())