from urllib.request import urlopen
from bs4 import BeautifulSoup


def getNews(keyWord):
    html = urlopen(formatUrl(keyWord))
    bs = BeautifulSoup(html, 'html.parser')
    news = bs.find_all('div', {'class': 'widget--info__text-container'}, limit=3)
    return formatNews(news)


def formatUrl(keyWord):
    return f'https://g1.globo.com/busca/?q={keyWord}'


def formatNews(news):
    notices = []
    for notice in news:
        notices.append([
            notice.find('div', {'class': 'widget--info__title'}).get_text(),
            f"https:{notice.find('a').attrs['href']}"
        ])

    return notices


if __name__ == '__main__':
    print(getNews('parana'))