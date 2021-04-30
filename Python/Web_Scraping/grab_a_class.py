import requests
import bs4
res=requests.get('https://en.wikipedia.org/wiki/Grace_Hopper')
soup=bs4.BeautifulSoup(res.text,'lxml')
print(soup)
print('\n')
first_item=soup.select('.toctext')[0]
print(first_item.text)

print('\n')
for item in soup.select('.toctext'):
    print(item.text)