import requests
from bs4 import BeautifulSoup as bs

def get_releasenote(url):
    page = requests.get(url)
    soup = bs(page.text, "html.parser")
    elements = soup.select('div.section')
    contents = " " 

    for index, element in enumerate(elements, 1):
        content = "{}".format(index, element.text)
        contents += content
    
    return contents
