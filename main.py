from bs4 import BeautifulSoup

import requests

my_web="https://news.ycombinator.com/"
response=requests.get(my_web)
page=response.text
soup=BeautifulSoup(page,"html.parser")
b=soup.find_all(name="span",class_="titleline")
first=b[0].text
while True:
    my_web = "https://news.ycombinator.com/"
    response = requests.get(my_web)
    page = response.text
    soup = BeautifulSoup(page, "html.parser")
    a = soup.find_all(name="span", class_="titleline")
    if a[0].text==first:
        pass
    else:
        for i in a:
            print(i.text)
