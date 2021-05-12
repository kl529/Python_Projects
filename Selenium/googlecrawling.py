from urllib.parse import quote_plus
from bs4 import BeautifulSoup
from selenium import webdriver

baseurl = 'https://www.google.com/search?q='
plusurl = input('검색어를 입력하세요 : ')
url = baseurl + quote_plus(plusurl)

driver = webdriver.Chrome()
driver.get(url)

html = driver.page_source
soup = BeautifulSoup(html)

r= soup.select('.r')
for i in r:
    print(i.select_one('.ellip').text)
    print(i.a.attrs['href'])
    print()