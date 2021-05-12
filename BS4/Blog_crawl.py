#검색어를 입력해주면 검색한 블로그들을 보여주는 프로그램
import urllib.request
import urllib.parse
from bs4 import BeautifulSoup

baseurl = 'https://search.naver.com/search.naver?where=post&sm=tab_jum&query='
plusurl = input('검색어를 입력하세요:')
url = baseurl + urllib.parse.quote_plus(plusurl)

html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html,'html.parser')

title = soup.find_all(class_='sh_blog_title')

for i in title:
    print(i.attrs['title'])
    print(i.attrs['href'])
    print()



