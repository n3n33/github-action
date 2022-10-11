import requests
from bs4 import BeautifulSoup as bs

def get_releasenote(url):
    page = requests.get(url)
    soup = bs(page.text, "html.parser")
    elements = soup.select('div.section')
    contents = " " 

    #for element in elements:
    #    content = element.text
    #    contents += content
    for i in range(len(elements)):
        if i % 2 != 0:
             content = "## " + elements[i].text
             contents += content
        else:
            content = elements[i].text
            contents += content
    
    return contents
