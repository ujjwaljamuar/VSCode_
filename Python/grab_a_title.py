import requests
result=requests.get('http://www.example.com')
print(type(result))
print(result.text)

import bs4
soup=bs4.BeautifulSoup(result.text,'lxml')
print(soup)

# grab things
print(soup.select('title'))
print(soup.select('h1'))
print(soup.select('title')[0].getText())

site_paragraph=soup.select('p')
print(site_paragraph)
print(type(site_paragraph[0]))

print(site_paragraph[0].getText())