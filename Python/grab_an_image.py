import requests
import bs4
res=requests.get('https://en.wikipedia.org/wiki/Deep_Blue_(chess_computer)')
soup=bs4.BeautifulSoup(res.text,'lxml')
print(soup)

print('\n')
print(soup.select('.thumbimage'))

computer=soup.select('.thumbimage')[0]
print('\n')
print(computer['src'])


print('\n')
img_link=requests.get('https://en.wikipedia.org/wiki/Deep_Blue_(chess_computer)#/media/File:Deep_Blue.jpg')
f=open('my_image.jpg','wb')
f.write(img_link.content)
f.close()