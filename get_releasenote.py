import requests
from bs4 import BeautifulSoup as bs

def get_releasenote(url):
    page = requests.get(url)
    soup = bs(page.text, "html.parser")
    elements = soup.select('div.section')
    contents = " " 

    for element in element:
        content = element.text
        contents += content
    
    return contents
