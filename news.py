from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests


def createBs(url):
    html = urlopen(url)
    return BeautifulSoup(html, 'html.parser')


def generateNotices():
    notices = getNews()
    for notice in notices:
        notice[2] = downloadImage(notice[2], notice[0])
    return notices


def getNews():
    bs = createBs('https://g1.globo.com/')
    notices = bs.find_all('div', {'class': 'feed-post-body'}, limit=3)
    return formatNews(notices)


def formatNews(news):
    formatedNews = []
    for notice in news:
        formatedNews.append([
            notice.find('div', {'class': 'feed-post-body-title'}).text,
            notice.find('div', {'class': 'feed-post-body-title'}).a.attrs['href'],
            notice.find('a', {'class': 'feed-post-figure-link'}).img.attrs['src']
        ])
    return formatedNews


def downloadImage(imageUrl, imageName):
    imagePath = 'images/' + imageName + '.jpg'
    image = open(imagePath, 'wb')
    response = requests.get(imageUrl)
    image.write(response.content)
    return imagePath


if __name__ == "__main__":
    print(generateNotices())