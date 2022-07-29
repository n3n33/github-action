import requests
from bs4 import BeautifulSoup as bs

def get_releasenote(url):
    page = requests.get(url)
    soup = bs(page.text, "html.parser")
    elements = soup.select('div.section')
    for index, element in enumerate(elements, 1):
        print("{} 번째 게시글의 제목: {}".format(index, element.text))

    return elements